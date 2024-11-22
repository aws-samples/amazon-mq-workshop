package com.amazonaws.samples;

import java.util.concurrent.atomic.AtomicLong;

import javax.jms.Connection;
import javax.jms.DeliveryMode;
import javax.jms.JMSException;
import javax.jms.MessageProducer;
import javax.jms.Session;

import org.apache.activemq.ActiveMQSslConnectionFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.ibm.mq.jms.MQQueueConnectionFactory;
import com.ibm.msg.client.wmq.WMQConstants;

public class Bootstrap {

    public static void main(String... args) throws Exception {
        final AtomicLong amazonMQCounter = new AtomicLong();
        final AtomicLong ibmMQCounter = new AtomicLong();

        new Thread(
            new AmazonMQSender(
                System.getenv("amazonMQ.brokerURL"),
                "DEV.QUEUE.1",
                System.getenv("amazonMQ.userName"),
                System.getenv("amazonMQ.password"),
                amazonMQCounter)).start();

        new Thread(
            new IBMMQSender(
                System.getenv("websphereMQ.hostName"),
                System.getenv("websphereMQ.channel"),
                System.getenv("websphereMQ.queueManager"),
                "DEV.QUEUE.2",
                System.getenv("websphereMQ.userName"),
                System.getenv("websphereMQ.password"),
                ibmMQCounter)).start();

        new Thread(new MetricCollector(amazonMQCounter, ibmMQCounter)).start();
    }

    public static class AmazonMQSender implements Runnable {

        private Logger log = LoggerFactory.getLogger(AmazonMQSender.class);
        private ActiveMQSslConnectionFactory connFact;
        private Connection conn;
        private Session session;
        private MessageProducer messageProducer;
        private AtomicLong counter;

        public AmazonMQSender(String url, String destination, String user, String password, AtomicLong counter) throws JMSException {
            this.counter = counter;

            connFact = new ActiveMQSslConnectionFactory(url);
            connFact.setConnectResponseTimeout(10000);

            conn = connFact.createConnection(user, password);
            conn.start();

            session = conn.createSession(false, Session.AUTO_ACKNOWLEDGE);

            messageProducer = session.createProducer(session.createQueue(destination));
            messageProducer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            messageProducer.setTimeToLive(5*1000);
        }

        public void run() {
            while (true) {
                try {
                    messageProducer.send(session.createTextMessage("Message " + counter.incrementAndGet()));

                    // ~ the first minute
                    if (counter.get() < 60) {
                        try {
                            Thread.sleep(1000);
                        } catch (InterruptedException e) {
                        }
                    // ~ the second minutes
                    }
                    if (counter.get() < 660) {
                        try {
                            Thread.sleep(100);
                        } catch (InterruptedException e) {
                        }
                    // ~ the third minute
                    } else if (counter.get() < 1860) {
                        try {
                            Thread.sleep(50);
                        } catch (InterruptedException e) {
                        }
                    // ~ the forth minute
                    } else if (counter.get() < 4300) {
                        try {
                            Thread.sleep(25);
                        } catch (InterruptedException e) {
                        }
                     // ~ the fifth minute
                    } else if (counter.get() < 10300) {
                        try {
                            Thread.sleep(10);
                        } catch (InterruptedException e) {
                        }
                    // after ~ 6 minutes
                    } else {
                        // no delay
                    }
                } catch (JMSException e) {
                    log.info("Received exception {}", e);
                }
            }
        }
    }

    public static class IBMMQSender implements Runnable {

        private Logger log = LoggerFactory.getLogger(IBMMQSender.class);
        private MQQueueConnectionFactory connFact;
        private Connection conn;
        private Session session;
        private MessageProducer messageProducer;
        private AtomicLong counter;

        public IBMMQSender(String host, String channel, String queueManager, String destination, String user, String password, AtomicLong counter) throws JMSException {
            this.counter = counter;

            connFact = new MQQueueConnectionFactory();
            connFact.setHostName(host);
            connFact.setChannel(channel);
            connFact.setPort(1414);
            connFact.setQueueManager(queueManager);
            connFact.setTransportType(1);
            connFact.setStringProperty(WMQConstants.USERID, user);
            connFact.setStringProperty(WMQConstants.PASSWORD, password);

            conn = connFact.createConnection();
            conn.start();

            session = conn.createSession(false, Session.AUTO_ACKNOWLEDGE);

            messageProducer = session.createProducer(session.createQueue(destination));
            messageProducer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            messageProducer.setTimeToLive(5*1000);
        }

        public void run() {
            while (true) {
                try {
                    messageProducer.send(session.createTextMessage("Message " + counter.incrementAndGet()));

                    // ~ the first minute
                    if (counter.get() < 60) {
                        try {
                            Thread.sleep(1000);
                        } catch (InterruptedException e) {
                        }
                    // ~ the second minutes
                    }
                    if (counter.get() < 660) {
                        try {
                            Thread.sleep(100);
                        } catch (InterruptedException e) {
                        }
                    // ~ the third minute
                    } else if (counter.get() < 1860) {
                        try {
                            Thread.sleep(50);
                        } catch (InterruptedException e) {
                        }
                    // ~ the forth minute
                    } else if (counter.get() < 4300) {
                        try {
                            Thread.sleep(25);
                        } catch (InterruptedException e) {
                        }
                     // ~ the fifth minute
                    } else if (counter.get() < 10300) {
                        try {
                            Thread.sleep(10);
                        } catch (InterruptedException e) {
                        }
                    // after ~ 6 minutes
                    } else {
                        // no delay
                    }
                } catch (JMSException e) {
                    log.info("Received exception {}", e);
                }
            }
        }
    }

    public static class MetricCollector implements Runnable {

        private AtomicLong amazonMQCounter;
        private AtomicLong ibmMQCounter;
        private Logger log = LoggerFactory.getLogger(MetricCollector.class);

        public MetricCollector(AtomicLong amazonMQCounter, AtomicLong ibmMQCounter) {
            this.amazonMQCounter = amazonMQCounter;
            this.ibmMQCounter = ibmMQCounter;
        }

        public void run() {
            long previousAmazonMQCounter = 0;
            long currentAmazonMQCounter = 0;
            long previousIBMMQCounter = 0;
            long currentIBMMQCounter = 0;

            while (true) {
                try {
                    Thread.sleep(60 * 1000);
                } catch (InterruptedException e) {
                }

                previousAmazonMQCounter = currentAmazonMQCounter;
                currentAmazonMQCounter = amazonMQCounter.get();
                log.info("Sent {} messages / minute to Amazon MQ...", currentAmazonMQCounter - previousAmazonMQCounter);

                previousIBMMQCounter = currentIBMMQCounter;
                currentIBMMQCounter = ibmMQCounter.get();
                log.info("Sent {} messages / minute to IBM MQ...", currentIBMMQCounter - previousIBMMQCounter);
            }
        }
    }
}