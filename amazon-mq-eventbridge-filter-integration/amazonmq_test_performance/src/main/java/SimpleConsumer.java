package org.fusebyexample.activemq;

import java.util.Arrays;
import java.util.List;
import javax.jms.*;
import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.apache.commons.cli.*;

class ConsumerThread implements Runnable {
    private Thread t;
    private static final Logger log = LoggerFactory.getLogger(SimpleConsumer.class);
    private static final int MESSAGE_TIMEOUT_MILLISECONDS = 1000;

    private String queue;
    private String brokerUrl;
    private String username;
    private String password;

    ConsumerThread(String country, String app, String brokerUrl, String username, String password) throws JMSException {
        this.queue = "NEW_" + app + "_" + country;
        this.brokerUrl = brokerUrl;
        this.username = username;
        this.password = password;
    }

    public void run() {
        System.out.println("Thread is running...");
        try {
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerUrl);
            connectionFactory.setUserName(username);
            connectionFactory.setPassword(password);
            
            ActiveMQConnection connection = (ActiveMQConnection) connectionFactory.createConnection();
            connection.setCheckForDuplicates(true);
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queue);
            
            log.info("Start consuming messages from " + destination.toString() + " with " + 
                    MESSAGE_TIMEOUT_MILLISECONDS + "ms timeout");

            MessageConsumer consumer = session.createConsumer(destination);

            while (true) {
                Message message = consumer.receive();
                if (message != null && message instanceof TextMessage) {
                    String text = ((TextMessage) message).getText();
                }
            }
        } catch (Exception t) {
            t.printStackTrace();
        }
    }

    public void start() {
        System.out.println("Starting consumer for Queue " + queue);
        if (t == null) {
            t = new Thread(this, queue);
            t.start();
        }
    }
}

public class SimpleConsumer {
    public static void main(String[] args) throws InterruptedException, JMSException {
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
            formatter.printHelp("SimpleConsumer", options);
            System.exit(1);
        }

        String brokerUrl = cmd.getOptionValue("broker-url");
        String username = cmd.getOptionValue("username");
        String password = cmd.getOptionValue("password");

        List<String> countryList = Arrays.asList("canada"
            //, "US", "UK"
        );
        List<String> appList = Arrays.asList("Application_A",
            "Application_B", "Application_C", "Application_D", "Application_E"
        );

        for (String cntry : countryList) {
            for (String app : appList) {
                new ConsumerThread(
                    cntry.toUpperCase(), 
                    app.toUpperCase(), 
                    brokerUrl,
                    username,
                    password
                ).start();
            }
        }
    }
}
