# Lab 9: Network of Brokers

In this exercise, you will learn about two critical aspects of large enterprise scale messaging systems. **High Availability** and **Connection Scaling**. First, we will cover some key concepts which will help set the stage and then we will dive into those concepts using a few exercises.

## Introduction

In order to provide massive scalability, Amazon MQ supports a feature known as Network of Brokers. In this configuration you can connect multiple single or active/standby brokers into a network using a topology. Each active/standby broker runs in two availability zones, with messages stored in a shared durable storage (EFS). Thus, providing high availability and message durability in itself.

While there are many different topologies for connecting brokers - [there are a few topology patterns described in AWS documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/network-of-brokers.html#nob-topologies).

If you are running the **advanced** Lab (by either choosing **advanced** or **all** as Lab Type when deploying the CloudFormation), the default mesh broker topology is deployed with active/standby broker configuration.

In the Mesh topology, Broker 1 and Broker 2, Broker 2 and Broker 3, Broker 1 and Broker 3 are connected with each other using OpenWire network connectors. Please follow the instructions below to understand how Broker network is configured in a Mesh topology. 

Go to AWS Console, Open console for Amazon MQ, find one of the mesh brokers, the name of the broker is CloudFormation {Stackname}-Broker1, {Stackname}-Broker2 or {Stackname}-Broker3.

In the broker details page, you should see "Configuration revision", under this click on the link to open Broker Configuration. 

<details><summary>An example screenshot is shown below</summary><p>

![Mesh Broker Configuration](/images/mesh-broker-config.png)

</details>

In the XML broker configuration, look for ```<networkConnectors>```. In this XML item, you will see **four** ```<networkConnector>``` blocks. Two for queues and Two for topics. For each queue and topic, a set of ```<networkConnector>``` items each for connection from the current broker and two other brokers in the mesh.

Each networkConnector establishes a connection from one broker to another in a specific direction. A networkConnector from Broker1 to Broker2, propagates messages from Broker1 to Broker2. In order for Broker2 to send messages to Broker1, either add an explicit networkConnector from Broker2 to Broker1 or mark the Broker1 to Broker2 networkConnector with **duplex** attribute. There are two key points here for you to remember:

>In a network of brokers, messages flow between brokers on using networkConnectors only when a consumer demands them. The messages do not flow to other brokers if no consumer is available. For example, when producer sends messages to Broker1, if no consumer exists on Broker2 or Broker3, the messages remain in Broker1. However, there is a special configuration ```staticallyIncludedDestinations``` which if set with specific destinations, brokers will forward messages to those destinations even without a consumer.

>The **duplex** attribute on networkConnector essentially establishes a two-way connection on the same port. This would be useful when network connections are traversing a firewall and is common in **Hub and Spoke** broker topology. In a Mesh topology, it is recommended to use explicit unidirectional networkConnector as it allows flexibility to include or exclude destinations.

Each broker can accept connections from clients. The client endpoints are named ```transportConnectors```.  In order to scale, client connections can be divided across brokers.
Because these brokers are all connected using network connectors, when a producer sends messages to say Broker 1, the messages can be consumed from Broker 2 or from Broker 3. This helps to distribute the load from clients across brokers in Mesh. 

## Producer Load Balancing

Producers can be load balanced across the network of brokers, by concentrating them on a set of brokers in the network. For example, in a Mesh network of 3 brokers, producers can be spread across Broker1 and Broker2. The consumers can be connected to Broker3.

## Consumer Load Balancing

In the networkConnector configuration you should have noticed an attribute named ```conduitSubscriptions```. This setting specifies how the messages are distributed. **By default, AmazonMQ sets ```conduitSubscriptions``` to ```false```**

![conduitSubscriptions enabled](/images/nob-conduit-true.png)

When ```conduitSubscriptions``` set to ```true```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees two connections, one for Broker1 and another for Consumer1. So, it distributes 60 messages, 30 each for Broker1 and rest 30 for Consumer1. For Broker2, since there are two consumers, each consumer receives 15 messages each. This is an uneven distribution of messages.

In order to distribute the messages evenly among all subscriptions, ```conduitSubscriptions``` should set to ```false``` (default in AmazonMQ).

![conduitSubscriptions disabled](/images/nob-conduit-false.png)

When ```conduitSubscriptions``` set to ```false```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees three connections, one consumer for Broker1 and two consumers on Broker2 and distributes messages equally among all consumers. Each consumer receives 20 messages.

## High Availability

When an active/standby broker configured within a Network of Brokers, the standby broker is redundant till active broker fails. In addition, in a Network of Brokers, if both active and standby brokers fail, other brokers in the network can share the load. The client connections to the failed broker can be automatically rebalanced to other brokers **without a change in application code or configuration**. The same applies when you add new brokers to the existing network. This feature is controlled by the following attributes in **transportConnector**. Both of the settings must be set to true to rebalance connections when a new broker is added or a broker fails.

>```updateClusterClients = true``` - This informs clients about new broker joining the network. Application code then choose to connect to new broker.
```rebalanceClusterClients = true``` - This automatically disconnects the client connection and reconnects the client to an active broker.

### :white_check_mark: 1. Prerequisites

For the Advanced Lab, you should have a mq.m5.large instance running for performance testing. In addition, you should also see a set of 3 brokers setup in a Mesh configuration. 

<details><summary>Store environment variable</summary><p>

To make it easier to run the commands in the following labs we store frequently used parameters like the Amazon MQ broker URL in Bash environment variable.

Go to the [AmazonMQ console](https://console.aws.amazon.com/amazon-mq), and click on the name of the broker (the one prefixed with CloudFormation stack name you created)

:white_check_mark: Scroll down to the Connections section and click the **Copy failover string** link beside the OpenWire row 
to copy the string to your clipboard. You need to **repeat this 3 more times** for capturing and saving broker failover URLs for the brokers in Mesh network.

![Copy failover link](/images/fail-over-Step2.png)

:white_check_mark: Go to the AWS Console home, find Cloud9 service, open the service console. You should see a pre-built workspace named MQClient. Click on "Open IDE". 
Once the IDE is launched, you should see a bash shell window opened with the workshop github repository synced to amazon-mq-workshop folder.
In the bash shell, type the following commands one at a time (make sure you replace <failover URL> with the failover URL you copied below).

``` bash

cd ~/environment/amazon-mq-workshop
export temp_url="<{Stackname}Broker failover URL>"
export temp1_url="<{Stackname}Broker1 in Mesh failover URL>"
export temp2_url="<{Stackname}Broker2 in Mesh failover URL>"
export temp3_url="<{Stackname}Broker3 in Mesh failover URL>"
echo "perfurl=\"$temp_url\"" >> ~/.bashrc; 
echo "mesh1url=\"$temp1_url\"" >> ~/.bashrc; 
echo "mesh2url=\"$temp2_url\"" >> ~/.bashrc; 
echo "mesh3url=\"$temp3_url\"" >> ~/.bashrc; 
source ~/.bashrc
./setup.sh
```
</details>

:white_check_mark: **NOTE**: Ensure that all terminals windows that you will use for the workshop are created after having run this step.

### 2. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4 terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
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

Now let's run another receiver as follows. 

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh3url -mode receiver -type queue -destination workshop.queueA 
```
Now you should notice that messages are being distributed equally among two receivers and receivers are reading from the same queue on two different brokers. This is the result of conduitSubscriptions (false) that you learned earlier in this lab.

## Scenario 2 : Producer Load Balancing 

Run and repeat the following command in two separate terminals to start 2 producers connecting to Broker1. 

``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh1url -mode sender -type queue -destination workshop.queueA -name Sender-1
```

Run the following two commands to start receivers in two separate terminals each connecting to Broker2 and Broker3.


``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh2url -mode receiver -type queue -destination workshop.queueA 
```
``` bash
java -jar ./bin/amazon-mq-client.jar -url $mesh3url -mode receiver -type queue -destination workshop.queueA 
```
This is a simple demonstration to have two producers on one broker and two consumers each on different brokers. Leave them running for the next exercise.

## Scenario 3 : High Availability

The following block uses the two settings we discussed above (shown here for your reference). This was already added to the CloudFormation script.

```
  <transportConnectors>
    <transportConnector name="openwire" rebalanceClusterClients="true" updateClusterClients="true"/>
  </transportConnectors>
```

Assuming that you left the producers and consumers running from the previous Scenario. If not, start them again as per instructions in Scenario 2. 

Now, go to AWS Console, Open AmazonMQ console, pick Broker1 (or any broker) and reboot the broker. Now notice the applications running in the terminals, you should have noticed that client connections are automatically updated to available broker's URL and rebalanced to available brokers. Once the rebooted broker is in Running state, the client connections get rebalanced again. This is very powerful feature as you can simply add more brokers into the network using CloudFormation and clients get rebalanced.

An example output shown below. The connections automatically rebalance between available brokers.

### Output from Sender

```
[ActiveMQ Transport: ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com/10.42.1.21:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (nio+ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
        at java.io.DataInputStream.readInt(DataInputStream.java:392)
        at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
        at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
        at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
        at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
        at java.lang.Thread.run(Thread.java:748)
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-3f5547ed-5874-4ee7-ae65-2033dfe309fa-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:19.589 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 267'
07.09.2019 18:05:20.603 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 268'
07.09.2019 18:05:21.617 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 269'
07.09.2019 18:05:22.640 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 270'
07.09.2019 18:05:23.651 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 271'
07.09.2019 18:05:24.970 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 272'
07.09.2019 18:05:25.981 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 273'
07.09.2019 18:05:27.2 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 274'
07.09.2019 18:05:28.17 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 275'
07.09.2019 18:05:29.28 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 276'
07.09.2019 18:05:30.40 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 277'
07.09.2019 18:05:31.55 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 278'
07.09.2019 18:05:32.65 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 279'
07.09.2019 18:05:33.75 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 280'
07.09.2019 18:05:34.86 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 281'
[ActiveMQ Task-4] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-6c8721b5-7112-40ba-a7bf-ae2d06091f3a-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:35.109 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 282'
07.09.2019 18:05:36.126 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 283'
```

### Output from receiver 1

```
07.09.2019 18:05:18.512 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 266'
[ActiveMQ Transport: ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com/10.42.1.21:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
        at java.io.DataInputStream.readInt(DataInputStream.java:392)
        at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
        at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
        at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
        at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
        at java.lang.Thread.run(Thread.java:748)
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-6c8721b5-7112-40ba-a7bf-ae2d06091f3a-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:20.599 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 268'
07.09.2019 18:05:22.626 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 270'
07.09.2019 18:05:24.659 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 272'
07.09.2019 18:05:26.989 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 274'
07.09.2019 18:05:29.23 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 276'
07.09.2019 18:05:31.46 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 278'
07.09.2019 18:05:33.71 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 280'
[ActiveMQ Task-4] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-3f5547ed-5874-4ee7-ae65-2033dfe309fa-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:36.117 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 283'
07.09.2019 18:05:38.158 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 285'
```

### Output from receiver 2
```
07.09.2019 18:05:17.497 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 265'
[ActiveMQ Transport: ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com/10.42.1.21:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (nio+ssl://b-6b42ffae-aed6-48cf-9b70-05817d4f7e1b-1.mq.us-east-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
        at java.io.DataInputStream.readInt(DataInputStream.java:392)
        at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
        at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
        at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
        at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
        at java.lang.Thread.run(Thread.java:748)
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-6c8721b5-7112-40ba-a7bf-ae2d06091f3a-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:19.638 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 267'
07.09.2019 18:05:21.610 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 269'
07.09.2019 18:05:23.647 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 271'
07.09.2019 18:05:25.976 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 273'
07.09.2019 18:05:28.9 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 275'
07.09.2019 18:05:30.36 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 277'
07.09.2019 18:05:32.61 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 279'
07.09.2019 18:05:34.82 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 281'
[ActiveMQ Task-4] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to nio+ssl://b-3f5547ed-5874-4ee7-ae65-2033dfe309fa-1.mq.us-east-1.amazonaws.com:61617
07.09.2019 18:05:35.99 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 282'
07.09.2019 18:05:37.133 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 284'
07.09.2019 18:05:39.181 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 286'
```

If your application needs a way to handle the interruption and resumption of connections, you can implement a [TransportListener](https://activemq.apache.org/maven/apidocs/src-html/org/apache/activemq/transport/TransportListener.html#line.33)

# Completion

Congratulations, you've successfully completed Lab 9! You can move on to [Lab 10: Performance Testing](/labs/lab-10.md)

[Return to the Workshop Landing page](/README.md)
