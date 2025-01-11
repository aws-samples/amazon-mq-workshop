package org.example.activemq;

import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.command.ActiveMQQueue;
import org.apache.commons.cli.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
// import org.apache.log4j.Logger;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import javax.jms.*;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class AMQConsumerThread implements Runnable {
    private static final Logger log = LoggerFactory.getLogger(AMQConsumer.class);
    // private final Logger log = Logger.getLogger(getClass());
    
    private static final int MESSAGE_TIMEOUT_MILLISECONDS = 1000;
    
    private final String queue;
    private final String brokerUrl;
    private final String username;
    private final String password;
    private final Thread thread;
    private volatile boolean isRunning = true;
    
    AMQConsumerThread(String country, String app, String brokerUrl, String username, String password) {
        this.queue = "NEW_" + app + "_" + country;
        this.brokerUrl = brokerUrl;
        this.username = username;
        this.password = password;
        this.thread = new Thread(this, queue);
    }

    private ActiveMQConnectionFactory createConnectionFactory() {
        ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerUrl);
        connectionFactory.setUserName(username);
        connectionFactory.setPassword(password);
        return connectionFactory;
    }

    private void purgeQueue(ActiveMQConnection connection, String queueName) {
        Session session = null;
        try {
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            ActiveMQQueue queue = new ActiveMQQueue(queueName);
            
            try {
                connection.destroyDestination(queue);
                log.info("Successfully purged queue: {}", queueName);
            } catch (JMSException e) {
                log.warn("Could not purge queue {}: {}", queueName, e.getMessage());
                
                MessageConsumer consumer = null;
                try {
                    consumer = session.createConsumer(queue);
                    while (consumer.receive(100) != null) {
                        // Drain the queue
                    }
                    log.info("Successfully drained queue: {}", queueName);
                } finally {
                    if (consumer != null) {
                        consumer.close();
                    }
                }
            }
        } catch (JMSException e) {
            log.error("Error while purging queue {}", queueName, e);
        } finally {
            if (session != null) {
                try {
                    session.close();
                } catch (JMSException e) {
                    log.error("Error closing purge session", e);
                }
            }
        }
    }

    private void processMessages(MessageConsumer consumer) throws JMSException {
        while (isRunning) {
            Message message = consumer.receive(MESSAGE_TIMEOUT_MILLISECONDS);
            if (message instanceof TextMessage) {
                String text = ((TextMessage) message).getText();
                // log.debug("Received message: {}", text);

            }
        }
    }

    @Override
    public void run() {
        log.info("Starting consumer thread for queue: {}", queue);
        ActiveMQConnection connection = null;
        Session session = null;
        MessageConsumer consumer = null;

        try {
            connection = (ActiveMQConnection) createConnectionFactory().createConnection();
            connection.setCheckForDuplicates(true);
            connection.start();

            // Purge the queue before starting to consume
            purgeQueue(connection, queue);

            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queue);
            
            log.info("Start consuming messages from {} with {}ms timeout", 
                    destination.toString(), MESSAGE_TIMEOUT_MILLISECONDS);

            consumer = session.createConsumer(destination);
            processMessages(consumer);

        } catch (JMSException e) {
            log.error("Error in consumer thread for queue {}", queue, e);
        } catch (Exception e) {
            log.error("Unexpected error in consumer thread for queue {}", queue, e);
        } finally {
            try {
                if (consumer != null) consumer.close();
                if (session != null) session.close();
                if (connection != null) connection.close();
            } catch (JMSException e) {
                log.error("Error closing resources", e);
            }
        }
    }

    public void start() {
        log.info("Starting consumer for Queue {}", queue);
        thread.start();
    }

    public void stop() {
        isRunning = false;
        thread.interrupt();
    }

    public boolean isRunning() {
        return isRunning && thread.isAlive();
    }
}

class AMQConsumerStatsThread implements Runnable {
    private static final Logger log = LoggerFactory.getLogger(AMQConsumer.class);
    // private final Logger log = Logger.getLogger(getClass());
    private static final int MESSAGE_TIMEOUT_MILLISECONDS = 1000;
    private static final int TARGET_MESSAGE_COUNT = 10000;
    private static final int POLLING_INTERVAL = 1000;
    private static final String QUEUE_STATS_PREFIX = "ActiveMQ.Statistics.Destination.NEW_APPLICATION_";
    private static final String[] APPLICATIONS = {"A", "B", "C", "D", "E"};

    private final String queue;
    private final ConnectionFactory connectionFactory;
    private final Thread thread;
    private volatile boolean isRunning = true;
    private int totalMessages = 0;

    private static class QueueStats {
        final Queue replyQueue;
        final MessageConsumer consumer;
        final Queue queryQueue;

        QueueStats(Queue replyQueue, MessageConsumer consumer, Queue queryQueue) {
            this.replyQueue = replyQueue;
            this.consumer = consumer;
            this.queryQueue = queryQueue;
        }
    }

    AMQConsumerStatsThread(String country, String app, String brokerUrl, String username, String password) {
        this.queue = "NEW_" + app + "_" + country;
        this.connectionFactory = createConnectionFactory(brokerUrl, username, password);
        this.thread = new Thread(this, queue);
    }

