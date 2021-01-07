# Direct exchange type
Direct exchange provides the ability to route messages based on specific routing key.Messages sent to a direct exchange has a routing key which needs to match exactly to a binding key for it to be routed to the specific queue. In this lab, we will look at a sender which sends messages to a direct exchange and have two consumers with two different queues bound to the exchange with the same binding key.

## 
1. Change the directory to direct-exchange.
2. Run the following command in the terminal window to send messages to an exchange with type as direct. You can open the direct-sender.py file to browse the source code for sending the messages on a direct exchange. You can use any routing key but in this lab we will use  demo-routing-key.

```bash
python direct-sender.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e direct-demo-exchange -r demo-routing-key
```
We are now sending messages to a direct exchange.The script will send messages until you stop it by pressing control+c.

3. Open two new terminal windows by right clicking on the existing terminal window and selecting split pane in two columns. Click the + option to open the bash shell.

![Exchange list](images/split-terminal.png)

3. Switch to second terminal window and change directory to direct-exchange. 

4. Run the following command to receive messages on a queue that is bound to the exchange using the same routing key value as the binding key. Please note that in our lab we have declared the exchange in the receiver as well. However, it is optional. If you know the order in which the sender receivers may be executed you can skip the exchange declaration in receiver. 

```bash
 python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e direct-demo-exchange -q direct-demo-q-1 -b demo-routing-key
 ```
Lets check the configuration on the exchange to confirm if the binding was created on the queue. We will do that by running the rabbitmqadmin command.

```bash
./rabbitmqadmin -H $BROKER_ENDPOINT -P 443 -u $BROKER_USER -p $BROKER_PASSWORD -sk list exchanges
```
The command should list the different exchanges on the broker. You should see the exchange that you just created on the broker with the type as fanout. The output should be similar to the image below.

![Exchange list](images/lab-2-2/exchange-list.png)

You can see that the exchange type is listed as direct. Lets now confirm that the binding to the queue is using the same binding that we specified in executing our receiver script.

```bash
./rabbitmqadmin -H $BROKER_ENDPOINT -P 443 -u $BROKER_USER -p $BROKER_PASSWORD -sk list bindings
```

The output should be similar to the image below. It shows that the binding we created is attached to the same exchanged as source and using the key that we specified.

![Binding list](images/binding-list.png)

Let us now create one more receiver on a different queue to check if the same message is routed to that queue as well if the binding key is the same.

1. Go to the third window and run the following command.

```bash
 python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e direct-demo-exchange -q direct-demo-q-2 -b -b demo-routing-key
 ```
 
More examples of RabbitMQ topic patterns can be found in official [documentation](https://www.rabbitmq.com/tutorials/tutorial-five-python.html).You can try to change the binding key to a value which does not match the routing key and the receiver should not get any messages.

Click [here](lab1.md) to go back to main page.