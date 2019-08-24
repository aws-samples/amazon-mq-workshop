# Lab 10: Performance testing

In this exercise you will learn how to do Performance Testing using ActiveMQ Mavem Plug-in. This tool was written and maintained by Apache ActiveMQ team. This is one of the many tools available for performance testing. 

At the end of this lab, in the **References** section, you can see a list of additional tools that you can use to do Performance Testing with AmazonMQ.

As you have learnt in the previous labs, AmazonMQ supports a variety of features. Point-To-Point queues, Publish/Subscribe topics, Network of Brokers. In addition it also supports Transacted sessions, Message Groups, Prefetch buffers, to name a few. One of the most important tuning parameters in AmazonMQ is ```concurrentStoreAndDispatchQueues``` queues and ```concurrentStoreAndDispatchTopics``` for topics.

## Concurrent Store and Dispatch

Concurrent store and dispatch is a strategy that facilitates high rates of message throughput provided the consumers are able to keep up with the flow of messages from the broker. 

When a producer is sending messages to broker and if the consumers can also consume messages at the same or higher rate (a.k.a **fast consumer**), then setting the ```concurrentStoreAndDispatchQueues``` (or ```concurrentStoreAndDispatchTopics```) to **true**  (default) will increase throughput (compared to having this set to **false**). When this setting is set to **true**, Broker sends messages directly from producer to consumer, once consumer acknowledges message receipt, Broker commits the messages to disk.

However when producers are sending messages at a higher rate than consumers, then this flag should be set to **false**. In this case, Broker secures the message to disk first and when the consumer is ready, it delivers the message. Since there is a disk i/o occurring before message delivery, this option incurs a performance penalty.

## 1. Prerequisites

In Lab 2, you should have run the ```setup.sh``` this script installs Amazon Corretto JDK 8 and Maven build tool. If you haven't run the Lab 2, then you should run the setup script in order to do this Lab.

## 2. Open MQClient Cloud9 IDE

In the Cloud9 workspace, open a terminal, type ```cd ~/activemq-perftest```

In this folder you should see ```src``` folder, ```pom.xml``` and ```readme.html```. The ```readme.html``` file is the manual that contains all the options and commands for running the performance test. 

The ```pom.xml``` file is the build script. The ```src/main/resources``` folder contains various test configuration files.

Each properties file sets up different test case and you can keep these files to compare and contrast different features or for tuning the AmazonMQ environment to find an optimal configuration for your application.

For this lab, we prepared two test configuration files ```openwire-producer.properties``` and ```openwire-consumer.properties```. Both fiels can be found under ```~/environment/amazon-mq-workshop``` folder.

Copy these two files from using the following command

```
cp ~/environment/amazon-mq-workshop/openwire-producer.properties ~/environment/activemq-perftest
cp ~/environment/amazon-mq-workshop/openwire-consumer.properties ~/environment/activemq-perftest
```

Now we are all set to run the performance test and view the results. Since the default configuration for Broker sets ```concurrentStoreAndDispatchQueues``` to **true**, we will start the consumers first and then the producers to see full impact of this setting.

```
cd ~/environment/activemq-perftest
```
You can run each test case by running the following command one each for producer and consumer. Open two terminal windows, run the first command in one terminal and the second commond in a different terminal.

```
mvn activemq-perf:consumer -DsysTest.propsConfigFile=openwire-consumer.properties 
mvn activemq-perf:producer -DsysTest.propsConfigFile=openwire-producer.properties 
```
Once each of the above tests complete, they provide a summary of the tests in stdout as shown below.

```System Average Throughtput``` and ```System Total Clients``` are the most useful metrics.

```
#########################################
####    SYSTEM THROUGHPUT SUMMARY    ####
#########################################
System Total Throughput: 19116
System Total Clients: 1
System Average Throughput: 63.72
System Average Throughput Excluding Min/Max: 63.38
System Average Client Throughput: 63.72
System Average Client Throughput Excluding Min/Max: 63.38
Min Client Throughput Per Sample: clientName=JmsProducer12340, value=26
Max Client Throughput Per Sample: clientName=JmsProducer12340, value=76
Min Client Total Throughput: clientName=JmsProducer12340, value=19116
Max Client Total Throughput: clientName=JmsProducer12340, value=19116
Min Average Client Throughput: clientName=JmsProducer12340, value=63.72
Max Average Client Throughput: clientName=JmsProducer12340, value=63.72
Min Average Client Throughput Excluding Min/Max: clientName=JmsProducer12340, value=63.38
Max Average Client Throughput Excluding Min/Max: clientName=JmsProducer12340, value=63.38
```

From this test, the average throughput for a producer is around 64 messages per sec for 1 client. Keep in mind that the broker instance is a t2.micro. Don't pay attention to the numbers.

In the ```reports``` directory you should see an xml file with more detailed throughput metrics. In the ```JmsProducer1234_numClients1_numDests1_all.xml``` file for example, ```jmsClientSettings``` and ```jmsFactorySettings``` captures different broker switches.

Each of the report files captures exact test and broker environment. Keeping these files around will help you to compare performance between different test cases and how a set of settings have impacted performance.

The previous test showcases a normal scenarios where producers and consumers are running at the same time at least both at the same rates.

Now let's see what happens if you run only the producer without a consumer running.

```
mvn activemq-perf:producer -DsysTest.propsConfigFile=openwire-producer.properties 
```


### 3. Resources

  - https://activemq.apache.org/activemq-performance-module-users-manual

