# Lab 8: Protocol interoperability

In this exercise, you are connecting one of the message producer to the broker and start sending message. Afterwards, you connect one of the message consumer to the broker, using a different protocol. We will repeat this with multiple protocol combinations to figure out, which protocol conversions are supported by Amazon MQ.  
You your ec2-user home directory, you will find the following executable:
* amazon-mq-client.jar (using the OpenWire protocol) - [Source](https://github.com/muellerc/Amazon-MQ-Workshop/blob/master/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java)
* amqp-client.jar (using the AMQP protocol) - [Source](https://github.com/muellerc/Amazon-MQ-Workshop/blob/master/amqp-client/src/main/java/com/aws/sample/amazonmq/AMQPClient.java)
* mqtt-client.jar (using the MQTT protocol) - [Source](https://github.com/muellerc/Amazon-MQ-Workshop/blob/master/mqtt-client/src/main/java/com/aws/sample/amazonmq/MQTTClient.java)
* stomp-client.jar (using the Stomp protocol) - [Source](https://github.com/muellerc/Amazon-MQ-Workshop/blob/master/stomp-client/src/main/java/com/aws/sample/amazonmq/StompClient.java)

1\. Open an SSH session to your EC2 instance and start a new **tmux** session:

```
tmux
```

To split your terminal window into 4 individual screens, run the following commands:

```
CTRL + b "
CTRL + b %
CTRL + b [arrow key up]
CTRL + b %
CTRL + b [arrow key left]
```

**CTRL+b "** will split your active screen horizontally and **CTRL+b %** will split your active screens vertically. With **CTRL+b [arrow key up|down|left|right]** you can navigate between the different screens to chose the one to work with.

The top left screen should be your active screen now.

<details><summary>Screenshot step 1</summary><p>

![Amazon MQ workshop lab 8 step 1](/images/tmux-session.png)

</p></details><p/>


2\. Run the following command to start a sender using the **OpenWire** protocol:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type topic -destination workshop.topicA -name OpenWire
```

You should see a log output like the following one:

```
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```

3\. Type  

```
CTRL + b [arrow key right]
```

to choose the upper right window. Run the following command to start a receiver using the **Stomp** protocol (first replace **<Stomp single connection url>** with your current broker value):

  * URL: This client doesn't support the failover connection url. You have to provide the Stomp connection url for the active broker, like **stomp+ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61614**.

```
java -jar stomp-client.jar -url '<Stomp single connection url>' -user $user -password $password -mode receiver -type topic -destination workshop.topicA
```

You should see a log output like the following one:

```
Successfully connected to stomp+ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61614
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```


3\. Type  

```
CTRL + b [arrow key down]
CTRL + b [arrow key left]
```

to choose the bottom left window. Run the following command to start a receiver using the **MQTT** protocol (first replace **<MQTT single connection url>** with your current broker value):

  * URL: This client doesn't support the failover connection url and expects the scheme to be **ssl** instead of **mqtt+ssl**. You have to provide the MQTT connection url for the active broker, like **ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:8883**.
  * Type: MQTT is build for publish-subscribe and therefore, it only supports topics in Amazon MQ and not queues.
  * Destination: In MQTT, it's common to use a '/' as a seperator, instead of a '.' to define your queue name. Amazon MQ transforms by default all '/' to '.' in your queue name.

```
java -jar mqtt-client.jar -url '<MQTT single connection url>' -user $user -password $password -mode receiver -destination workshop/topicA
```

You should see a log output like the following one:

```
Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:8883
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```


4\. Type  

```
CTRL + b [arrow key right]
```

to choose the bottom right window. Run the following command to start a receiver using the **AMQP** protocol (first replace **<AMQP failover connection url>** with your current broker value):

  * URL: This client does support the failover connection url, but not the scheme **amqp+ssl**. It expects the scheme in the form **amqps**. You have to provide the AMQP connection url like **failover:(amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671,amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:5671)**.

```
java -jar amqp-client.jar -url '<AMQP failover connection url>' -user $user -password $password -mode receiver -type topic -destination workshop.topicA
```

You should see a log output like the following one:

```
[AmqpProvider :(1):[amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671]] INFO org.apache.qpid.jms.sasl.SaslMechanismFinder - Best match for SASL auth was: SASL-PLAIN
[FailoverProvider: serialization thread] INFO org.apache.qpid.jms.JmsConnection - Connection ID:19a24b2a-7399-4538-a66d-436260b21c31:1 connected to remote Broker: amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```


5\. Feel free to try other combinations, using **AMQP**, **MQTT** or **Stomp** as sender protocol.


6\. Stop the sender and receiver by holding **CTRL + c** in each tmux screen. To terminate the active tmux screen, type **CTRL + d**.