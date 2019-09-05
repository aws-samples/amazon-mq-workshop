# Lab 9: Network of Brokers

In this exercise, you will learn about two critical aspects of large enterprise scale messaging systems. **High Availability** and **Connection Scaling**. In Lab 10, you will learn about **Message Scaling**. First we will cover some key concepts which will help set the stage and then we will dive into those concepts using a few exercises.

## Introduction

In order to provide massive scalability, Amazon MQ supports a feature known as Network of Brokers. In this configuration you can connect multiple single or active/standby brokers into a network using a topology. Each active/standby broker runs in two availability zones, with messages stored in a shared durable storage (EFS). Thus providing high availability and message durability in itself.

While there are many different topologies for connecting brokers - [there are a few topology patterns described in AWS documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/network-of-brokers.html#nob-topologies).

If you are running an Advanced Lab (by either choosing **advanced** or **all** as Lab Type when deploying the CloudFormation), the default mesh broker topology is deployed with active/standby broker configuration.

In the Mesh topology, Broker 1 and Broker 2, Broker 2 and Broker 3, Broker 1 and Broker 3 are connected with each other using OpenWire network connectors. Please follow the instructions below to understand how Broker network is configured in a Mesh topology. 

Go to AWS Console, Open console for Amazon MQ, find one of the mesh brokers, the name of the broker is CloudFormation {Stackname}-Broker1, {Stackname}-Broker2 or {Stackname}-Broker3.

In the broker details page, you should see "Configuration revision", under this click on the link to open Broker Configuration. 

<details><summary>An example screenshot is shown below</summary><p>

![Mesh Broker Configuration](/images/mesh-broker-config.png)

</details>

In the XML broker configuration, look for ```<networkConnectors>```. In this XML item, you will see **four** ```<networkConnector>``` blocks. Two for queues and Two for topics. For each queue and topic, a set of ```<networkConnector>``` items each for connection from the current broker and two other brokers in the mesh.

Each networkConnector establishes a connection from one broker to another in a specific direction. A networkConnector from Broker1 to Broker2, propogates messages from Broker1 to Broker2. In order for Broker2 to send messages to Broker1, either add an explicit networkConnector from Broker2 to Broker1 or mark the Broker1 to Broker2 networkConnector with **duplex** attribute. There are two key points here for you to remember:

> In a network of brokers, messages flow between brokers on using networkConnectors only when a consumer demands them. The messages do not flow to other brokers if no consumer is available. For example, when producer sends messages to Broker1, if no consumer exists on Broker2 or Broker3, the messages remain in Broker1. 

>The **duplex** attribute on networkConnector essentially establishes a two-way connection on the same port. This would be useful when network connections are traversing a firewall and is common in **Hub and Spoke** broker topology. In a Mesh topology, it is recommended to use explicit unidirectional networkConnector as it allows flexibility to include or exclude destinations.

Each broker can accept connections from clients. The client endpoints are named ```transportConnectors```.  In order to scale, client connections can be divided across brokers.
Because these brokers are all connected using network connectors, when a producer sends messages to say Broker 1, the messages can be consumed from Broker 2 or from Broker 3. This helps to distribute the load from clients across brokers in Mesh. 

## Producer Load Balancing

Producers can be load balanced across the network of brokers, by concentrating them on a set of brokers in the network. For example, In a Mesh network of 3 brokers, all producers can be connected to Broker1 and all consumers can be connected to Broker3, leaving Broker2 as a redundant instance in case either Broker1 or Broker3 are unavailable.

## Consumer Load Balancing

In the networkConnector configuration you should have noticed an attribute named ```conduitSubscriptions```. This setting specifies how the messages are distributed. **By default AmazonMQ sets ```conduitSubscriptions``` to ```false```**

![conduitSubscriptions enabled](/images/nob-conduit-true.png)

When ```conduitSubscriptions``` set to ```true```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees two connections, one for Broker1 and another for Consumer1. So it distributes 60 messages, 30 each for Broker1 and rest 30 for Consumer1. For Broker2, since there are two consumers, each consumer receives 15 messages each. This is an uneven distribution of messages.

In order to distribute the messages evenly among all subscriptions, ```conduitSubscriptions``` should set to ```false``` (default in AmazonMQ).

![conduitSubscriptions disabled](/images/nob-conduit-false.png)

When ```conduitSubscriptions``` set to ```false```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees three connections, one consumer for Broker1 and two consumers on Broker2 and distributes messages equally among all consumers. So each consumer receives 20 messages each.

## High Availability

When an active/standby broker configured within a Network of Brokers, the standby broker is redundant till active broker fails. In addition, in a Network of Brokers, if both active and standby brokers fail, other brokers in the network can share the load. The client connections to the failed broker can be automatically rebalanced to other brokers **without a change in application code or configuration**. The same applies when you add new brokers to the existing network. This feature is controlled by the following attributes in **transportConnector**. Both of the settings must be set to true to rebalance connections when a new broker is added or a broker fails.

| Attribute | Description |
| --------- | ----------- |
| updateClusterClients = true | This informs clients about new broker joining the network. Application code then choose to connect to new broker. |
| rebalanceClusterClients = true | This automatically disconnects the client connection and reconnects the client to an active broker |

### :white_check_mark: 1. Prerequisites

For the Advanced Lab, You should have a mq.m5.large instance running for performance testing. In addition, you should also see a set of 3 brokers setup in a Mesh configuration. 

<details><summary>Store environment variable</summary><p>

To make it easier to run the commands in the following labs we store frequently used parameters like the Amazon MQ broker url in Bash environment variable.

Go to the [AmazonMQ console](https://console.aws.amazon.com/amazon-mq), and click on the name of the broker (the one prefixed with CloudFormation stack name you created)

:white_check_mark: Scroll down to the Connections section and click the **Copy failover string** link beside the OpenWire row 
to copy the string to your clipboard. You need to **repeat this 3 more times** for capturing and saving broker failover urls for the brokers in Mesh network.

![Copy failover link](/images/fail-over-Step2.png)

:white_check_mark: Go to the AWS Console home, find Cloud9 service, open the service console. You should see a pre-built workspace named MQClient. Click on "Open IDE". 
Once the IDE is launched, you should see a bash shell window opened with the workshop github repository synced to amazon-mq-workshop folder.
In the bash shell, type the following commands one at a time (make sure you replace <failover url> with the failover url you copied below).

``` bash
cd ~/environment/amazon-mq-workshop
export temp_url="<failover url>"
export temp1_url="<failover url>"
export temp2_url="<failover url>"
export temp3_url="<failover url>"
echo "perfurl=\"$temp_url\"" >> ~/.bashrc; 
echo "mesh1url=\"$temp1_url\"" >> ~/.bashrc; 
echo "mesh2url=\"$temp2_url\"" >> ~/.bashrc; 
echo "mesh3url=\"$temp3_url\"" >> ~/.bashrc; 
source ~/.bashrc
./setup.sh
```
</details>

### 2. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals should be in the `/environment/amazon-mq-workshop` directory.

**NOTE**: In order to split the windows into a chequered pattern, on the 2nd and 4th terminal windows, right click and select "Split Pane in Two Columns" and navigate to the projects root directory by running 'cd amazon-mq-workshop' 

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>


## Scenario 1 : Consumer Load Balancing 

Run the following commands in each of the terminal to start 1 producer to send messages to Broker1. Once this done, give a couple of seconds to start the flow of messages, run the 2nd command to start a receiver on Broker2.

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh1url -mode sender -type queue -destination workshop.queueA -name Sender-1
```

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh2url -mode receiver -type queue -destination workshop.queueA 
```
With both of the above commands running, you can see that while producer is producing messages to Broker1, a receiver is reading messages from the same queue from a different broker i.e. Broker2.

Now lets run another receiver as follows. 

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh3url -mode receiver -type queue -destination workshop.queueA 
```
Now you should notice that messages are being distributed equally among two receivers and receivers are reading from the same queue on two different brokers. This is the result of conduitSubscriptions (false) that you learned earlier in this lab.

## Scenario 2 : Producer Load Balancing 

Run the following command in two terminals to start 2 producers to Broker1. Once this is done, give a couple of seconds to start the flow of messages, run the 2nd command to start 1 consumer on Broker2 and another on Broker3 in other two terminals. 

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh1url -mode sender -type queue -destination workshop.queueA -name Sender-1
```
``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh2url -mode receiver -type queue -destination workshop.queueA 
```
``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh3url -mode receiver -type queue -destination workshop.queueA 
```
This is a simple demonstration to have two producers on one broker and two consumers each on different brokers. Leave them running for the next exercise.

## Scenario 3 : High Availability

The following block uses the two settings we discussed above. This was already added to the CloudFormation script. 

```
  <transportConnectors>
    <transportConnector name="openwire" rebalanceClusterClients="true" updateClusterClients="true"/>
  </transportConnectors>
```

Assuming that you left the producers and consumers running. If not, start them again. 

Now, Go to AWS Console, Open AmazonMQ console, pick Broker1 (or any broker) and reboot the broker. Now notice the applications running in the terminals, you should have noticed that client connections are automatically rebalanced to available brokers. Once the rebooted broker is in Running state, the client connections get rebalanced again.  

# Completion

Congratulations, you've successfully completed Lab 9! You can move on to [Lab 10: Performance Testing](/labs/lab-10.md)

[Return to the Workshop Landing page](/README.md)