    private ActiveMQConnectionFactory createConnectionFactory(String brokerUrl, String username, String password) {
        ActiveMQConnectionFactory factory = new ActiveMQConnectionFactory(brokerUrl);
        factory.setUseAsyncSend(true);
        factory.setUserName(username);
        factory.setPassword(password);
        return factory;
    }

    private void purgeQueue(Connection connection, String queueName) {
        Session session = null;
        try {
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            ActiveMQQueue queue = new ActiveMQQueue(queueName);
            
            if (connection instanceof ActiveMQConnection) {
                try {
                    ((ActiveMQConnection) connection).destroyDestination(queue);
                    log.info("Successfully purged stats queue: {}", queueName);
                } catch (JMSException e) {
                    log.warn("Could not purge stats queue {}: {}", queueName, e.getMessage());
                }
            }
        } catch (JMSException e) {
            log.error("Error while purging stats queue {}", queueName, e);
        } finally {
            if (session != null) {
                try {
                    session.close();
                } catch (JMSException e) {
                    log.error("Error closing purge session", e);
                }
            }
        }
    }

    private List<QueueStats> initializeQueues(Session session) throws JMSException {
        List<QueueStats> queueStats = new ArrayList<>();
        for (String app : APPLICATIONS) {
            Queue replyTo = session.createTemporaryQueue();
            MessageConsumer consumer = session.createConsumer(replyTo);
            Queue queryQueue = session.createQueue(QUEUE_STATS_PREFIX + app + "_CANADA");
            queueStats.add(new QueueStats(replyTo, consumer, queryQueue));
        }
        return queueStats;
    }

    private void processQueueMessages(MessageProducer producer, Message msg, List<QueueStats> queueStats) throws JMSException {
        totalMessages = 0;
        for (QueueStats stats : queueStats) {
            msg.setJMSReplyTo(stats.replyQueue);
            producer.send(stats.queryQueue, msg);
            MapMessage reply = (MapMessage) stats.consumer.receive(MESSAGE_TIMEOUT_MILLISECONDS);
            if (reply != null) {
                totalMessages += reply.getLong("dequeueCount");
            }
        }
    }

    // Monitor message counts
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    
    private void logMessageCount() {
        String timestamp = LocalDateTime.now().format(formatter);
        String message = String.format("%s %s Active MQ Consumer Messages: %d", 
            timestamp, 
            totalMessages == TARGET_MESSAGE_COUNT ? "Final Total" : "Total", 
            totalMessages);
        System.out.println(message);
    }

    @Override
    public void run() {
        log.info("Starting consumer thread for queue: {}", queue);
        Connection connection = null;
        Session session = null;
        MessageProducer producer = null;
        List<QueueStats> queueStats = null;

        try {
            connection = connectionFactory.createConnection();
            connection.start();
            
            // Purge all queues before starting
            for (String app : APPLICATIONS) {
                String queueName = QUEUE_STATS_PREFIX + app + "_CANADA";
                purgeQueue(connection, queueName);
            }

            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            producer = session.createProducer(null);
            
            queueStats = initializeQueues(session);
            Message msg = session.createMessage();

            while (isRunning) {
                try {
                    processQueueMessages(producer, msg, queueStats);
                    logMessageCount();

                    if (totalMessages == TARGET_MESSAGE_COUNT) {
                        isRunning = false;
                        break;
                    }

                    Thread.sleep(POLLING_INTERVAL);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    log.error("Thread interrupted", e);
                    break;
                } catch (JMSException e) {
                    log.error("Error processing messages", e);
                    break;
                }
            }
        } catch (JMSException e) {
            log.error("Fatal error in consumer thread", e);
        } finally {
            try {
                if (queueStats != null) {
                    for (QueueStats stats : queueStats) {
                        if (stats.consumer != null) stats.consumer.close();
                    }
                }
                if (producer != null) producer.close();
                if (session != null) session.close();
                if (connection != null) connection.close();
            } catch (JMSException e) {
                log.error("Error closing resources", e);
            }
        }
    }

    public void start() {
        log.info("Starting consumer statistics for Queue {}", queue);
        thread.start();
    }

    public void stop() {
        isRunning = false;
        thread.interrupt();
    }
}

public class AMQConsumer {
    public static void main(String[] args) throws InterruptedException, JMSException {
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
            formatter.printHelp("AMQConsumer", options);
            System.exit(1);
        }

        String brokerUrl = cmd.getOptionValue("broker-url");
        String username = cmd.getOptionValue("username");
        String password = cmd.getOptionValue("password");

        List<String> countryList = Arrays.asList("CANADA");
        List<String> appList = Arrays.asList(
            "APPLICATION_A",
            "APPLICATION_B", 
            "APPLICATION_C", 
            "APPLICATION_D", 
            "APPLICATION_E"
        );

        for (String country : countryList) {
            for (String app : appList) {
                new AMQConsumerThread(
                    country, 
                    app, 
                    brokerUrl,
                    username,
                    password
                ).start();

                new AMQConsumerStatsThread(
                    country, 
                    app, 
                    brokerUrl,
                    username,
                    password
                ).start();
            }
        }
    }
}
