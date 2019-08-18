# Lab 8: Protocol Interoperability

In this exercise, you connect one message producer to the broker and start sending messages. You then connect a message consumer to the broker using a different protocol. You repeat these steps with multiple protocol combinations to figure out which protocol conversions are supported by Amazon MQ.


### 1. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals should be in the `/workspace` directory.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>

In the `/workspace` directory you find the following JARs:
* amazon-mq-client.jar (using the OpenWire protocol) - [Source](https://github.com/aws-samples/amazon-mq-workshop/blob/master/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java)
* amqp-client.jar (using the AMQP protocol) - [Source](https://github.com/aws-samples/amazon-mq-workshop/blob/master/amqp-client/src/main/java/com/aws/sample/amazonmq/AMQPClient.java)
* mqtt-client.jar (using the MQTT protocol) - [Source](https://github.com/aws-samples/amazon-mq-workshop/blob/master/mqtt-client/src/main/java/com/aws/sample/amazonmq/MQTTClient.java)
* stomp-client.jar (using the Stomp protocol) - [Source](https://github.com/aws-samples/amazon-mq-workshop/blob/master/stomp-client/src/main/java/com/aws/sample/amazonmq/StompClient.java)

Run the following command to start a sender using the `OpenWire` protocol in the top-left terminal:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode sender -type topic -destination workshop.topicA -name OpenWire
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```

** Please note the broker host to which the client successfully connected.  This is the active broker used in following steps.**


Select the upper-right terminal. Run the following command to start a receiver using the `Stomp` protocol (first replace `<Stomp single connection url>` with your current broker value. You find this value on the details page of your Amazon MQ broker in the **Connections** section.):

**NOTES for STOMP client**
* This client doesn't support the failover connection url. You have to provide the Stomp connection url for the active broker, like `stomp+ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61614`.

``` bash
java -jar ./bin/stomp-client.jar -url '<Stomp single connection url>' -mode receiver -type topic -destination workshop.topicA
```

You should see a log output like the following:

``` bash
Successfully connected to stomp+ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61614
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```

Select the bottom-left terminal. Run the following command to start a receiver using the **MQTT** protocol (first replace `<MQTT single connection url>` with your current broker value):

**NOTES for MQTT**:
  * URL: This client doesn't support the failover connection url and expects the scheme to be **ssl** instead of **mqtt+ssl**. You have to provide the MQTT connection url for the active broker, like **ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:8883**.
  * Type: MQTT is built for publish-subscribe and therefore, it only supports topics in Amazon MQ and not queues.
  * Destination: In MQTT, it's common to use a '/' as a seperator, instead of a '.' to define your queue name. Amazon MQ transforms by default all '/' to '.' in your queue name.

``` bash
java -jar ./bin/mqtt-client.jar -url '<MQTT single connection url>' -mode receiver -destination workshop/topicA
```

You should see a log output like the following:

``` bash
Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:8883
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```

Select the bottom-right terminal. Run the following command to start a receiver using the **AMQP** protocol (first replace **<AMQP failover connection url>** with your current broker value):

**NOTE for AMQP client**
* Schema: This client supports the failover connection url, but not the scheme `amqp+ssl`. It expects the scheme in the form `amqps`. You have to provide the AMQP connection url like `failover:(amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671,amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:5671)`.

``` bash
java -jar ./bin/amqp-client.jar -url '<AMQP failover connection url>' -mode receiver -type topic -destination workshop.topicA
```

You should see a log output like the following:

``` bash
[AmqpProvider :(1):[amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671]] INFO org.apache.qpid.jms.sasl.SaslMechanismFinder - Best match for SASL auth was: SASL-PLAIN
[FailoverProvider: serialization thread] INFO org.apache.qpid.jms.JmsConnection - Connection ID:19a24b2a-7399-4538-a66d-436260b21c31:1 connected to remote Broker: amqps://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:5671
12.04.2018 12:00:58.369 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 1'
12.04.2018 12:00:58.395 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 2'
12.04.2018 12:00:58.419 - Receiver: received '[topic://workshop.topicA] [OpenWire] Message number 3'
...
```

Feel free to try other combinations, using **AMQP**, **MQTT** or **Stomp** as sender protocol.

Stop any running sender or receiver by holding `CTRL + C` or or  `CONTROL + C` in each terminal window.


# Completion

Congratulations, you've successfully completed Lab 8! This is the last lab in the workshop.
You can move on to [Workshop cleanup instructions](/labs/lab-cleanup.md)

[Return to the Workshop Landing page](/README.md)