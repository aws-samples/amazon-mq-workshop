# AmazonMQ - Rabbit MQ workshop Lab-0
In this lab, we will run a cloudformation template to setup the environment. We will be creating a private RabbitMQ cluster. The template also creates a Cloud9 instance which will be in a public subnet. We will be using the Cloud9 instance to run our labs.

The architecture for the broker can be described as below:

![Private Cluster](images/private-broker.png)

The brokers run in a service owned account. Your account will have a VPC endpoint which can run on multiple subnets. The VPC endpoint points to a NLB that runs on the service account which points to the broker instances.

To begin this workshop, **click one of the 'Deploy to AWS' buttons below for the region you'd like to use**. This is the AWS region where you will launch resources for the duration of this workshop. This will open the CloudFormation template in the AWS Management Console for the region you select. **You will be providing a user name and password for the broker as parameter. The same credentials will be used to connect to the broker.**

Region | Launch Template
------------ | -------------
**Ohio** (us-east-2) | [![Launch Amazon MQ Workshop Stack into Ohio with CloudFormation](images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=amqrabbitmqworkshop&templateURL=https://amq-rabbitmq-workshop.s3-us-west-2.amazonaws.com/template.yaml)

The template will take around 15-20 mins to complete. Once completed, please go to the outputs of the cloudformation template. You should see a link for launching the cloud9 instance. Click on the link to laumch the Cloud9 instance.
![Cloud9 Link](images/cloud9-output.png)


We will be running our labs from the cloud9 instace. Click the link to open the Cloud9 instance.

# Accessing the RabbitMQ console.

We have deployed a private broker cluster which means that the RabbitMQ web console will not be accesible over public internet. You can still setup access to the RabbitMQ web console using a proxy. However, in this lab we will be using the rabbitmqadmin tool to view the queues and exchanges.

You can also follow the instructions [here](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/accessing-web-console-of-broker-without-private-accessibility.html) to access the RabbitMQ webconsole for private broker.

1. Go to the terminal and follow the steps below to install rabbitmqadmin.

```bash
wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.8.9/bin/rabbitmqadmin

chmod u+x rabbitmqadmin 

```
2. Get the broker endpoint by extracting the output results from the cloudformation template.

```bash
aws cloudformation describe-stacks \
    --stack-name amqrabbitmqworkshop \
    --query 'Stacks[].Outputs[?OutputKey==`PrivateBrokerEndpoint`][OutputValue]' \
    --output text

```
3. Let’s store this broker endpoint in an environment variable, so we don’t have to repeat it all the time:

```bash
export BROKER_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name amqrabbitmqworkshop \
    --query 'Stacks[].Outputs[?OutputKey==`PrivateBrokerEndpoint`].OutputValue' \
    --output text)
```

4. Let's store the broker credentials in SSM paramters so we dont have to type it every time from command line.

```bash
export BROKER_USER="<<REPLACE_WITH_BROKER_USER"
export BROKER_PASSWORD="<<REPLACE_WITH_BROKER_PASSWORD"
```


Run the command below to list the nodes in the cluster.

```bash
./rabbitmqadmin --host=$BROKER_ENDPOINT  --port=443 \
    --username=$BROKER_USER --password=$BROKER_PASSWORD \
    -sk list nodes

```

Click [here](lab1.md) to go to the next lab.


