# Workshop Setup

1\. To begin this workshop, **click one of the 'Deploy to AWS' buttons below for the region you'd like to use**. This is the AWS region where you will launch resources for the duration of this workshop. This will open the CloudFormation template in the AWS Management Console for the region you select.

Region | Launch Template
------------ | -------------
**N. Virginia** (us-east-1) | [![Launch Amazon MQ Workshop Stack into N. Virginia with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ohio** (us-east-2) | [![Launch Amazon MQ Workshop Stack into Ohio with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Oregon** (us-west-2) | [![Launch Amazon MQ Workshop Stack into Oregon with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Sydney** (ap-southeast-2) | [![Launch Amazon MQ Workshop Stack into Sydney with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Frankfurt** (eu-central-1) | [![Launch Amazon MQ Workshop Stack into Frankfurt with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)
**Ireland** (eu-west-1) | [![Launch Amazon MQ Workshop Stack into Ireland with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=amazonmqworkshop&templateURL=https://s3-eu-central-1.amazonaws.com/cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json)

2\. Once you have chosen a region and are inside the AWS CloudFormation Console, you should be on a screen titled "Select Template". We are providing CloudFormation with a template on your behalf, by providing a S3 template URL. Click the blue **Next** button to proceed.
<details><summary>Screenshot step 2</summary><p>

![Amazon MQ workshop setup step 2](/images/workshop-set-up-Step2.png)

</p></details><p/>


3\. On the following screen, "Specify Details", your Stack is pre-populated with the name "amazonmqworkshop". You can customize that to a name of your choice **less than 15 characters in length** or leave as is. The user launching the stack (you) already have the necessary permissions. Click **Next**.

*An IAM role will also be created and those role will be added to the EC2 instance, you are using during this workshop. On deletion of the stack, those resources will be deleted for you.*
<details><summary>Screenshot step 3</summary><p>

![Amazon MQ workshop setup step 3](/images/workshop-set-up-Step3.png)

</p></details><p/>


4\. On the "Options" page, leave the defaults and click **Next**.


5\. On the "Review" page, verify your selections, then scroll to the bottom and select the checkbox **I acknowledge that AWS CloudFormation might create IAM resources**. Then click **Create** to launch your stack.
<details><summary>Screenshot step 5</summary><p>

![Amazon MQ workshop setup step 5](/images/workshop-set-up-Step5.png)

</p></details><p/>


6\. Your stack will take about 3 minutes to launch and you can track its progress in the "Events" tab. When it is done creating, the status will change to "CREATE_COMPLETE".


7\. On the "Outputs" tab in CloudFormation, you can look-up the public IP address of your EC2 instance in the line "EC2IP". Use this to connect to your EC2 instance via SSH.
