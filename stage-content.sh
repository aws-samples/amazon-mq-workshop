#!/bin/bash

aws s3 cp --acl public-read CloudFormationTemplate/CreateAmazonMQWorkshop.json s3://cmr-amazon-mq-workshop/CreateAmazonMQWorkshop.json

aws s3 cp --acl public-read amazon-mq-client/target/amazon-mq-client.jar s3://cmr-amazon-mq-workshop/amazon-mq-client.jar
aws s3 cp --acl public-read stomp-client/target/stomp-client.jar s3://cmr-amazon-mq-workshop/stomp-client.jar
aws s3 cp --acl public-read mqtt-client/target/mqtt-client.jar s3://cmr-amazon-mq-workshop/mqtt-client.jar
aws s3 cp --acl public-read amqp-client/target/amqp-client.jar s3://cmr-amazon-mq-workshop/amqp-client.jar