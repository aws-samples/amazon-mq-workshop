# Lab 6: Tighten up Security with Access Control

In this lab you will tighten up the security configuration with access control policies, so that you control which user can send/receive messages from which queues/topics.

### 1. Create new users

Navigate to the Amazon MQ Brokers page.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 1](/images/amazon-mq-broker-overview.png)

</p></details><p/>

Click on the name of the broker, you created in [Lab 1](/labs/lab-1.md).
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 2](/images/security-set-up-Step2.png)

</p></details><p/>

Go to the bottom of the page and click `Create user`.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 3](/images/security-set-up-Step3.png)

</p></details><p/>

Create two users. One with the name and group `user1` and a second one with the name and group `user2`.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 4a](/images/security-set-up-Step4a.png)

</p></details><p/>

### 2. Apply the changes

In order to apply the modifications done to the broker configuration, such as adding users, the broker must be rebooted. 
Go to the top of the page and choose `Actions -> Reboot broker`.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 5](/images/security-set-up-Step5.png)

</p></details><p/>

It takes a few minutes for the broker to finish the reboot. The reboot is done when the status in the **Pending modifications** column is empty.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 6](/images/security-set-up-Step6.png)

</p></details><p/>

### 3. Edit the configuration

Go to list of brokers and click on the name of your broker. Click **Edit** at the top of the page.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 7](/images/security-set-up-Step7.png)

</p></details><p/>

To view and edit the latest configuration, just click the **Edit** link in the Configuration section. This will open a new tab where you can see the current configuration. 

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 8](/images/security-set-up-Step8.png)

</p></details><p/>


On this page, you see the XML configuration of Active MQ. Click `Edit configuration` button in the top right corner.

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 9](/images/security-set-up-Step9.png)

</p></details><p/>

Scroll down to the element `<authorizationPlugin\>` and modify the content so that it looks as follows. Afterwards click **Save**, and confirm, to store the configuration changes. Make sure that the whole section is uncommented removing the opening and closing comments marks `<!--` and `--!>`. What this configuration does is to allow `user1` to manage, write and read from `queue.user1`, but not `user2`, who is allowed instead to a/r/w on `topic.user2`.

``` xml
    <authorizationPlugin>
      <map>
        <authorizationMap>
          <authorizationEntries>
            <authorizationEntry admin="admin,activemq-webconsole" queue="&gt;" read="admin,activemq-webconsole" write="admin,activemq-webconsole"/>
            <authorizationEntry admin="admin,activemq-webconsole" topic="&gt;" read="admin,activemq-webconsole" write="admin,activemq-webconsole"/>
            <authorizationEntry admin="admin,user1" queue="queue.user1" read="user1" write="user1"/>
            <authorizationEntry admin="admin,user2" read="user2" topic="topic.user2" write="user2"/>
            <authorizationEntry admin="admin,user1,user2" read="admin,user1,user2" topic="ActiveMQ.Advisory.&gt;" write="admin,user1,user2"/>
          </authorizationEntries>
          <tempDestinationAuthorizationEntry>
            <tempDestinationAuthorizationEntry admin="tempDestinationAdmins" read="tempDestinationAdmins" write="tempDestinationAdmins"/>
          </tempDestinationAuthorizationEntry>
        </authorizationMap>
      </map>
    </authorizationPlugin>
```

<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 10](/images/security-set-up-Step10.png)

</p></details><p/>

Close this browser-tab and go back to the Edit broker page. From the **Revision** drop down select the new revision you just created.  You may need to refresh your browser window to see the Revision.  Once the new Revision is selected, click **Schedule modifications**. On the next page, select **Immediately** and click on **Apply**. It might takes few minutes to restart the broker.
<details><summary>Screenshot</summary><p>

![Amazon MQ workshop lab 6 step 11](/images/security-set-up-Step11.png)

</p></details><p/>

After the broker is again in the status `Running`, run the following command in a terminal tab in the Cloud9 IDE (replacing the parameter **<user 2 password>** with the value you have chosen) to start sending messages to `queue.user1` as `user2`.

``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -user user2 -password <user 2 password> -mode sender -type queue -destination queue.user1 -name user2
```

You should see a log output like the following, indicating that `user2` is not authorized to write into this queue. 

``` bash
[ActiveMQ Task-1] INFO org.apache.activemq.transport.failover.FailoverTransport - Successfully connected to ssl://b-4e4bfd69-7b83-4a27-9faf-4684cfa80443-2.mq.eu-central-1.amazonaws.com:61617
Error: User user2 is not authorized to write to: queue://queue.user1
```

Try now to send messages to the same queue as `user1`.
``` bash
java -jar ./bin/amazon-mq-client.jar -url $url -user user1 -password <user 1 password> -mode sender -type queue -destination queue.user1 -name user1
```

As expected, `user1` can write on this queue. You can try a similar excercise with the topic `topic.user2`, verifying that `user1` cannot publish nor receive messages from the topic, while `user2` can (the commands can be found in [Lab 2](/labs/lab-2.md), but you will need to adapt the `-user` and `-password` parameters)


13\. Stop the sender by holding `CTRL + C` or or  `CONTROL + C` in the terminal window.

# Completion

Congratulations, you've successfully completed Lab 6! You can move on to [Lab 7: Active MQ Broker Statistics](/labs/lab-7.md)

[Return to the Workshop Landing page](/README.md)