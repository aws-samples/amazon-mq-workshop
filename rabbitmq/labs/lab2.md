# AmazonMQ - Rabbit MQ workshop Lab-2

In this lab, we will test the failover of RabbitMQ cluster. We use the same client in lab 1 to send messages. 

## 
1. Go to the terminal window and change the directory to lab-2.
2. Run the following command in the terminal window to send messages to an exchange with type as direct. You can open the direct-sender.py file to browse the source code for sending the messages on a direct exchange. You can use any routing key but in this lab we will use  demo-routing-key.

```bash
python direct-sender.py -H <<host>> -P <<Port>> -u <<user>> -p <<password>> -e direct-demo-exchange -r demo-routing-key
```
We are now sending messages to a direct exchange.The script will send messages until you stop it by pressing control+c.

3. While the messages are sent, open the Amazon MQ console and click on the broker that we created in the lab.

4. On the top right corner of the broker details page, you will see an option to reboot broker. Click on Reboot broker. It will reboot the cluster by rebooting one broker at a time.

![MQ Console](images/broker-reboot.png)
5. Watch the terminal console. You will notice that there will be an exception similar to below.

ConnectionResetError: [Errno 104] Connection reset by peer

You will notice that the client reconnects again after the exception and resumes sending messages even though the broker is still rebooting. The output should be similar to the screenshot below. 
![Broker Reconnect](images/broker-reconnect.png)

In our sender code, we have captured the exception generated as the broker disconnects the client. We then reconnect to an instance which remains active during the reboot.




