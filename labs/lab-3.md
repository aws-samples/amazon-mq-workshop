# Lab 3: Using Publish-Subscribe Messaging Using Topics

In this exercise you will learn how to do Publish-Subscribe messaging with Amazon MQ using topics. The behavior of a message topic is that a message published onto the topic will be received by all subscribers of that topic, so that there is 1:n relationship between sender and receivers for each published message.  

You will find the source code of this client [here](/amazon-mq-client/src/main/java/com/aws/sample/amazonmq/AmazonMqClient.java).

### 1. Prerequisites

You should have an Amazon MQ broker running and have configured the necessary environment variable as per the guide below.

<details><summary>Store environment variable</summary><p>

To make it easier to run the commands in the following labs we store frequently used parameters like Amazon MQ broker user, password, etc. in Bash environment variables.

Go to the [AmazonMQ console](https://console.aws.amazon.com/amazon-mq), and click on the name of the broker (the one with a name starting with the stack name you created)

Scroll down to the Connections section and click the **Copy failover string** link beside the OpenWire row 
to copy the string to your clipboard.

![Copy failover link](/images/fail-over-Step2.png)

Go to the [CloudFormation console](https://console.aws.amazon.com/cloudformation) and select the stack that you launched at the beginning of the workshop. In the Output tab shown in the lower part of the screen you will have a Cloud9ConsoleURL entry. Click on the URL and enter **aws** as username and **mq** as password. 
 Once the Cloud9 IDE has launched, select the terminal window at the bottom and enter the following commands, one at the time, replacing the values **<...>** with the value you have chosen during the creation of the stack.

``` bash
export temp_url="<failover url>"
echo "url=\"$temp_url\"" >> ~/.bashrc; source ~/.bashrc
```

**NOTE**: Ensure that all terminals windows that you will use for the workshop are crated after having run this step.

</p></details><p/>

### 2. Go to the Cloud9 IDE tab in the browser

In the main pane, close the Welcome screen and add 4  terminal tabs (click on + tab and select New Terminal. Reorganize them in a chequered pattern using the mouse and select the top left terminal.
All terminals should be in the `/workspace` directory.

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

Select the-top right terminal and run the following command to start a second sender. This is the same as the previous command with a diffent name to distinguish the senders. 

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type topic -destination demo.topicA -name Sender-2
```

Select the bottom-left terminal and run the following command to start a receiver. 

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type topic -destination demo.topicA
```

The receiver is starting receiving messages published on the topic by both senders and you should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:01:03.672 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 1'
12.04.2018 12:01:03.772 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 2'
12.04.2018 12:01:03.673 - Receiver: received '[topic://workshop.topicA] [Sender-1] Message number 3'
...
```

Repeat the last command in another terminal to start a second receiver, so that there are 2 clients listening on the same **topic**.

You see that multiple senders can send messages to the same topic and multiple receivers can receive messages from the same topic. You also observe that each message is **delivered to all receivers**.

### 3. Clean-up

Stop the sender and receiver by holding `CTRL + C` or `CONTROL + C` in each terminal.

# Completion

Congratulations, you've successfully completed Lab 3! You can move on to [Lab 4: Active MQ Broker Statistics](/labs/lab-4.md)

[Return the the Workshop Landing page](/README.md)