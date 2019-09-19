#!/bin/bash

aws s3 cp --acl public-read CloudFormationTemplate/CreateAmazonMQWorkshop.yaml s3://amazon-mq-workshop/CreateAmazonMQWorkshop.yaml