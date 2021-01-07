package com.aws.sample.amazonmq;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.UUID;

import javax.jms.BytesMessage;
import javax.jms.Connection;
import javax.jms.DeliveryMode;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageListener;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;

import org.apache.activemq.ActiveMQSslConnectionFactory;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagement;
import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagementClientBuilder;
import com.amazonaws.services.simplesystemsmanagement.model.GetParameterRequest;
import com.amazonaws.services.simplesystemsmanagement.model.GetParameterResult;

class WrapInt {
    public int v = 0;
}

public class AmazonMqClient {

    private static final DateFormat df = new SimpleDateFormat("dd.MM.yyyy HH:mm:ss.S");

    public static void main(String[] args) throws JMSException, ParseException {
        CommandLine cmd = parseAndValidateCommandLineArguments(args);
        final WrapInt count = new WrapInt();
        final long ds = System.currentTimeMillis();

        ActiveMQSslConnectionFactory connFact = new ActiveMQSslConnectionFactory(cmd.getOptionValue("url"));
        connFact.setConnectResponseTimeout(10000);
        final int interval = Integer.parseInt(cmd.getOptionValue("interval", "1000"));
        final long ttl = Integer.parseInt(cmd.getOptionValue("ttl", "-1"));
        String name = cmd.getOptionValue("name", UUID.randomUUID().toString());
        int deliveryMode = cmd.hasOption("notPersistent") ? DeliveryMode.NON_PERSISTENT : DeliveryMode.PERSISTENT;
        registerShutdownHook(count, ds, interval);

        try {
            String user = null;
            String password = null;
            String secrets = null;    
            if (cmd.hasOption("user") && cmd.hasOption("password")) {
                user = cmd.getOptionValue("user");
                password = cmd.getOptionValue("password");                
          } else {
                secrets = getUserPassword("MQBrokerUserPassword");
                if (secrets!=null && !secrets.isEmpty()) {
                    user = secrets.split(",")[0];
                    password = secrets.split(",")[1];
                }
            }
            Connection conn = connFact.createConnection(user, password);
            conn.setClientID("AmazonMQWorkshop-" + System.currentTimeMillis());
            conn.start();

            Session session = conn.createSession(false, Session.CLIENT_ACKNOWLEDGE);

            if (cmd.getOptionValue("mode").contentEquals("sender")) {
                if (cmd.getOptionValue("type").contentEquals("queue")) {
                    MessageProducer queueMessageProducer = session.createProducer(session.createQueue(cmd.getOptionValue("destination")));
                    sendMessages(session, queueMessageProducer, ttl, name, interval, deliveryMode, count);
                } else {
                    MessageProducer topicMessageProducer = session.createProducer(session.createTopic(cmd.getOptionValue("destination")));
                    sendMessages(session, topicMessageProducer, ttl, name, interval, deliveryMode, count);
                }
            } else {
                if (cmd.getOptionValue("type").contentEquals("queue")) {
                    MessageConsumer queueConsumer = session.createConsumer(session.createQueue(cmd.getOptionValue("destination")));
                    receiveMessages(session, queueConsumer);
                } else {
                    MessageConsumer topicConsumer = session.createConsumer(session.createTopic(cmd.getOptionValue("destination")));
                    receiveMessages(session, topicConsumer);
                }
            }
        } catch (javax.jms.JMSSecurityException ex) {
            System.out.println(String.format("Error: %s", ex.getMessage()));
            System.exit(1);
        }
    }

    private static void sendMessages(Session session, MessageProducer queueMessageProducer, long ttl, String name, int interval, int deliveryMode, WrapInt count) throws JMSException {
        String destination = queueMessageProducer.getDestination().toString();

        while (true) {
            count.v++;
            String id = UUID.randomUUID().toString();
            TextMessage message = session.createTextMessage(String.format("[%s] [%s] Message number %s", destination, name, count.v));
            message.setJMSMessageID(id);
            message.setJMSCorrelationID(id);
            queueMessageProducer.send(message, deliveryMode, 0, ttl);
            if (interval > 0) {
                System.out.println(String.format("%s - Sender: sent '%s'", df.format(new Date()), message.getText()));
                try {
                    Thread.sleep(interval);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static void receiveMessages(Session session, MessageConsumer consumer) throws JMSException {
        consumer.setMessageListener(new MessageListener() {
            public void onMessage(Message message) {
                try {
                    if (message instanceof TextMessage) {
                        TextMessage msg = (TextMessage) message;
                        System.out.println(String.format("%s - Receiver: received '%s'", df.format(new Date()), msg.getText()));
                    } else if (message instanceof BytesMessage) {
                        BytesMessage msg = (BytesMessage) message;
                        byte[] content = new byte[(int)msg.getBodyLength()];
                        msg.readBytes(content);
                        System.out.println(String.format("%s - Receiver: received '%s'", df.format(new Date()), new String(content)));
                    } else {
                        System.out.println(String.format("%s - Receiver: received '%s'", df.format(new Date()), message));
                    }
                    message.acknowledge();
                } catch (JMSException e) {
                    throw new RuntimeException(e);
                }
            }});
    }

    private static CommandLine parseAndValidateCommandLineArguments(String[] args) throws ParseException {
        Options options = new Options();
        options.addOption("help", false, "Print the help message.");
        options.addOption("url", true, "The broker connection url.");
        options.addOption("user", true, "The user to connect to the broker.");
        options.addOption("password", true, "The password for the user.");
        options.addOption("mode", true, "Whether to act as 'sender' or 'receiver'");
        options.addOption("type", true, "Whether to use a queue or a topic.");
        options.addOption("destination", true, "The name of the queue or topic");
        options.addOption("name", true, "The name of the sender");
        options.addOption("interval", true, "The interval in msec at which messages are generated. Default 1000");
        options.addOption("notPersistent", false, "Send messages in non-persistent mode");
        options.addOption("ttl", true, "The time to live value for the message.");
        CommandLineParser parser = new DefaultParser();
        CommandLine cmd = parser.parse(options, args);

        if (cmd.hasOption("help")) {
            printUsage(options);
        }

        if (!(cmd.hasOption("url") && cmd.hasOption("type") && cmd.hasOption("mode") && cmd.hasOption("destination"))) {
            printUsage(options);
        }

        return cmd;
    }

    private static void printUsage(Options options) throws ParseException {
        HelpFormatter formatter = new HelpFormatter();
        formatter.printHelp( "java -jar amazon-mq-client.jar -url <url> -user <user> -password <password> -mode <sender|receiver> -type <queue|topic> -destination <destination> [-name <name> -interval <interval> -notPersistent]", options);
        System.exit(1);
    }

    private static void registerShutdownHook(final WrapInt count, final long ds, final int interval) {
        Thread shutdown = new Thread(new Runnable(){
            long d = ds;
            double rate_theor = interval > 0 ? 1000.0 / interval : 0;

            public void run() {
                long delta = System.currentTimeMillis() - d;
                System.err.print(String.format("\nMessages: %d Seconds: %f Rate: %f/sec vs %f/sec", count.v, delta/1000.0, 1000.0*count.v/delta, rate_theor));
            }
        });
        Runtime.getRuntime().addShutdownHook(shutdown);
    }
    
    public static String getUserPassword(String key) {
        GetParameterResult parameterResult = AWSSimpleSystemsManagementClientBuilder.defaultClient().getParameter(new GetParameterRequest()
            .withName(key));
        return parameterResult.getParameter().getValue();
    }
}