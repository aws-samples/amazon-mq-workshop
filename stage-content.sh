#!/bin/bash

mvn clean install

aws s3 cp --acl public-read CloudFormationTemplate/CreateAmazonMQWorkshop.json s3://amazon-mq-workshop/CreateAmazonMQWorkshop.json
aws s3 cp --acl public-read CloudFormationTemplate/Dockerfile s3://amazon-mq-workshop/Dockerfile
aws s3 cp --acl public-read CloudFormationTemplate/ec2-script-c9-docker.sh s3://amazon-mq-workshop/ec2-script-c9-docker.sh

aws s3 cp --acl public-read amazon-mq-client/target/amazon-mq-client.jar s3://amazon-mq-workshop/amazon-mq-client.jar
aws s3 cp --acl public-read stomp-client/target/stomp-client.jar s3://amazon-mq-workshop/stomp-client.jar
aws s3 cp --acl public-read mqtt-client/target/mqtt-client.jar s3://amazon-mq-workshop/mqtt-client.jar
aws s3 cp --acl public-read amqp-client/target/amqp-client.jar s3://amazon-mq-workshop/amqp-client.jar