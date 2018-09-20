# Lab 1: Set-up the broker

In this lab you will create the Amazon MQ broker, we will use during the workshop.

1\. Navigate to the [Amazon MQ service console](https://console.aws.amazon.com/amazon-mq).
* If you don't have a broker running, the AWS console will forward you to the page below. Otherwise continue with step 3.
<details><summary>Screenshot step 1</summary><p>

![Amazon MQ workshop lab 1 step 1](/images/broker-set-up-Step1.png)

</p></details><p/>


2\. Click to the navigation button in the top left corner and select **Brokers**.
<details><summary>Screenshot step 2</summary><p>

![Amazon MQ workshop lab 1 step 2](/images/broker-set-up-Step2.png)

</p></details><p/>


3\. On the Broker home page, click the button **Create broker**.
<details><summary>Screenshot step 3</summary><p>

![Amazon MQ workshop lab 1 step 3](/images/broker-set-up-Step3.png)

</p></details><p/>


4\. Configure the broker details as following and scroll down:
  * Broker name: **workshop**
  * Broker instance type: **mq.t2.micro**
  * Deployment mode: **Active/standby broker for high availability**
<details><summary>Screenshot step 4</summary><p>

![Amazon MQ workshop lab 1 step 4](/images/broker-set-up-Step4.png)

</p></details><p/>


5\. Continue with the broker web console access configuration and scroll down:
  * Username: **workshop-user**
  * Password: **\<choose one>\**
<details><summary>Screenshot step 5</summary><p>

![Amazon MQ workshop lab 1 step 5](/images/broker-set-up-Step5.png)

</p></details><p/>


6\. Open the brokers advanced settings and choose the following settings. Scrcoll down afterwards.
  * Virtual Private Cloud (VPC): **{Stackname}-VPC**
  * Subnet(s): **{Stackname}-Subnet1** and **{Stackname}-Subnet2**

**It's important to use the VPC, subnet and security group which was created with the CloudFormation template to make sure, the connectivity between your EC2 instance and Amazon MQ is working!**
<details><summary>Screenshot step 6</summary><p>

![Amazon MQ workshop lab 1 step 6](/images/broker-set-up-Step6.png)

</p></details><p/>


7\. Continue with the advanced settings as below and click **Create broker**.
  * Security group(s): **{Stackname}-AmazonMQSecurityGroup-...**
  * Public accessibility: **Yes** (to be able to access the Apache ActiveMQ web console)
  * Maintenance window: **No preference**
<details><summary>Screenshot step 7</summary><p>

![Amazon MQ workshop lab 1 step 7](/images/broker-set-up-Step7.png)

</p></details><p/>


8\. It will take up to 10 minutes until the broker is in the **Running** state and ready to use.

9\. Open an SSH session to your EC2 instance, you have created during the set-up. We will store frequently used parameters like Amazon MQ broker user, password, etc. in Bash environment variables, to make it easier to run the commands in the following labs. Before you run the following commands, replace the values **<...>** with the value you have chosen. 

```
echo 'user=<user>' >> ~/.bashrc; source ~/.bashrc
echo 'password=<password>' >> ~/.bashrc; source ~/.bashrc
echo 'url="<failover openWire url>"' >> ~/.bashrc; source ~/.bashrc
```
