# Lab 9: Network of Brokers

In order to provide massive scalability, Amazon MQ supports a feature known as Network of Brokers. In this configuration you can connect multiple single or dual instance brokers into a network using a topology.

There are no predefined rules for connecting brokers, [there are a few topology patterns described in AWS documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/network-of-brokers.html#nob-topologies)..

If you are running an Advanced Lab (by either choosing advanced or all as Lab Type when delpoying the CloudFormation), the default mesh broker topology is deployed with active/standby instance configuration.

In the Mesh topology, Broker 1 and Broker 2, Broker 2 and Broker 3, Broker 1 and Broker 3 are connected with each other using OpenWire Transports.

Go to AWS Console, Open console for Amazon MQ, find one of the mesh brokers, the name of the broker is CloudFormation stack name-Broker(1, 2 or 3).

In the broker details page, you should see "Configuration revision", under this click on the link to open Broker Configuration. An example screenshot is shown below.

![Mesh Broker Configuration](/images/mesh-broker-config.png)

In the XML broker configuration, look for ```<networkConnectors>```. In this XML item, you will see **four** ```<networkConnector>``` blocks. Two for queues and Two for topics. For each queue and topic, a set of ```<networkConnector>``` items each for connection from the current broker and two other brokers in the mesh.

Each broker can accept connections from clients. In order to scale, client connections can be divided across the three brokers in the mesh.

When a producer sends messages to say Broker 1, the messages can be consumed from Broker 2 or from Broker 3. This helps to distribute the load from clients across brokers in Mesh. 

### :white_check_mark: 1. Prerequisites

For the Advanced Lab, You should have a mq.m5.large instance running for performance testing. In addition, you should also see a set of 3 brokers setup in a Mesh configuration. 

<details><summary>Store environment variable</summary><p>

To make it easier to run the commands in the following labs we store frequently used parameters like the Amazon MQ broker url in Bash environment variable.

Go to the [AmazonMQ console](https://console.aws.amazon.com/amazon-mq), and click on the name of the broker (the one with a name starting with the stack name you created)

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

## Network Connectors

Each network connector establishes a connection from one broker to another in a specific direction. A network connector from Broker1 to Broker2, propogates messages from Broker1 to Broker2.

Network connectors can be established from Broker2 to Broker1 to allow flow of messages from Broker2 to Broker1. 

There is an attribute ```duplex``` when set to ```true``` allows a bidirectional flow of messages on the same network connector. If this flag is set to ```false``` (default), the direction of messages is considered unidirectional.

The ```duplex``` flag is useful when network connections are traversing a firewall and is common in **Hub and Spoke** broker topology.

For each broker we can configure multiple network connectors. Each network connector in a broker can be configured to include or exclude specific destinations. This would be helpful to distribute the queue/topic load across multiple connectors.

## Conduit Subscriptions

In the networkConnector configuration you should have noticed an attribute named ```conduitSubscriptions```. This setting specifies how the messages are distributed. By default AmazonMQ sets this to ```false```

![conduitSubscriptions enabled](/images/nob-conduit-true.png)

When ```conduitSubscriptions``` set to ```true```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees two connections, one for Broker1 and another for Consumer1. So it distributes 60 messages, 30 each for Broker1 and rest 30 for Consumer1. 

For Broker2, since there are two consumers, each consumer receives 15 messages each. This is an uneven distribution of messages.

In order to distribute the messages evenly among all subscriptions, ```conduitSubscriptions``` should set to ```false``` (default in AmazonMQ).

![conduitSubscriptions disabled](/images/nob-conduit-false.png)

When ```conduitSubscriptions``` set to ```true```, taking an example (see above diagram), when Producer1 sends 60 messages to Broker1, Broker1 sees three connections, one consumer for Broker1 and two consumers on Broker2 and distributes messages equally among all consumers. So each consumer receives 20 messages each.

## TTL Concepts



### messageTTL


![Message TTL](/images/nob-message-ttl.png)

### consumerTTL

![ConsumerTTL](/images/nob-consumer-ttl.png)

## Scenario 1 : Produce/Consume to/from same broker

## Scenario 2 : Produce to Broker 1 and Consume from Broker 2

## Scenario 3 : duplex

## Scenario 4 : conduitSubscriptions

# Completion

Congratulations, you've successfully completed Lab 9! You can move on to [Lab 10: Performance Testing](/labs/lab-10.md)

[Return to the Workshop Landing page](/README.md)
