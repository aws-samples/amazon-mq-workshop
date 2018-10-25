# Lab 4: Testing a Broker Fail-over

In this lab you will have a running sender and receiver producing and consuming messages while you issue a Broker reboot. You will see how long the clients are not able to send and receive messages before they successfully reconnect to the broker.

### 1. Prerequisites

You should have an AmazonMQ broker running and have configured the necessary environment variable as per the guide below.

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

In the main pane, close the Welcome screen and add 2  terminal tabs (click on + tab and select New Terminal. Reorganize them to have them one on top of the other or side by side.
All terminals should be in the `/workspace` directory.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 2 step 3](/images/c9-window.png)

</p></details><p/>

Run the following command in one of the terminals to start the sender:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-1
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Select the other terminal and run the following command to start the receiver:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:01:03.672 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 1'
12.04.2018 12:01:03.772 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 2'
12.04.2018 12:01:03.673 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Scroll to the top of your brokers details page and click on `Actions -> Reboot broker`.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 4 step 5](/images/fail-over-Step5.png)

</p></details><p/>

Shortly after, you should see an exception in both consoles because the primary broker isn't reachable any 	more. 

```bash
[ActiveMQ Transport: ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com/52.28.200.138:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
	at java.io.DataInputStream.readInt(DataInputStream.java:392)
	at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
	at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
	at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
	at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
	at java.lang.Thread.run(Thread.java:748)
```


After waiting a few more seconds, you should see a successful reconnect from your clients to the secondary broker, which is now the new primary one (compare the connection urls):

```bash 
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
```

The sender terminal log output should look similar to this one:

``` bash
12.04.2018 12:02:59.869 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4668'
12.04.2018 12:02:59.895 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4669'
12.04.2018 12:02:59.919 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4670'
[ActiveMQ Transport: ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com/52.28.200.138:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
	at java.io.DataInputStream.readInt(DataInputStream.java:392)
	at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
	at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
	at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
	at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
	at java.lang.Thread.run(Thread.java:748)
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:03:11.534 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4671'
12.04.2018 12:03:11.670 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4672'
12.04.2018 12:03:11.783 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 4673'
```

The receiver terminal log output should look similar to this one:

``` bash
12.04.2018 12:02:59.876 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4668'
12.04.2018 12:02:59.902 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4669'
12.04.2018 12:02:59.926 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4670'
[ActiveMQ Transport: ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com/52.28.200.138:61617] WARN org.apache.activemq.transport.failover.FailoverTransport - Transport (ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617) failed , attempting to automatically reconnect: {}
java.io.EOFException
	at java.io.DataInputStream.readInt(DataInputStream.java:392)
	at org.apache.activemq.openwire.OpenWireFormat.unmarshal(OpenWireFormat.java:268)
	at org.apache.activemq.transport.tcp.TcpTransport.readCommand(TcpTransport.java:240)
	at org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:232)
	at org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
	at java.lang.Thread.run(Thread.java:748)
[ActiveMQ Task-3] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully reconnected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:03:11.541 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4671'
12.04.2018 12:03:11.677 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4672'
12.04.2018 12:03:11.790 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 4673'
```


### 3. Clean-up

Stop the sender and receiver by holding `CTRL + C` or `CONTROL + C` in each terminal.

# Completion

Congratulations, you've successfully completed Lab 4! You can move on to [Lab 5: Set-Up Amazon CloudWatch to Monitor Our Broker](/labs/lab-5.md)

[Return the the Workshop Landing page](/README.md)