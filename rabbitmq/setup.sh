wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.8.9/bin/rabbitmqadmin

chmod u+x rabbitmqadmin 

sudo pip install pika

echo BROKER_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name amqrabbitmqworkshop \
    --query 'Stacks[].Outputs[?OutputKey==`PrivateBrokerEndpoint`].OutputValue' \
    --output text) >> ~/.bashrc; 
    
echo BROKER_USER='<<REPLACE_WITH_BROKER_USER>>' >> ~/.bashrc; 
echo BROKER_PASSWORD='<<REPLACE_WITH_BROKER_PASSWORD>>' >> ~/.bashrc;  



source ~/.bashrc