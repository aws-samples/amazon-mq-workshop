# Workshop Setup

To begin this workshop, **click one of the 'Deploy to AWS' buttons below for the region you'd like to use**. This is the AWS region where you will launch resources for the duration of this workshop. This will open the CloudFormation template in the AWS Management Console for the region you select.

Region | Launch Template
------------ | -------------
**Ohio** (us-east-2) | [![Launch Amazon MQ Workshop Stack into Ohio with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**N. California** (us-west-1) | [![Launch Amazon MQ Workshop Stack into N. California with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Oregon** (us-west-2) | [![Launch Amazon MQ Workshop Stack into Oregon with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Seoul** (ap-northeast-2) | [![Launch Amazon MQ Workshop Stack into Seoul with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Singapore** (ap-southeast-1) | [![Launch Amazon MQ Workshop Stack into Singapore with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Sydney** (ap-southeast-2) | [![Launch Amazon MQ Workshop Stack into Sydney with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Tokyo** (ap-northeast-1) | [![Launch Amazon MQ Workshop Stack into Tokyo with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Frankfurt** (eu-central-1) | [![Launch Amazon MQ Workshop Stack into Frankfurt with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**Ireland** (eu-west-1) | [![Launch Amazon MQ Workshop Stack into Ireland with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)
**N. Virginia** (us-east-1) | [![Launch Amazon MQ Workshop Stack into N. Virginia with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=amazonmqworkshop&templateURL=https://s3.amazonaws.com/amazon-mq-workshop/CreateAmazonMQWorkshop.yaml)


Once you have chosen a region and are inside the AWS CloudFormation Console, you should be on a screen titled "Quick Create Stack".

<details><summary>Screenshot new CF Console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-1.png)

</p></details><p/>

<details><summary>Screenshot old CF Console</summary><p>

![Amazon MQ workshop setup step 2](/images/labsetup-1-old.png)

</p></details><p/>

In the **Stack name** section the Stack name is pre-populated with the name "amazonmqworkshop". You can customize that to a name of your choice **less than 15 characters in length** or leave as is. 
The Amazon MQ broker will be named `<stackname>-Broker`.

In the **Parameter** section you must provide a password for the user that will administer the Amazon MQ broker. Choose something easy to remember, 12 characters or more. Select a Lab Level. There are three options provided. The **basic** lab is for Labs 1 thru 8. The **advanced** lab is for Labs 9-11 and the **all** option is for all labs. Select a lab that is most suitable for you. You can attempt each level at your own pace. One thing to remember is to run a lab, delete all resources for the lab and then attempt the next lab. For example if you selected **basic** lab, and created CloudFormation resources and wanted to attempt the **advanced** lab, then you must delete the **basic** lab stack first and then create reosurces for **advanced** lab.
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

It can take sometime to launch the IDE the first time.
Once the creation has completed, you can click on your stack name (“amazonmqworkshop” or the custom name you chose instead) to check the details of your stack. Cloud9 IDE instance has been setup as part of the stack. Navigate to Cloud9 service and look for MQClient workspace and click on OpenIDE to open the workspace.
# Completion

Congratulations, you've successfully completed the workshop setup! You can move on to [Lab 1: Set-Up the Broker (Optional)](/labs/lab-1.md)

[Return to the Workshop Landing page](/README.md)
