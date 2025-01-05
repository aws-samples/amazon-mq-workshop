export MQ_PRODUCER_URL="ssl://b-87d1622d-851d-4804-87cd-0cb370060f5b-1.mq.us-west-1.amazonaws.com:61617"
export MQ_CONSUMER_URL="ssl://b-af427aca-42d3-4401-820f-53124cb8682a-1.mq.us-west-1.amazonaws.com:61617"
export MQ_USERNAME='admin'
export MQ_PASSWORD='F8tR|cCQJw\Nj4OU'

# java -cp target/amazonmq-eventbridge-1.0-SNAPSHOT-with-dependencies.jar  org.example.activemq.AMQConsumer -b $MQ_CONSUMER_URL -u $MQ_USERNAME -p $MQ_PASSWORD
java -cp bin/amazonmq-eventbridge.jar  org.example.activemq.AMQConsumer -b $MQ_CONSUMER_URL -u $MQ_USERNAME -p $MQ_PASSWORD