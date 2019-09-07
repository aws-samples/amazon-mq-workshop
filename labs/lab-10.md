# Lab 10: Performance testing

In this exercise you will learn how to do Performance Testing using ActiveMQ Maven Plug-in. This tool was written and maintained by Apache ActiveMQ team. This is one of the many tools available for performance testing. 

At the end of this lab, in the **References** section, you can see a list of additional tools that you can use to do Performance Testing with AmazonMQ.

As you have learnt in the previous labs, AmazonMQ supports a variety of features. Point-To-Point queues, Publish/Subscribe topics, Network of Brokers. In addition, it also supports Transacted sessions, Message Groups, Prefetch buffers, to name a few. One of the most important tuning parameters in AmazonMQ is ```concurrentStoreAndDispatchQueues``` queues and ```concurrentStoreAndDispatchTopics``` for topics.

## Concurrent Store and Dispatch

Concurrent store and dispatch is a strategy that facilitates high rates of message throughput provided the consumers are able to keep up with the flow of messages from the broker. 

When a producer is sending messages to broker and if the consumers can also consume messages at the same or higher rate (a.k.a **fast consumer**), then setting the ```concurrentStoreAndDispatchQueues``` (or ```concurrentStoreAndDispatchTopics```) to **true**  (default) will increase throughput (compared to having this set to **false**). When this setting is set to **true**, Broker sends messages directly from producer to consumer, once consumer acknowledges message receipt, Broker commits the messages to disk.

However, when producers are sending messages at a higher rate than consumers, then this flag should be set to **false**. In this case, Broker secures the message to disk first and when the consumer is ready, it delivers the message. Since there is a disk i/o occurring before message delivery, this option incurs a performance penalty.

## 1. Prerequisites

In Lab 9, you should have run the ```setup.sh``` this script installs Amazon Corretto JDK 8 and Maven build tool. If you haven't run the Lab 9, then you should run the setup script in order to do this Lab.

## 2. Open MQClient Cloud9 IDE

In the Cloud9 workspace, open a terminal, type ```cd ~/environment/activemq-perftest```

In this folder you should see ```src``` folder, ```pom.xml``` and ```readme.html```. The ```readme.html``` file is the manual that contains all the options and commands for running the performance test. 

The ```pom.xml``` file is the build script. The ```src/main/resources``` folder contains various test configuration files.

Each properties file sets up different test case and you can keep these files to compare and contrast different features or for tuning the AmazonMQ environment to find an optimal configuration for your application.

For this lab, we prepared two test configuration files ```openwire-producer.properties``` and ```openwire-consumer.properties```. Both files can be found under ```~/environment/amazon-mq-workshop``` folder.

Copy these two files from using the following command

```
cp ~/environment/amazon-mq-workshop/openwire-producer.properties ~/environment/activemq-perftest
cp ~/environment/amazon-mq-workshop/openwire-consumer.properties ~/environment/activemq-perftest
```

Now we are all set to run the performance test and view the results. Since the default configuration for Broker sets ```concurrentStoreAndDispatchQueues``` to **true**, we will start the consumers first and then the producers to see full impact of this setting.

```
cd ~/environment/activemq-perftest
```
You can run each test case by running the following command one each for producer and consumer. Open two terminal windows, run the first command (consumer) in one terminal and the second command (producer) in a different terminal.

```
mvn activemq-perf:consumer -DsysTest.propsConfigFile=openwire-consumer.properties 
mvn activemq-perf:producer -DsysTest.propsConfigFile=openwire-producer.properties 
```
Once each of the above tests complete, they provide a summary of the tests in stdout as shown below. Your results may vary. The following output is from a test we performed and shown below as a sample output.

```System Average Throughput``` and ```System Total Clients``` are the most useful metrics.

In the ```reports``` directory you should see an xml file with more detailed throughput metrics. In the ```JmsProducer1234_numClients1_numDests1_all.xml``` file for example, ```jmsClientSettings``` and ```jmsFactorySettings``` captures different broker switches.

Each of the report files captures exact test and broker environment. Keeping these files around will help you to compare performance between different test cases and how a set of settings have impacted performance.


```
#########################################
####    SYSTEM THROUGHPUT SUMMARY    ####
#########################################
System Total Clients: 5
System Average Throughput: 317.87
```

From this test, the average throughput for a producer is around 318 messages per sec for 5 clients. Keep in mind that the broker instance is a mq.m5.large. You can get higher throughput with more clients and a larger broker instance. This test demonstrates the concept of running **fast** consumers while producing messages.

Now let's see another test that demonstrates what happens if there is only a producer without a consumer. The performance degrades relatively in comparison with the previous test.

```
mvn activemq-perf:producer -DsysTest.propsConfigFile=openwire-producer.properties 
```

Once the above test finishes you should see the output something like below

```
#########################################
####    SYSTEM THROUGHPUT SUMMARY    ####
#########################################
System Total Clients: 5
System Average Throughput: 71.66
```

As you can see the average performance is **5 times** slower compared relatively to running consumers and producers at the same time in the earlier test.

Now let's see how the ```concurrentStoreAndDispatchQueues``` setting you learned earlier help in cases where producers are producing messages while consumers are unable to keep up (or not available)

Open AWS Console, go AmazonMQ Console, open the {StackName}-Broker details, open Configuration of the broker, click on **Edit Configuration** (right hand corner)

In the XML configuration, you should see a commented XML block as shown below. Remove ```<!--``` and ```-->``` to uncomment the setting.

```
  <!--
  <persistenceAdapter>
    <kahaDB  concurrentStoreAndDispatchQueues="false"/>
  </persistenceAdapter>
  -->
```

Save the configuration, small popup appears to ask for Description, give "Test concurrentStoreAndDispatchQueues" as description.

Now go back to AmazonMQ console, select the {StackName}-Broker, click on Edit. Once the Edit screen opens, go to Configuration block, click on "Revision 1" dropdown, select "Revision 2".

At the bottom of the page, you should see **Schedule modifications**, on the next screen, select **Immediately" (to apply the changes now) and click Apply.

Now broker applies your configuration changes and reboots broker. Wait for about 5 minutes for the broker to get to **Running** state,

Run the following test to see how the ```concurrentStoreAndDispatchQueues = false``` helps when there are slow consumers (or no consumers) and fast producers. You can also experiment with a consumer with 1 or 2 clients and a producer with 5 clients. 


```
mvn activemq-perf:producer -DsysTest.propsConfigFile=openwire-producer.properties 
```

When there are no consumers (worst case), see the results from the above test, 5 producers performed at about **2.2 times** faster than same test case with ```concurrentStoreAndDispatchQueues = true```

```
#########################################
####    SYSTEM THROUGHPUT SUMMARY    ####
#########################################
System Total Clients: 5
System Average Throughput: 163.77333333333334
```

### Conclusion

If your workload contains consumers that are slower than producers, you get better performance using ```concurrentStoreAndDispatchQueues = false```.

On the other hand, if your consumers can keep up with producers, you get significantly better performance using ```concurrentStoreAndDispatchQueues = true```. Keep in mind that this is the default for AmazonMQ.

### 3. Resources

  - https://activemq.apache.org/activemq-performance-module-users-manual

# Completion

Congratulations, you've successfully completed Lab 10! You can move on to [Lab 11: Polyglot programming](/labs/lab-11.md)

[Return to the Workshop Landing page](/README.md)
