# Amazon MQ Workshop: Lab Guide

## Overview of Workshop Labs
The [Amazon MQ Workshop](http://aws.amazon.com/events/amazon-mq-workshop) introduces the relevant concepts and features of a message driven application using [Amazon MQ](https://aws.amazon.com/amazon-mq/). You will learn how to set-up an Amazon MQ broker and how connect sender and receivers to them, to send and receive messages. This also includes using different protocols to demonstrate the protocol interoperability Amazon MQ provides.  
We will also dive into the security and monitoring features Apache Active MQ provides out of the box, and what Amazon MQ adds on top of it.  
At the end, we will have a look how the broker fail-over works in a Multi-AZ set-up and how long does it takes.  

### Workshop Architecture
The architecture for this workshop is the following:  

![Workshop architecture](/images/workshop-architecture.png)

### Prerequisites
This section provides a list of prerequisites that are required to successfully complete the workshop.

1\. An AWS account setup and the proper rights to use Amazon CloudFormation, Amazon IAM, Amazon EC2, Amazon S3 and Amazon VPC.

2\. An AWS EC2 key pair in the region you are using for this workshop.

3\. An SSH client on your local machine.


### Let's Begin! Launch the CloudFormation Stack

[Workshop setup instructions](/labs/lab-setup.md)


### Labs
Each of the labs in this workshop is an independent section and you may choose to do some or all of them, or in any order that you prefer.

* **Lab 1: Broker set-up**  

  Here, we are setting-up the Amazon MQ broker we are using during this workshop. We will touch and explain almost all configuration options and when to use which one.  
  [Lab instructions](/labs/lab-1.md)

* **Lab 2: Using Point-To-Point messaging**  

  In this exercise you will learn how to achieve Point-To-Point messaging with Amazon MQ using queues. The behavior of a message queue is that each message is consumed by one receiver, so that there is a 1:1 relationship between sender and receiver for each considered message.  
  [Lab instructions](/labs/lab-2.md)

* **Lab 3: Using Publish-Subscribe messaging**  

  In this exercise you will learn how to achieve Publish-Subscribe messaging with Amazon MQ using topics. The behavior of a message topic is that a sender publishes a message into the topic that will be received by all subscribers of that topic, so that there is 1:n relationship between sender and receivers for each considered message.  
  [Lab instructions](/labs/lab-3.md)

* **Lab 4: Watch the broker statistics**  

  Apache Active MQ comes with an embedded web console, which provides useful broker statistics to you. We will discover these statistics and learn a bit more about the web console features, e.g.:
  * How to create a new queue/topic?
  * How to purge all messages from one queue?
  * How to send a messages to a queue/topic using the web console?

  [Lab instructions](/labs/lab-4.md)

* **Lab 5: Set-up CloudWatch to monitor our broker**  

  In this exercise, we will have a closer look which broker, queue and topic metrics are provides via CloudWatch metrics. We will also create an CloudWatch alarm which will trigger an e-mail, as soon as there are messages in the **ActiveMQ.DLQ** queue. The **ActiveMQ.DLQ** queue is a special queue, where Amazon MQ will move messages to it, when they coudn't be processed for multiple times (so called poison messages).  
  [Lab instructions](/labs/lab-5.md)

* **Lab 6: Tighten up security with access control**  

  Apache Active MQ provides out of the box a feature which allows you to define fine grained access control policies per queue/topic. In this lab we will configure such kind of access control policies for a queue and topic and see how it works.  
  [Lab instructions](/labs/lab-6.md)

* **Lab 7: Testing a broker fail-over**  

  Let's figure out how the broker fail-over in a Multi-AZ set-up works, what the impact for the clients is and how long it will take. We will have a sender and receiver running during this fail-over and observe they behavior.  
  [Lab instructions](/labs/lab-7.md)

* **Lab 8: Protocol interoperability**  

  In this exercise, you are connecting one of the message producer to the broker and start sending message. You also connect one of the message consumer to the broker, using a different protocol. We will repeat this with multiple protocol combinations to figure out, which protocol conversions are supported by Amazon MQ.  
  [Lab instructions](/labs/lab-8.md)


### Workshop Cleanup

This section provides instructions to tear down your environment when you're done working on the labs.  
  [Workshop cleanup instructions](/labs/lab-cleanup.md)
