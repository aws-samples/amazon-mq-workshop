wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.8.9/bin/rabbitmqadmin

chmod u+x rabbitmqadmin 

sudo pip install pika

echo BROKER_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name amqrabbitmqworkshop \
    --query 'Stacks[].Outputs[?OutputKey==`PrivateBrokerEndpoint`].OutputValue' \
    --output text) >> ~/.bashrc; 
    
echo BROKER_USER='admin' >> ~/.bashrc; 
echo BROKER_PASSWORD='admin1234567' >> ~/.bashrc;  



source ~/.bashrc