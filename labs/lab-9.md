# Lab 9: Network of Brokers

In order to provide massive scalability, Amazon MQ supports a feature known as Network of Brokers. In this configuration you can connect multiple single or dual instance brokers into a newtwork using a topology.

There are no predefined rules for connecting brokers, [there are a few topology patterns described in AWS documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/network-of-brokers.html#nob-topologies)..

If you are running an Advanced Lab (by either choosing advanced or all as Lab Type when delpoying the CloudFormation), the default mesh broker topology used with either single or active/standby instance configuration.

In the Mesh topology, Broker 1 and Broker 2, Broker 2 and Broker 3, Broker 1 and Broker 3 are connected with each other using OpenWire Transports.

# Completion

Congratulations, you've successfully completed Lab 9! You can move on to [Lab 10: Performance Testing](/labs/lab-10.md)

[Return to the Workshop Landing page](/README.md)
