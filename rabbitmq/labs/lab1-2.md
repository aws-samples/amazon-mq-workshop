# Fanout exchange type
Fanout exchange is used to publish messages to all consumers of the exchange irrespective of their binding key. In this lab, we will not use any routing key to send messages to a fanout exchange. We will then launch two consumers to the fanout exchange with random binding and validate the messages.

## 
1. Change the directory to fanout-exchange.
2. Run the following command in the terminal window to send messages to an exchange with type as fanout. You can open the fanout-sender.py file to browse the source code for sending the messages on a fanout exchange. You can use any routing key but in this lab we will use  demo-routing-key.

```bash
python fanout-sender.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e <<exchange>> fanout-demo-exchange
```
We are now sending messages to a fanout exchange.The script will send messages until you stop it by pressing control+c.

3. Open two new terminal windows by right clicking on the existing terminal window and selecting split pane in two columns. Click the + option to open the bash shell.
![Exchange list](images/split-terminal.png)

3. Switch to second terminal window and change directory to fanout-exchange. 

4. Run the following command to receive messages on a queue that is bound to the fanout exchange using a random routing key value as the binding key. Please note that in our lab we have declared the exchange in the receiver as well. However, it is optional. If you know the order in which the sender receivers may be executed you can skip the exchange declaration in receiver. 

```bash
 python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e fanout-demo-exchange -q direct-fanout-q-1 -b demo-routing-key-1
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

Let us now create one more receiver on a different queue to check if the same message is routed to that queue as well if the binding key is the same.

1. Go to the third window and run the following command.

```bash
python topic-receiver.py -H $BROKER_ENDPOINT -P 5671 -u $BROKER_USER -p $BROKER_PASSWORD -e fanout-demo-exchange -q direct-fanout-q-2 -b demo-routing-key-2
 ```
 
More examples of RabbitMQ topic patterns can be found in official [documentation](https://www.rabbitmq.com/tutorials/tutorial-five-python.html).

Click [here](lab1.md) to go back to main page.