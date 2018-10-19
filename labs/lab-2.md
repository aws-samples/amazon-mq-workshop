# Lab 2: Using Point-To-Point Messaging Using Queues

In this exercise you learn how to do Point-To-Point messaging with Amazon MQ using queues. The behavior of a message queue is that each message is consumed by one receiver, so that there is a 1:1 relationship between sender and receiver for each published message.

You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).

### 1. Navigate to the Amazon MQ Brokers page

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>

### 2. Copy the Connection String

Click on the name of the broker you created in [Lab 1](/labs/lab-1.md) and scroll down to the **Connections** section. Copy the `OpenWire` fail-over connection url, by clicking on the `Copy failover string (Java)` link on the right side.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 2](/images/point-to-point-Step2.png)

</p></details><p/>

### 3. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals shoul be in the `/workspace` directory.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>

Run the following command start the sender. The sender name is added to the message to identify who is sending the message:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-1
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:33:03.609 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 1'
14.04.2018 11:33:04.645 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 2'
14.04.2018 11:33:05.680 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Select the top right window. 

Start a second sender. Now you have 2 clients sending messages to the same **queue**. Use a different name on order to distinguish the sender of the messages:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-2
```

Select the lower left window. Run the following command, to start the first receiver:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:47:41.616 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 1'
14.04.2018 11:47:41.620 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 2'
...
14.04.2018 11:47:41.622 - Receiver: received '[queue://workshop.queueA] [Sender-2] Message number 1'
14.04.2018 11:47:41.623 - Receiver: received '[queue://workshop.queueA] [Sender-2] Message number 2'
...
```

Select the lower right window and start a second receiver. You now have 2 clients listening on the same **queue**:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You can see that multiple senders can send messages to the same queue, and multiple receivers can receive messages from the same queue. But you will also observe that each message is only **delivered to one receiver**, not both. You also observer that there is no direct relationship between sender and receiver. Try to stop/start the receiver to see what changes.


Stop the sender and receiver by holding `CTRL + c` in each terminal window. 


# Completion

Congratulations, you've successfully completed Lab 2! You can move on to [Lab 3: Using Publish-Subscribe Messaging Using Topics](/labs/lab-3.md)

[Return the the Workshop Landing page](/README.md)