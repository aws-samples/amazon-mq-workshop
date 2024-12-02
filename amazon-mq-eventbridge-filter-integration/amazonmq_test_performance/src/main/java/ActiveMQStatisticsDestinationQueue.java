package org.fusebyexample.activemq;

import java.time.Instant;
import javax.jms.*;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.ActiveMQSession;
import org.apache.commons.cli.*;

public class ActiveMQStatisticsDestinationQueue {

    public static void main(String[] args) {
        // Define command line options
        Options options = new Options();
        options.addOption(Option.builder("b")
                .longOpt("broker-url")
                .desc("Broker URL (e.g., ssl://hostname:61617)")
                .hasArg()
                .required()
                .build());
        
        options.addOption(Option.builder("u")
                .longOpt("username")
                .desc("Username for authentication")
                .hasArg()
                .required()
                .build());
        
        options.addOption(Option.builder("p")
                .longOpt("password")
                .desc("Password for authentication")
                .hasArg()
                .required()
                .build());

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd = null;

        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("ActiveMQStatisticsDestinationQueue", options);
            System.exit(1);
        }

        String brokerUrl = cmd.getOptionValue("broker-url");
        String username = cmd.getOptionValue("username");
        String password = cmd.getOptionValue("password");

        Connection connection = null;
        try {
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerUrl);
            connectionFactory.setUseAsyncSend(true);
            connectionFactory.setUserName(username);
            connectionFactory.setPassword(password);
            
            connection = connectionFactory.createConnection();
            connection.start();

            ActiveMQSession session = (ActiveMQSession) connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            Queue replyTo1 = session.createTemporaryQueue();
            MessageConsumer consumer1 = session.createConsumer(replyTo1);

            Queue replyTo2 = session.createTemporaryQueue();
            MessageConsumer consumer2 = session.createConsumer(replyTo2);

            Queue replyTo3 = session.createTemporaryQueue();
            MessageConsumer consumer3 = session.createConsumer(replyTo3);

            Queue replyTo4 = session.createTemporaryQueue();
            MessageConsumer consumer4 = session.createConsumer(replyTo4);

            Queue replyTo5 = session.createTemporaryQueue();
            MessageConsumer consumer5 = session.createConsumer(replyTo5);

            MessageProducer producer = session.createProducer(null);

            String queueName1 = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_A_CANADA";
            String queueName2 = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_B_CANADA";
            String queueName3 = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_C_CANADA";
            String queueName4 = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_D_CANADA";
            String queueName5 = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_E_CANADA";

            Queue query1 = session.createQueue(queueName1);
            Queue query2 = session.createQueue(queueName2);
            Queue query3 = session.createQueue(queueName3);
            Queue query4 = session.createQueue(queueName4);
            Queue query5 = session.createQueue(queueName5);

            Message msg = session.createMessage();
            while (true) {
                try {
                    msg.setJMSReplyTo(replyTo1);
                    producer.send(query1, msg);
                    MapMessage reply = (MapMessage) consumer1.receive();

                    msg.setJMSReplyTo(replyTo2);
                    producer.send(query2, msg);
                    MapMessage reply2 = (MapMessage) consumer2.receive();

                    msg.setJMSReplyTo(replyTo3);
                    producer.send(query3, msg);
                    MapMessage reply3 = (MapMessage) consumer3.receive();

                    msg.setJMSReplyTo(replyTo4);
                    producer.send(query4, msg);
                    MapMessage reply4 = (MapMessage) consumer4.receive();

                    msg.setJMSReplyTo(replyTo5);
                    producer.send(query5, msg);
                    MapMessage reply5 = (MapMessage) consumer5.receive();

                    System.out.println(
                            Instant.now() + " Total Messages: " + (reply.getLong("dequeueCount") + 
                            reply2.getLong("dequeueCount") + reply3.getLong("dequeueCount") + 
                            reply4.getLong("dequeueCount") + reply5.getLong("dequeueCount")));

                    Thread.sleep(1000);
                } catch (Exception e) {
                    e.printStackTrace();
                    break;
                }
            }

            producer.close();
            session.close();
        } catch (Exception t) {
            t.printStackTrace();
        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (JMSException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
