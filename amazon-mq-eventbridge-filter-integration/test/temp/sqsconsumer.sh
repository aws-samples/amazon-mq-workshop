export AWS_REGION=us-west-1
export AWS_ACCOUNT=986635652628

# java -cp "target/demo-1.0-SNAPSHOT.jar:target/dependency-jars/*"  org.example.activemq.SQSConsumerMonitor 100
# java -verbose:class -cp target/amazonmq-eventbridge-1.0-SNAPSHOT-with-dependencies.jar   org.example.activemq.SQSConsumer
java -cp bin/amazonmq-eventbridge.jar   org.example.activemq.SQSConsumer


