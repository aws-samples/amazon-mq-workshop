#!/bin/bash

# Set Path
echo "Starting Amazon Workshop Script ..."
cd ~



sudo amazon-linux-extras install docker -y
sudo service docker start

mkdir /home/ec2-user/workspace
cd ~/workspace
# Copy the clients used for the labs
wget https://s3.amazonaws.com/amazon-mq-workshop/labs-clients.zip
unzip labs-clients.zip
rm labs-clients.zip
chmod +x *.jar

cd ~
wget https://s3.amazonaws.com/amazon-mq-workshop/Dockerfile

echo "user=$1" > bash_env_src
echo "password=$2" >> bash_env_src
sudo `aws ecr get-login --no-include-email --registry-ids 416075262792 --region eu-west-1`
sudo docker build -t cloud9amqws .
sudo docker run -d -v /home/ec2-user/workspace:/cloud9/workspace -p 8180:8180 cloud9amqws --auth aws:mq

# Signal CF 
echo "Tell CloudFormation we're done ..."
bash /signal.txt
#sudo rm /ec2-script-c9-docker.sh
#sudo rm /bash_env

