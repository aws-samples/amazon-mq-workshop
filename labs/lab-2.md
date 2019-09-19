# Lab 2: Using Point-To-Point Messaging Using Queues

In this exercise you learn how to do Point-To-Point messaging with Amazon MQ using queues. The behavior of a message queue is that each message is consumed by one receiver, so that there is a 1:1 relationship between sender and receiver for each published message.

You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).

### :white_check_mark: 1. Prerequisites

You should have an Amazon MQ broker running and have configured the necessary environment variable as per the guide below.

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
echo "url=\"$temp_url\"" >> ~/.bashrc 
./setup.sh
source ~/.bashrc
```

:white_check_mark: **NOTE**: Ensure that all terminals windows that you will use for the workshop are created after having run this step.

</p></details><p/>

### 2. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals should be in the `/environment/amazon-mq-workshop` directory.

**NOTE**: In order to split the windows into a chequered pattern, on the 2nd and 4th terminal windows, right click and select "Split Pane in Two Columns" and navigate to the projects root directory by running 'cd amazon-mq-workshop' 

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>

Run the following command in the top-left terminal to start the sender. The sender name is added to the message to identify who is sending the message:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode sender -type queue -destination workshop.queueA -name Sender-1
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:33:03.609 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 1'
14.04.2018 11:33:04.645 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 2'
14.04.2018 11:33:05.680 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Select the top-right terminal and start a second sender. Now you have 2 clients sending messages to the same **queue**. Use a different name on order to distinguish the sender of the messages:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode sender -type queue -destination workshop.queueA -name Sender-2
```

Select the lower-left terminal. Run the following command, to start the first receiver:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode receiver -type queue -destination workshop.queueA
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

Select the lower-right terminal and start a second receiver. You now have 2 clients listening on the same **queue**:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode receiver -type queue -destination workshop.queueA
```

You can see that multiple senders can send messages to the same queue, and multiple receivers can receive messages from the same queue. But you will also observe that each message is only **delivered to one receiver**, not both. You will also observe that there is no direct relationship between sender and receiver. Try to stop/start the receiver to see what changes.

### 3. Clean-up

Stop the sender and receiver by holding `CTRL + C` or  `CONTROL + C` in each terminal window. 

# Completion

Congratulations, you've successfully completed Lab 2! You can move on to [Lab 3: Using Publish-Subscribe Messaging Using Topics](/labs/lab-3.md)

[Return to the Workshop Landing page](/README.md)