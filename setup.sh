#!/bin/bash
cd ~/environment
wget https://d3pxv6yz143wms.cloudfront.net/8.222.10.1/java-1.8.0-amazon-corretto-devel-1.8.0_222.b10-1.x86_64.rpm
sudo yum localinstall -y java-1.8.0-amazon-corretto-devel-1.8.0_222.b10-1.x86_64.rpm
echo "export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))" >> ~/.bashrc
wget http://mirror.cc.columbia.edu/pub/software/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz
tar zxvf apache-maven-3.6.1-bin.tar.gz
echo "export PATH=~/environment/apache-maven-3.6.1/bin:$PATH" >> ~/.bashrc
svn checkout http://svn.apache.org/repos/asf/activemq/sandbox/activemq-perftest/ activemq-perftest
sed -i 's/5.8-SNAPSHOT/5.15.9/g' ~/environment/activemq-perftest/pom.xml
mkdir ~/environment/activemq-perftest/reports
userPassword=`aws ssm get-parameter --name "MQBrokerUserPassword" | grep Value`
brokerUser=`echo $userPassword | sed 's/"//g' | sed 's/Value://g' | cut -d',' -f1 | sed 's/ //g'`
brokerPassword=`echo $userPassword | sed 's/"//g' | sed 's/Value://g' | cut -d',' -f2`
source ~/.bashrc
printf "\nfactory.brokerURL=\"$url\"\n" >> ~/environment/amazon-mq-workshop/openwire-producer.properties
printf "factory.userName=$brokerUser\n" >> ~/environment/amazon-mq-workshop/openwire-producer.properties
printf "factory.password=$brokerPassword\n" >> ~/environment/amazon-mq-workshop/openwire-producer.properties
printf "\nfactory.brokerURL=$url\n" >> ~/environment/amazon-mq-workshop/openwire-consumer.properties
printf "factory.userName=$brokerUser\n" >> ~/environment/amazon-mq-workshop/openwire-consumer.properties
printf "factory.password=$brokerPassword\n" >> ~/environment/amazon-mq-workshop/openwire-consumer.properties
