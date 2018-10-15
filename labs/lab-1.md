# Lab 1: Set-Up the Broker

In this lab you will create the Amazon MQ broker we will use during the workshop.

### 1. Navigate to the [Amazon MQ service console](https://console.aws.amazon.com/amazon-mq).

* If you don't have a broker running, the AWS console will forward you to the page below. Otherwise continue with step 3.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 1](/images/broker-set-up-Step1.png)

</p></details><p/>

### 2. Click to the navigation button in the top-left corner and select **Brokers**.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 2](/images/broker-set-up-Step2.png)

</p></details><p/>

### 3. On the Broker home page, click the button **Create broker**.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 3](/images/broker-set-up-Step3.png)

</p></details><p/>


### 4. Configure the broker details as follows and scroll down:

* Broker name: `workshop`
* Broker instance type: `mq.t2.micro`
* Deployment mode: `Active/standby broker for high availability`

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 4](/images/broker-set-up-Step4.png)

</p></details><p/>

### 5. Continue with the broker web console access configuration and scroll down:

* Username: `workshopUser`
* Password: `<choose one>`

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 5](/images/broker-set-up-Step5.png)

</p></details><p/>

### 6. Open the brokers advanced settings and choose the following settings. Scroll down afterwards.

* Virtual Private Cloud (VPC): `{Stackname}-VPC`
* Subnet(s): `{Stackname}-PublicSubnet1` and `{Stackname}-PublicSubnet2`

> It's important to use the VPC, subnets and security group which were created by the CloudFormation template to make sure the connectivity between your EC2 instance and Amazon MQ is working!

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 6](/images/broker-set-up-Step6.png)

</p></details><p/>

### 7. Continue with the advanced settings as below and click **Create broker**.

* Security group(s): **{Stackname}-AmazonMQSecurityGroup-...**
* Public accessibility: **Yes** (to be able to access the Apache ActiveMQ web console)
* Maintenance window: **No preference**

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop Lab 1 step 7](/images/broker-set-up-Step7.png)

</p></details><p/>


### 8. It might take up to 10 minutes for the broker to go into **Running** state and be ready to use.

### 9. Store Bash Variables

Open an SSH session to the EC2 instance you have created during the set-up. To make it easier to run the commands in the following labs we store frequently used parameters like Amazon MQ broker user, password, etc. in Bash environment variables. Before you run the following commands, replace the values **<...>** with the value you have chosen.

``` bash
echo 'user=<user>' >> ~/.bashrc; source ~/.bashrc
echo 'password=<password>' >> ~/.bashrc; source ~/.bashrc
echo 'url="<failover openWire url>"' >> ~/.bashrc; source ~/.bashrc
```

# Completion

Congratulations, you've successfully completed Lab 1! You can move on to [Lab 2: Using Point-To-Point Messaging Using Queues](/labs/lab-2.md)

[Return the the Workshop Landing page](/README.md)