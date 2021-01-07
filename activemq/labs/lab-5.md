# Lab 5: Set-Up Amazon CloudWatch to Monitor Our Broker

In this lab we will have a closer look at broker, queue and topic metrics provided via CloudWatch metrics. We also create a CloudWatch alarm which triggers an e-mail as soon as there are messages in the **ActiveMQ.DLQ** queue. The **ActiveMQ.DLQ** queue is a special queue used by Amazon MQ to store messages that failed to be processed multiple times (so called "poison messages").

### 1. Go to the Cloud9 IDE tab in the browser

Run the following command in one of the terminal windows to send a few message to a queue where no receiver is listening to:

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -mode sender -type queue -destination workshop.DLQTest -name Sender-1 -ttl 1000
```

> Note the `ttl` option. This means the message has a life time of only 1 second. All messages which are not consumed before the ttl expires are moved to the **ActiveMQ.DLQ** queue by default.

You should see a log output like the following:

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-1.mq.eu-central-1.amazonaws.com:61617
14.04.2018 11:33:03.609 - Sender: sent '[queue://workshop.DLQTest] [Sender-1] Message number 1'
14.04.2018 11:33:04.645 - Sender: sent '[queue://workshop.DLQTest] [Sender-1] Message number 2'
14.04.2018 11:33:05.680 - Sender: sent '[queue://workshop.DLQTest] [Sender-1] Message number 3'
...
```

### 2. Working with Amazon CloudWatch Metrics

While we are waiting for the above producer to generate a meaningful amount of data points, let's explore the metrics available in CloudWatch for the AmazonMQ service.

Navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch). Click on `Metrics` in the left navigation pane.


![Amazon MQ workshop lab 5 step 2](/images/cloud-watch-Step2.png)


AmazonMQ publishes metrics for the broker, such as Cpu Utilization, HeapUsage, NetworkOut. If you have an HA configuration with a primary and a secondary broker, you will have independent metrics for each instance.  
Click on the **AmazonMQ** namespace and on **Broker Metrics** afterwards.

> If you have multiple brokers running or already started a broker in the past, enter the name of your current broker in the search field and click enter, to filter the metrics for the workshop broker (primary and secondary).


![Amazon MQ workshop lab 5 step 3](/images/cloud-watch-Step3.png)


By selecting some of the metrics, e.g. `CpuUtilization`, you can plot the metric for a given time-frame. 

> Make sure you selected a relative time interval in Amazon CloudWatch, e.g. last 2 hours.

![Amazon MQ workshop lab 5 step 4](/images/cloud-watch-Step4.png)

AmazonMQ also publishes metrics for the Topics such as MemoryUsage, EnqueueCount (messages published by producers), DispatchCount (message delivered to consumers). 

Go back to the AmazonMQ namespace by clicking on **AmazonMQ**. Click on `AmazonMQ > Topic Metrics by Broker` to navigate to the topic metrics. In the filter put  the name of the topic you want to monitor, for example `topicA`.

![Amazon MQ workshop lab 5 step 5](/images/cloud-watch-Step5.png)


AmazonMQ also publishes metrics for the Queues. Go back to the AmazonMQ namespace by clicking on **AmazonMQ**. Click on `AmazonMQ > Queue Metrics by Broker` to navigate to the queue metrics. You can use the filter to narrow the list of queues that are listed to select the one of interest, for example `queueA`.

![Amazon MQ workshop lab 5 step 6](/images/cloud-watch-Step6.png)

### 3. Monitoring of an active queue

By now the producer that we started at the beginning should have generated enough data. Stop the producer by holding `CTRL + C` or or  `CONTROL + C` in each terminal window.  
To inspect the metric, select the checkbox for the queue `ActiveMQ.DLQ` and the metric name `QueueSize` for the broker(s). Then click the tab **Graphed metrics**.

![Amazon MQ workshop lab 5 step 7](/images/cloud-watch-Step7.png)


### 4. Working with Amazon CloudWatch Alarms


Click on the bell image for the first broker to create a new CloudWatch Alarm. Enter the following values:

* Name: `Failed message delivery from broker workshop-1`
* Description: `Failed message delivery from broker workshop-1`
* Whenever: `<see screenshot>`
* Treat missing data as: `good`


![Amazon MQ workshop lab 5 step 8](/images/cloud-watch-Step8.png)


Continue with the configuration and the following values:

* Whenever this alarm: `State is ALARM`
* Send notification to: Click **New List** and then enter `notifyMe` as the value for 'Enter a topic name...'
* Email list: `<your e-mail address>`


![Amazon MQ workshop lab 5 step 9](/images/cloud-watch-Step9.png)


Then click **Create Alarm** to create the alarm. 

If you are asked to **Confirm new email addresses**, click on **I will do it later** and navigate to your e-mail client.

![Amazon MQ workshop lab 5 step 10](/images/cloud-watch-Step10.png)

After you have confirmed your e-mail subscription, wait a few seconds and you should receive a mail, triggered by CloudWatch Alarm.

To learn more about metrics, please visit [Amazon CloudWatch Monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/mq-metricscollected.html).

# Completion

Congratulations, you've successfully completed Lab 5! You can move on to [Lab 6: Tighten up Security with Access Control](/labs/lab-6.md)

[Return to the Workshop Landing page](/README.md)