#!/bin/bash

#mvn clean install

aws s3 cp --acl public-read CloudFormationTemplate/CreateAmazonMQWorkshop.json s3://amazon-mq-workshop/CreateAmazonMQWorkshop.json