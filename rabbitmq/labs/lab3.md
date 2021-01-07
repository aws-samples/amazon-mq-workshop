# AmazonMQ - Rabbit MQ workshop Lab-3

In this lab, we will explore some of the cloudwatch metrics that Amazon MQ exposes for RabbitMQ.

## 
1. Go to one of the terminal windows and change the directory to lab-3. Run the following command in one of the terminal windows to send a few message to a queue.
```bash
python direct-sender.py -H <<host>> -P <<Port>> -u <<user>> -p <<password>> -e direct-demo-exchange -r demo-routing-key
```
While we are waiting for the above producer to generate a meaningful amount of data points, let’s explore the metrics available in CloudWatch for the AmazonMQ service.

2. Navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch). Click on Metrics in the left navigation pane.
![Cloudwatch Console](images/cloudwatch-1.png)
2. Click on AmazonMQ. It should have the option to explore queue metrics based on VHost, broker metrics or a node metrics.
3. Lets explore a few of the metrics for each of the categories. Under queue metrics, for each queue you should see metrics for message count, messageunacknowledged count, consumer count and message ready count. More details on each of the metrics can be found in the Amazon MQ developer [guide](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring-cloudwatch.html#rabbitmq-logging-monitoring).By selecting some of the metrics, e.g. MessageCount, you can plot the metric for a given time-frame.Make sure you selected a relative time interval in Amazon CloudWatch, e.g. last 2 hours.
![Cloudwatch graph](images/cloudwatch-2.png)

4. Lets explore some of the broker metrics. Under broker metrics, lets select PublishRate. You will be able to see the publish rate of the messages.

5. We will now see the metrics for the three individual metrics. Select Node Metrics by Broker. You will see several metrics listed for each of the nodes. Lets see the SystemCpuUtilization metric for one of the nodes. The graph should now show all the threee metrics that we have selected.

6. By now the sender that we started at the beginning should have generated enough data. Stop the producer by holding CTRL + C or CONTROL + C in each terminal window.In the next step, you will learn how to create a CloudWatch Alarm. Click on the bell image (as shown in the below picture with a red doodle) for the metric to create a new CloudWatch Alarm. Continue to next step to learn how to add an alarm.
![Alarm](images/alarm-4.png)
7. Enter the following values in Alarm Details, as shown in the first picture: 
![Alarm](images/alarm-1.png)

Name: Slow consumer alarm
Description: Trigger an alarm if the queue depth goes beyond the threshoold. 
![Alarm](images/alarm-2.png)
![Alarm](images/alarm-3.png)


We have now completed the lab for Cloudwatch monitoring. We can now move to performance benchmark.
