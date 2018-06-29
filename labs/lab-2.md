# Lab 2: Using Point-To-Point messaging

In this exercise you will learn how to achieve Point-To-Point messaging with Amazon MQ using queues. The behavior of a message queue is that each message is consumed by one receiver, so that there is a 1:1 relationship between sender and receiver for each considered message.  
You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).


1\. Navigate to the Amazon MQ Brokers page.
<details><summary>Screenshot step 1</summary><p>

![Amazon MQ workshop lab 2 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>


2\. Click on the name of the broker, you created in lab 1 and scroll a bit down to the **Connections** section. Copy the **OpenWire** fail-over connection url, by clicking on the **Copy failover string (Java)** link on the right site.
<details><summary>Screenshot step 2</summary><p>

![Amazon MQ workshop lab 2 step 2](/images/point-to-point-Step2.png)

</p></details><p/>


3\. Open an SSH session to your EC2 instance. Start a new **tmux** session (we are using tmux to be able to divide our terminal screen into multiple windows. You can learn more about tmux [here](https://github.com/tmux/tmux/wiki)):

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

![Amazon MQ workshop lab 2 step 3](/images/tmux-session.png)

</p></details><p/>


4\. Run the following command from the ec2-user home directory, to start the sender. The sender name will be added to the message and identify, who was sending the message:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-1
```

You should see a log output like the following one:

```
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:33:03.609 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 1'
14.04.2018 11:33:04.645 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 2'
14.04.2018 11:33:05.680 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```


5\. Type  

```
CTRL + b [arrow key right]
```

to choose the top right window. Start a second sender, so that 2 clients sending messages the same **queue**. You can distinguish between both by the different name they are using in the messages, they are sending:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-2
```

6\. Type

```
CTRL + b [arrow key down]
CTRL + b [arrow key left]
```

to switch to the lower left window and run the following command, to start the first receiver:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You should see a log output like the following one:

```
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:47:41.616 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 1'
14.04.2018 11:47:41.620 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 2'
...
14.04.2018 11:47:41.622 - Receiver: received '[queue://workshop.queueA] [Sender-2] Message number 1'
14.04.2018 11:47:41.623 - Receiver: received '[queue://workshop.queueA] [Sender-2] Message number 2'
...
```


7\. Type

```
CTRL + b [arrow key right]
```

to switch to the lower right window and start a second receiver, so that 2 clients listening on the same **queue**:

```
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You will see that multiple sender can send messages to the same queue, and multiple receiver can receiving messages from the same queue. But you will also observe, that each message is only **delivered to one receiver**, not both/all. You also see, there is no direct relationship between sender and receiver (stop/start the receiver to see how it will change).
<details><summary>Screenshot step 7</summary><p>

![Amazon MQ workshop lab 2 step 7](/images/point-to-point-Step7.png)

</p></details><p/>


8\. Stop the sender and receiver by holding **CTRL + c** in each tmux screen. To terminate the active tmux screen, type **CTRL + d**.