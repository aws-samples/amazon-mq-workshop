# Lab 4: Watch the Broker Statistics

In this lab, we will have a look at the statistics, Apache Active MQ is providing us through their web console.

### Prerequisites
You need to have done [Lab 2](/labs/lab-2.md) and [Lab 3](/labs/lab-3.md) to get statistics.  

### 1. Navigate to the Amazon MQ Brokers page.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>


### 2. Get ActiveMQ Web console address

Click on the name of the broker, you created in [Lab 1](/labs/lab-1.md) and scroll a bit down to the **Connections** section. Here you will find the links to the **ActiveMQ Web Console**. Only the link to the primary broker will be available. Try out which link is working at this time.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 2](/images/broker-statistics-Step2.png)

</p></details><p/>


### 3. Log into the ActiveMQ Web console

On the next page, click on **Manage ActiveMQ broker** and provide your credentials. After a successfull login, you will be forwarded to the overview page. Here you can find e.g. the information about the brokers up-time or used memory:

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 3](/images/broker-statistics-Step3.png)

</p></details><p/>

### 4. Managing Queues

Click on the **Queues** link in the top navigation bar to get some detailed information about the existing queues and the main information like number of active consumers, number of pending messages, messages enqueued and messages dequeued. This page provides you also the function to `Purge` the entire queue, to `Delete` a queue or to `Send` a message to this queue.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 4](/images/broker-statistics-Step4.png)

</p></details><p/>


Click on one of the queues, e.g. `queue.user1` to browse the queue content. Choose a queue which has some pending messages. On this page you can also `Delete` individual message, if you have to.

If you don't have a queue with pending messages, just start a sender and send some messages into a queue, as you have done in [Lab 2](/labs/lab-2.md).

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 5](/images/broker-statistics-Step5.png)

</p></details><p/>

By clicking on one of the messages, you can see the details of this message, including the timestamp when the message was sent, the unique message id and the content of this message. From this page, you can also **Delete** this message or **Copy/Move** it into another queue.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 6](/images/broker-statistics-Step6.png)

</p></details><p/>

### 4. Managing Topics

Click on the **Topics** link in the top navigation bar to get some detailed information about the existing topics and the main information like number of active consumers, messages enqueued and messages dequeued. This page provides you also the function to `Delete` a topic or to `Send` a message to this topic.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 7](/images/broker-statistics-Step7.png)

</p></details><p/>

You may wondering about the different `ActiveMQ.Advisory.\` topics. Apache Active MQ publishes different kind of events to the different topics which gives you the ability to react to these events. An example message from the `ActiveMQ.Advisory.Producer.Topic.workshop.topicA` topic could look like this one:

```
{
  commandId = 0,
  responseRequired = false,
  messageId = ID:ip-10-0-1-207-33499-1523623744067-1:1:0:0:149,
  originalDestination = null,
  originalTransactionId = null,
  producerId = ID:ip-10-0-1-207-33499-1523623744067-1:1:0:0,
  destination = topic://ActiveMQ.Advisory.Producer.Topic.workshop.topicA,
  transactionId = null,
  expiration = 0,
  timestamp = 0,
  arrival = 0,
  brokerInTime = 1523703346934,
  brokerOutTime = 1523703346935,
  correlationId = null,
  replyTo = null,
  persistent = false,
  type = Advisory,
  priority = 0,
  groupID = null,
  groupSequence = 0,
  targetConsumerId = null,
  compressed = false,
  userID = null,
  content = null,
  marshalledProperties = org.apache.activemq.util.ByteSequence@1dfc39d,
  dataStructure = ProducerInfo {
    commandId = 4,
    responseRequired = true,
    producerId = ID:c4b301d0e35d-62410-1523703346186-1:1:1:1,
    destination = topic://workshop.topicA,
    brokerPath = null,
    dispatchAsync = false,
    windowSize = 0,
    sentCount = 0
  },
  redeliveryCounter = 0,
  size = 0,
  properties = {
    producerCount=1,
    originBrokerName=workshop,
    originBrokerURL=ssl://ip-10-0-1-207:61617,
    originBrokerId=b-4e4bfd69-7b83-4a27-9faf-4684cfa80443
  },
  readOnlyProperties = true,
  readOnlyBody = true,
  droppable = false,
  jmsXGroupFirstForConsumer = false
}
```

By browsing to the **Subscribers**, **Connections** and **Network** links in the top navigation bar, you can get some more detailed information about these.

By clicking on the `Send` link in the top navigation bar, you can easily send a message to a queue or topic of your choice.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 4 step 10](/images/broker-statistics-Step10.png)

</p></details><p/>

# Completion

Congratulations, you've successfully completed Lab 4! You can move on to [Lab 5: Set-Up Amazon Cloudwatch to Monitor Our Broker](/labs/lab-5.md)

[Return the the Workshop Landing page](/README.md)