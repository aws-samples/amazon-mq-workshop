# Lab 5: Set-Up Amazon CloudWatch to Monitor Our Broker

In this lab we will have a closer look at broker, queue and topic metrics provided via CloudWatch metrics. We also create a CloudWatch alarm which triggers an e-mail as soon as there are messages in the **ActiveMQ.DLQ** queue. The **ActiveMQ.DLQ** queue is a special queue used by Amazon MQ to store messages that failed to be processed multiple times (so called "poison messages").

### 1. Open an SSH session to your EC2 instance 

Run the following command from the ec2-user home directory to send a few message to a queue where no receiver is listening to:

``` bash
java -jar amazon-mq-client.jar -url $url -user $user -password $password -mode sender -type queue -destination workshop.DLQTest -name Sender-1 -ttl 1000
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

Navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch). Click on `Metrics` in the left navigation pane.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 2](/images/cloud-watch-Step2.png)

</p></details><p/>

Click on the **AmazonMQ** namespace and on **Broker Metrics** afterwards.

> If you have multiple brokers running or already started a broker in the past, enter the name of your current broker in the search field and click enter, to filter the metrics for the workshop broker (primary and secondary).

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 3](/images/cloud-watch-Step3.png)

</p></details><p/>

By selecting some of the metrics, e.g. `CpuUtilization`, you can plot the metric for a given time-frame. 
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 4](/images/cloud-watch-Step4.png)

</p></details><p/>

Go back to the AmazonMQ namespace by clicking on **AmazonMQ**. Click on `AmazonMQ > Topic Metrics by Broker` to navigate to the topic metrics.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 5](/images/cloud-watch-Step5.png)

</p></details><p/>

Go back to the AmazonMQ namespace by clicking on **AmazonMQ**. Click on `AmazonMQ > Queue Metrics by Broker` to navigate to the queue metrics.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 6](/images/cloud-watch-Step6.png)

</p></details><p/>

Select the checkbox for the queue `ActiveMQ.DLQ` and the metric name `QueueSize` for both brokers. Then click the tab **Graphed metrics**.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 7](/images/cloud-watch-Step7.png)

</p></details><p/>

### 3. Working with Amazon CloudWatch Alarms

Click on the bell image for the first broker to create a new CloudWatch Alarm. Enter the following values:

* Name: `Failed message delivery from broker workshop-1`
* Description: `Failed message delivery from broker workshop-1`
* Whenever: `<see screenshot>`
* Treat missing data as: `good`

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 8](/images/cloud-watch-Step8.png)

</p></details><p/>

Continue with the configuration and the following values:

* Whenever this alarm: `State is ALARM`
* Send notification to: `<provide a name for a SNS topic>`
* Email list: `<your e-mail address>`

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 9](/images/cloud-watch-Step9.png)

</p></details><p/>


After you have confirmed your e-mail subscription...

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 5 step 10](/images/cloud-watch-Step10.png)

</p></details><p/>

Stop the sender and receiver by holding `CTRL + c` in each SSH session.

Wait a few seconds and you should receive a mail, triggered by CloudWatch Alarm.

To learn more about metrics, please visit [Amazon CloudWatch Monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/mq-metricscollected.html).

# Completion

Congratulations, you've successfully completed Lab 5! You can move on to [Lab 6: Tighten up Security with Access Control](/labs/lab-6.md)

[Return the the Workshop Landing page](/README.md)