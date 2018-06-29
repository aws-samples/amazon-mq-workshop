# Lab 3: Using Publish-Subscribe messaging

In this exercise you will learn how to achieve Publish-Subscribe messaging with Amazon MQ using topics. The behavior of a message topic is that a sender publishes a message into the topic that will be received by all subscribers of that topic, so that there is 1:n relationship between sender and receivers for each considered message.  
You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).

1\. Navigate to the Amazon MQ Brokers page.
<details><summary>Screenshot step 1</summary><p>

![Amazon MQ workshop lab 3 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>


2\. Click on the name of the broker, you created in lab 1 and scroll a bit down to the **Connections** section. Copy the **OpenWire** fail-over connection url, by clicking on the **Copy failover string (Java)** link on the right site.
<details><summary>Screenshot step 2</summary><p>

![Amazon MQ workshop lab 3 step 2](/images/publish-subscribe-Step2.png)

</p></details><p/>


3\. Open a new SSH session to your EC2 instance and start a new **tmux** session by running: 

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

<details><summary>Screenshot step 3</summary><p>

![Amazon MQ workshop lab 3 step 3](/images/tmux-session.png)

</p></details><p/>


4\. Run the following command in your tmux terminal session, to start the sender:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type topic -destination demo.topicA -name Sender-1
```

You should see a log output like the following one:

```
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[topic://workshop.topicA] [Sender-1] Message number 3'
...
```


5\. In your tmux terminal session, run

```
CTRL + b [arrow key right]
```

to switch to the top right screen. Repeat step 4\. to start a second sender, so that 2 clients sending messages the same **topic**. Use a different **name** to distinguish between both.


6\. Run 

```
CTRL + b [arrow key down]
CTRL + b [arrow key left]
```

in your tmux session to select the bottom left one as active screen and run the following command to start the first receiver:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type topic -destination demo.topicA
```

You should see a log output like the following one:

```
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:01:03.672 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 1'
12.04.2018 12:01:03.772 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 2'
12.04.2018 12:01:03.673 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 3'
...
```


7\. Repeat step number 6\. to start a second receiver, so that 2 clients listening on the same **topic**.

You will see that multiple sender can send messages to the same topic, and multiple receiver can receiving messages from the same topic. You will also observe, that each message is **delivered to all receivers**, not only one.
<details><summary>Screenshot step 7</summary><p>

![Amazon MQ workshop lab 3 step 7](/images/publish-subscribe-Step7.png)

</p></details><p/>


7\. Stop the sender and receiver by holding **CTRL + c** in each tmux screen. To terminate the active tmux screen, type **CTRL + d**.