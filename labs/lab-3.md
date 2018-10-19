# Lab 3: Using Publish-Subscribe Messaging Using Topics

In this exercise you will learn how to do Publish-Subscribe messaging with Amazon MQ using topics. The behavior of a message topic is that a message published onto the topic will be received by all subscribers of that topic, so that there is 1:n relationship between sender and receivers for each published message.  

You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).

### 1. Navigate to the Amazon MQ Brokers page.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 3 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>

### 2. Copy the Connection String

Click on the name of the broker you created in [Lab 1](/labs/lab-1.md) and scroll a bit down to the **Connections** section. Copy the `OpenWire` fail-over connection url, by clicking on the `Copy failover string (Java)` link on the right side.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 3 step 2](/images/publish-subscribe-Step2.png)

</p></details><p/>

### 3. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals shoul be in the `/workspace` directory.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>


Select the top-left terminal and run the following command to start the sender:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type topic -destination demo.topicA -name Sender-1
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 3'
...
```

Select the-top right terminal. Repeat the last command to start a second sender, so that there are 2 clients sending messages the same **topic**. Use a different **name** to distinguish the senders in the logs.

Run `CTRL + b [arrow key down]`, `CTRL + b [arrow key left]` in your tmux session to select the bottom left one as active screen and run the following command to start the first receiver:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type topic -destination demo.topicA
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:01:03.672 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 1'
12.04.2018 12:01:03.772 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 2'
12.04.2018 12:01:03.673 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 3'
...
```

Repeat the last command in another terminal to start a second receiver, so that there are 2 clients listening on the same **topic**.

You see that multiple senders can send messages to the same topic and multiple receivers can receive messages from the same topic. You also observe that each message is **delivered to all receivers**.


Stop the sender and receiver by holding `CTRL + c` in each terminal.

# Completion

Congratulations, you've successfully completed Lab 3! You can move on to [Lab 4: Active MQ Broker Statistics](/labs/lab-4.md)

[Return the the Workshop Landing page](/README.md)