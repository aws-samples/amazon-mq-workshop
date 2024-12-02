package org.fusebyexample.activemq;

import java.util.Arrays;
import java.util.List;
import java.util.Random;
import javax.jms.*;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.ActiveMQSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.apache.commons.cli.*;

public class SimpleProducer {
    private static final Logger LOG = LoggerFactory.getLogger(SimpleProducer.class);
    private static final int NUM_MESSAGES_TO_BE_SENT = 10000;

    public static void main(String[] args) throws ParseException {
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
        
        options.addOption(Option.builder("n")
                .longOpt("num-messages")
                .desc("Number of messages to send (default: 10000)")
                .hasArg()
                .type(Number.class)
                .build());

        String brokerUrl = null;
        String username = null;
        String password = null;
        int numMessages = NUM_MESSAGES_TO_BE_SENT;

        try {
            CommandLineParser parser = new DefaultParser();
            CommandLine cmd = parser.parse(options, args);

            brokerUrl = cmd.getOptionValue("broker-url");
            username = cmd.getOptionValue("username");
            password = cmd.getOptionValue("password");
            
            if (cmd.hasOption("num-messages")) {
                numMessages = ((Number)cmd.getParsedOptionValue("num-messages")).intValue();
            }
        } catch (ParseException e) {
            HelpFormatter formatter = new HelpFormatter();
            formatter.printHelp("SimpleProducer", options);
            throw new ParseException("Error parsing command line arguments: " + e.getMessage());
        }

        Connection connection = null;
        Random rand = new Random();
        List<String> countryList = Arrays.asList("canada");
        List<String> appList = Arrays.asList("Application_A", "Application_B", "Application_C", 
                                           "Application_D", "Application_E");
        String description = "sending to ";

        try {
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerUrl);
            connectionFactory.setUseAsyncSend(true);
            connectionFactory.setUserName(username);
            connectionFactory.setPassword(password);
            
            connection = connectionFactory.createConnection();
            ActiveMQSession session = (ActiveMQSession) connection.createSession(false, 
                                                                              Session.AUTO_ACKNOWLEDGE);

            Destination destination = session.createQueue("ALL_INBOUND");
            Destination destination2 = session.createQueue("EVENT_BRIDGE_INBOUND");

            MessageProducer producer = session.createProducer(destination);
            MessageProducer producer2 = session.createProducer(destination2);

            producer.setDeliveryMode(DeliveryMode.PERSISTENT);
            
            for (int i = 1; i <= numMessages; i++) {
                TextMessage message = session.createTextMessage("Message Body.");
                
                message.setStringProperty("message_type", "new");
                message.setStringProperty("country", 
                        countryList.get(rand.nextInt(countryList.size())));
                message.setStringProperty("description", 
                        description.concat(appList.get(rand.nextInt(appList.size())).toUpperCase()));

                if (i % 100000 == 0) {
                    LOG.info("Sending to destination: " + destination.toString() + 
                            " this text: '" + message.getText());
                }
                
                producer.send(message);
                producer2.send(message);
            }

            producer.close();
            session.close();
            
        } catch (JMSException e) {
            LOG.error("JMS Error", e);
        } catch (Exception e) {
            LOG.error("Error sending message", e);
        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (JMSException e) {
                    LOG.error("Error closing connection", e);
                }
            }
        }
    }
}
