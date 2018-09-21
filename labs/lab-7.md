# Lab 7: Testing a Broker Fail-over

In this lab you will have an running sender and receiver producing and consuming messages, when we will issue a Broker reboot. You will see how long the clients are not able to send and receive messages, until they could successfully reconnect to the broker.

### 1. Navigate to the Amazon MQ Brokers page

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 7 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>

### 2. Copy the Connection String

Click on the name of the broker, you created in lab 1 and scroll a bit down to the **Connections** section. Copy the **OpenWire** fail-over connection url, by clicking on the **Copy failover string (Java)** link on the right site.

<details><summary>Screenshot step 2</summary><p>

![Amazon MQ workshop lab 7 step 2](/images/fail-over-Step2.png)

</p></details><p/>

### 3. Open an SSH session to your EC2 instance

Open an SSH session to your EC2 instance and start a **tmux** session by running:

```
tmux
```

To split your terminal window into 2 individual screens, run the following commands:

```
CTRL + b "
CTRL + b [arrow key up]
```

Run the following command from the top screen, to start the sender:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.queueA -name Sender-1
```

You should see a log output like the following one:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:00:58.369 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 1'
12.04.2018 12:00:58.395 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 2'
12.04.2018 12:00:58.419 - Sender: sent '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Type `CTRL + b [arrow key down]` to switch to the bottom screen and run the following command, to start the receiver:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode receiver -type queue -destination workshop.queueA
```

You should see a log output like the following one:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
12.04.2018 12:01:03.672 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 1'
12.04.2018 12:01:03.772 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 2'
12.04.2018 12:01:03.673 - Receiver: received '[queue://workshop.queueA] [Sender-1] Message number 3'
...
```

Scroll to the top of your brokers details page and click on `Actions -> Reboot broker`.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 7 step 5](/images/fail-over-Step5.png)

</p></details><p/>


Shortly after, you should see an exception in both consoles, because the primary broker isn't reachable anymore. After waiting a few more seconds, you can see a successful reconnect from your clients to the secondary broker, which was becoming the new primary one (compare the connection urls):

The sender console log output should look similar to this one:

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

The receiver console log output should look similar to this one:

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

Stop the sender and receiver by holding `CTRL + c` in each tmux screen. To terminate the active tmux screen, type `CTRL + d`.

# Completion

Congratulations, you've successfully completed Lab 7! You can move on to [Lab 8: Protocol Interoperability](/labs/lab-8.md)

[Return the the Workshop Landing page](/README.md)