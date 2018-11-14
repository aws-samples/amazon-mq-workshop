# Workshop Setup

To begin this workshop, **click one of the 'Deploy to AWS' buttons below for the region you'd like to use**. This is the AWS region where you will launch resources for the duration of this workshop. This will open the CloudFormation template in the AWS Management Console for the region you select.

Region | Launch Template
------------ | -------------
**N. Virginia** (us-east-1) | [![Launch Amazon MQ Workshop Stack into N. Virginia with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ohio** (us-east-2) | [![Launch Amazon MQ Workshop Stack into Ohio with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**N. California** (us-west-1) | [![Launch Amazon MQ Workshop Stack into N. California with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Oregon** (us-west-2) | [![Launch Amazon MQ Workshop Stack into Oregon with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Seoul** (ap-northeast-2) | [![Launch Amazon MQ Workshop Stack into Seoul with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Singapore** (ap-southeast-1) | [![Launch Amazon MQ Workshop Stack into Singapore with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Sydney** (ap-southeast-2) | [![Launch Amazon MQ Workshop Stack into Sydney with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Tokyo** (ap-northeast-1) | [![Launch Amazon MQ Workshop Stack into Tokyo with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Frankfurt** (eu-central-1) | [![Launch Amazon MQ Workshop Stack into Frankfurt with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ireland** (eu-west-1) | [![Launch Amazon MQ Workshop Stack into Ireland with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.json)


Once you have chosen a region and are inside the AWS CloudFormation Console, you should be on a screen titled "Quick Create Stack".

<details><summary>Screenshot new CF Console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-1.png)

</p></details><p/>

<details><summary>Screenshot old CF Console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-1-old.png)

</p></details><p/>

In the **Stack name** section the Stack name is pre-populated with the name "amazonmqworkshop". You can customize that to a name of your choice **less than 15 characters in length** or leave as is. 
The Amazon MQ broker will be named `<stackname>-Broker`.

In the **Parameter** section you must provide a password for the user that will administer the Amazon MQ broker. Choose something easy to remember, 12 characters or more. 
Leave the rest of the options as is and check the **I acknowledge that AWS CloudFormation might create IAM resources** box. This is to allow CloudFormation to create a Role to allow access to resources needed by the workshop.


Scroll to the bottom and click **Create** to launch your stack.

Your stack will take sometime to launch, mostly due to the creation of the Amazon MQ broker. You can track its progress in the "Events" tab. When it is done creating, the status will change from "CREATE_IN_PROGRESS" to "CREATE_COMPLETE".

<details><summary>Screenshot new CF console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-2.png)

</p></details><p/>

<details><summary>Screenshot old CF console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-2-old.png)

</p></details><p/>

## Cloud9 IDE

Once the creation has completed, you can look-up the URL to access the Cloud9 IDE in the line "Cloud9ConsoleUrl". Click on this URL to open the Cloud9 editor and enter *aws* as username and *mq* as password.
It can take sometime to launch the IDE the first time.




# Completion

Congratulations, you've successfully completed the workshop setup! You can move on to [Lab 1: Set-Up the Broker (Optional)](/labs/lab-1.md)

[Return the the Workshop Landing page](/README.md)
