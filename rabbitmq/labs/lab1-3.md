# Topic exchange type
Topic exchange provides the ability to route messages based on matching patterns. Lets say we have a sender who is sending order related messages. The routing key for such a message can indicate the hierarchy of the order. For example, if the order is in the EU region in home category. It can have a routing key of orders.eu.home - the different parts of the key are seperated by a period. Now, if we have different consumers who want to get messages pertaining to their specific needs - they can bind their queue to the exchange based on a pattern. A consumer interested in all orders can simply say orders.#, a consumer interested in orders in US region can say orders.eu.#
We will explore a similar example in the lab.

## 
1. Change the directory to topic-exchange.
2. Run the following command in the terminal window to send messages to an exchange with type as topic. You can open the topic-sender.py file to browse the source code for sending the messages on a direct exchange.

```bash
python topic-sender.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e topic-demo-exchange -r orders.eu.home
```
We are now sending messages to a topic exchange by using a routing key which uses delimited tokens to facilitate routing.The script will send messages until stop it by pressing control+c.
3. Open two new terminal windows by right clicking on the existing terminal window and selecting split pane in two columns. Click the + option to open the bash shell.
![Exchange list](images/split-terminal.png)

3. Switch to second terminal window and change directory to topic-exchange. 

4. Run the following command to receive messages on a queue that is bound to the exchange using a binding key with a wild card. Please note that in our lab we have declared the exchange in the receiver as well. However, it is optional. If you know the order in which the sender receivers may be executed you can skip the exchange declaration in receiver. The binding key will have the # token to accept all orders in the US region.

```bash
 python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e topic-demo-exchange -q topic-demo-q-1 -b orders.eu.#
 ```
Lets check the configuration on the exchange to confirm if the binding was created on the queue. We will do that by running the rabbitmqadmin command.

```bash
./rabbitmqadmin -H $BROKER_ENDPOINT -P 443 -u $BROKER_USER -p $BROKER_PASSWORD -sk list exchanges
```
The command should list the different exchanges on the broker. You should see the exchange that you just created on the broker with the type as fanout. The output should be similar to the image below.

![Exchange list](images/lab-2-2/exchange-list.png)

You can see that the exchange type is listed as fanout. Lets now confirm that the binding to the queue is using the same binding that we specified in executing our receiver script.

```bash
./rabbitmqadmin -H $BROKER_ENDPOINT -P 443 -u $BROKER_USER -p $BROKER_PASSWORD -sk list bindings
```

The output should be similar to the image below. It shows that the binding we created is attached to the same exchanged as source and using the key that we specified.

![Binding list](images/binding-list.png)

Let us now create one more receiver on a different queue to check if the same message is routed to that queue as well if the binding key matches the pattern.

1. Go to the third window and run the following command.

```bash
 python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e topic-demo-exchange -q topic-demo-q-2 -b orders.#
 ```
 
More examples of RabbitMQ topic patterns can be found in official [documentation](https://www.rabbitmq.com/tutorials/tutorial-five-python.html).You can try to change the binding key to a pattern which does not match the routing key and the receiver should not get any messages.