export MQ_PRODUCER_URL="ssl://b-109b32a7-4e0e-486c-b8e7-9d98eb67acbc-1.mq.us-east-1.amazonaws.com:61617"
export MQ_CONSUMER_URL="ssl://b-5b0233ef-8ee7-4655-a3da-b6ba1e218e80-1.mq.us-east-1.amazonaws.com:61617"
export MQ_USERNAME="admin"
export MQ_PASSWORD="R1tVAZI)znNv6fN<"

java -cp "target/demo-1.0-SNAPSHOT.jar:target/dependency-jars/*"  org.fusebyexample.activemq.SimpleConsumer -b $MQ_CONSUMER_URL -u $MQ_USERNAME -p $MQ_PASSWORD 




