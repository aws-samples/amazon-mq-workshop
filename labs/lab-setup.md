# Workshop Setup

To begin this workshop, **click one of the 'Deploy to AWS' buttons below for the region you'd like to use**. This is the AWS region where you will launch resources for the duration of this workshop. This will open the CloudFormation template in the AWS Management Console for the region you select.

Region | Launch Template
------------ | -------------
**N. Virginia** (us-east-1) | [![Launch Amazon MQ Workshop Stack into N. Virginia with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ohio** (us-east-2) | [![Launch Amazon MQ Workshop Stack into Ohio with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**N. California** (us-west-1) | [![Launch Amazon MQ Workshop Stack into N. California with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Oregon** (us-west-2) | [![Launch Amazon MQ Workshop Stack into Oregon with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Seoul** (ap-northeast-2) | [![Launch Amazon MQ Workshop Stack into Seoul with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Singapore** (ap-southeast-1) | [![Launch Amazon MQ Workshop Stack into Singapore with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Sydney** (ap-southeast-2) | [![Launch Amazon MQ Workshop Stack into Sydney with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Tokyo** (ap-northeast-1) | [![Launch Amazon MQ Workshop Stack into Tokyo with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Frankfurt** (eu-central-1) | [![Launch Amazon MQ Workshop Stack into Frankfurt with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ireland** (eu-west-1) | [![Launch Amazon MQ Workshop Stack into Ireland with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)

Once you have chosen a region and are inside the AWS CloudFormation Console, you should be on a screen titled "Select Template". We are providing CloudFormation with a template on your behalf, by providing a S3 template URL. Click the blue **Next** button to proceed.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop setup step 2](/images/workshop-set-up-Step2.png)

</p></details><p/>

On the following screen, "Specify Details", your Stack name is pre-populated with the name "amazonmqworkshop". You can customize that to a name of your choice **less than 15 characters in length** or leave as is. 
The Amazon MQ broker will be named `<stackname>-Broker`.

You must also provide a password for the user that will administer the Amazon MQ broker. Choose something easy to remember, 12 characters or more. 
Click **Next**.


<details><summary>Screenshot</summary><p>

![Amazon MQ workshop setup step 3](/images/workshop-set-up-Step3.png)

</p></details><p/>

On the "Options" page, leave the defaults and click **Next**.

On the "Review" page, verify your selections, then scroll to the bottom and click **Create** to launch your stack.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop setup step 5](/images/workshop-set-up-Step5.png)

</p></details><p/>

Your stack will take sometime to launch, mostrly due to the creation of the Amazon MQ broker. You can track its progress in the "Events" tab. When it is done creating, the status will change to "CREATE_COMPLETE".

Once the creation has completed, you can look-up the URL to access the Cloud9 IDE in the line "Cloud9ConsoleUrl". Click on this URL to open the Cloud9 editor and enter *aws* as username and *mq* as password.
It can take sometime to launch the IDE the first time.


# Completion

Congratulations, you've successfully completed the workshop setup! You can move on to [Lab 1: Set-Up the Broker (Optional)](/labs/lab-1.md)

[Return the the Workshop Landing page](/README.md)
