# Lab 9: Network of Brokers

In order to provide massive scalability, Amazon MQ supports a feature known as Network of Brokers. In this configuration you can connect multiple single or dual instance brokers into a newtwork using a topology.

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
to copy the string to your clipboard.

![Copy failover link](/images/fail-over-Step2.png)

:white_check_mark: Go to the AWS Console home, find Cloud9 service, open the service console. You should see a pre-built workspace named MQClient. Click on "Open IDE". 
Once the IDE is launched, you should see a bash shell window opened with the workshop github repository synced to amazon-mq-workshop folder.
In the bash shell, type the following commands one at a time (make sure you replace <failover url> with the failover url you copied below).

``` bash
cd ~/environment/amazon-mq-workshop
export temp_url="<failover url>"
echo "url=\"$temp_url\"" >> ~/.bashrc; source ~/.bashrc
./setup.sh
```

# Completion

Congratulations, you've successfully completed Lab 9! You can move on to [Lab 10: Performance Testing](/labs/lab-10.md)

[Return to the Workshop Landing page](/README.md)
