# AmazonMQ - Rabbit MQ workshop Lab-1

RabbitMQ by default uses the AMQP 0-9-1 protocol for connectivity. Messaging in RabbitMQ is based on the concept on exchange, routing key, bindings and queues. A sender sends messages to an exchange which can have a routing key. Receivers get messages from a queue and the queue is bound to an exchange using a binding key. More details on RabbitMQ messaging concepts can be found in their official documentation. In this lab, we will explore the three types of exchange which RabbitMQ provides for message routing.

The patterns can be described as:

1. Direct - In this exchange type the sender sends the message to the exhange using a routing key. A routing key is like a meta data attribute for the message. Any receiver who wants to get a message from an exhange needs to bind its queue to the exchange using a binding key. The binding key needs to match the routing key from the sender to route messages to the queue used by the receiver. It is possible for sender to send the message directly to queue by using the default exchange type and using the routing key which is the same as the queue name. A default exchange is just a pre-declared direct exchange with no name.

2. Fanout - Fanout exchange provides a publish-subscribe pattern for messaging in RabbitMQ. Messages sent to an exchange with type as fanout are sent to all the queues that are bound to it irrespective of the routing key on the message.

3. Topic - A topic exchange type provides a means to send messages to queues which are based on pattern matching of the routing key. Various parts of a routing key needs to be delimited using a '.' token. The binding key for the different queue bindings using a pattern matching based on the differnt parts of the routing key.

We will explore each of the three exchange types using examples.

## Pre-requisites 
1. Go to the terminal window on Cloud9 instance and run the following commands to instal the Pika library.

```bash
sudo pip install pika
```

Click on the link for each of the exchange types to go to the lab.
1. [Direct](lab1-1.md)
2. [Fanout](lab1-2.md)
3. [Topic](lab1-3.md)




