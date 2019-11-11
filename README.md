# Amazon MQ Workshop: Lab Guide

## Overview of Workshop Labs

The [Amazon MQ Workshop](/README.md) introduces the relevant concepts and features of a message driven application using [Amazon MQ](https://aws.amazon.com/amazon-mq/). You will learn how to set-up an Amazon MQ broker and how to connect senders and receivers to exchange messages. This also includes using different protocols to demonstrate the protocol interoperability features Amazon MQ provides.

We will also dive into the security and monitoring features Apache Active MQ provides out of the box, and what Amazon MQ adds on top of them.  

At the end, we will look at how the broker fail-over works in a Multi-AZ set-up and how long does it takes.  

### Workshop Architecture

The architecture for this workshop is the following:  

![Workshop architecture](/images/workshop-architecture-new.png)

# Labs

## Prerequisites

This section provides a list of prerequisites that are required to successfully complete the workshop.

1. An AWS account and the proper rights to use Amazon MQ, Amazon CloudFormation, Amazon IAM, AWS Cloud9, Amazon S3 and Amazon VPC.

**Let's Begin! [Launch the CloudFormation Stack](/labs/lab-setup.md)**

## Lab Descriptions

Each of the labs in this workshop are independent and you may choose to do some or all of them, and in any order that you prefer. Only the first lab is compulsory, where you learn how to set-up an Amazon MQ broker.

* **[Lab 1: Broker Set-Up (Optional)](/labs/lab-1.md)** - Here, we set-up an Amazon MQ broker as we have it done via the CloudFormation template. We will touch and explain almost all configuration options and when to use which one. In our workshop, we will use the Amazon MQ broker which we already have set up via the CloudFormation template.

* **[Lab 2: Using Point-To-Point Messaging Using Queues](/labs/lab-2.md)** - In this exercise you will learn how to achieve Point-To-Point messaging with Amazon MQ using queues. The behavior of a message queue is that each message put onto the queue is consumed by only one receiver, so that there is a 1:1 relationship between sender and receiver for each published message.

* **[Lab 3: Using Publish-Subscribe Messaging Using Topics](/labs/lab-3.md)** - In this exercise you will learn how to achieve Publish-Subscribe messaging with Amazon MQ using topics. The behavior of a message topic is that a message published onto the topic will be received by all subscribers of that topic, so that there is 1:n relationship between sender and receivers for each published message.

* **[Lab 4: Testing a Broker Fail-Over](/labs/lab-4.md)** - Let's figure out how the broker fail-over in a Multi-AZ set-up works, what the impact for the clients is, and how long it will take to recover. We will have a sender and receiver running during this fail-over and observe their behavior.  

* **[Lab 5: Set-Up Amazon CloudWatch to Monitor Our Broker](/labs/lab-5.md)** - In this exercise, we will have a closer look to broker, queue and topic metrics that are provides via CloudWatch metrics. We will also create a CloudWatch alarm which will trigger an e-mail as soon as there are messages in the **ActiveMQ.DLQ** queue. The **ActiveMQ.DLQ** queue is a special queue used by Amazon MQ to store messages that failed to be processed multiple times (so called "poison messages").  

* **[Lab 6: Tighten up Security with Access Control](/labs/lab-6.md)** - Apache Active MQ provides out of the box a feature which allows to define fine grained access control policies per queue/topic. In this lab we will configure access control policies for a queue and topic and see how it works. 

* **[Lab 7: Active MQ Broker Statistics](/labs/lab-7.md)** - Apache Active MQ comes with an embedded web console, which provides useful broker statistics. We will discover these statistics and learn a bit more about the web console features:
  * How to create a new queue/topic
  * How to purge all messages from one queue
  * How to send a messages to a queue/topic using the web console

* **[Lab 8: Protocol Interoperability](/labs/lab-8.md)** - In this exercise, you are connecting one of the message producers to the broker and start sending messages. You also connect one of the message consumers to the broker, using a different protocol. We will repeat set-up this with multiple protocol combinations to figure out which protocol conversions are supported by Amazon MQ.

* **[Lab 9: Network of Brokers](/labs/lab-9.md)** - In this exercise, you will learn basic concepts about Network of Brokers and how this configuration of brokers can be used to scale producers and consumers. You will also learn about settings that play a critical role.

* **[Lab 10: Performance Testing](/labs/lab-10.md)** - In this exercise, you will learn about tools available for doing performance/load testing. This will help you to assess different broker configurations that would be helpful to optimize your workload performance using AmazonMQ.

* **[Lab 11: Polyglot Programming](/labs/lab-11.md)** - Most of this workshop focuses on working with Java clients. In this exercise, you will learn how to use other programming languages to communicate with AmazonMQ. You will work with a .Net client as an example. The Resources section in the lab provides links to code examples in other programming languages.

## Workshop Cleanup

This section provides instructions to tear down your environment when you're done working on the labs. [Workshop cleanup instructions](/labs/lab-cleanup.md)
