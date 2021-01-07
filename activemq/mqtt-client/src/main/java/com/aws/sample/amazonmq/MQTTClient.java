package com.aws.sample.amazonmq;

import java.nio.charset.StandardCharsets;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.UUID;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagement;
import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagementClientBuilder;
import com.amazonaws.services.simplesystemsmanagement.model.GetParameterRequest;
import com.amazonaws.services.simplesystemsmanagement.model.GetParameterResult;

class WrapInt {
    public int v = 0;
}

public class MQTTClient {

    private static final DateFormat df = new SimpleDateFormat("dd.MM.yyyy HH:mm:ss.S");

    public static void main(String[] args) throws Exception {
        CommandLine cmd = parseAndValidateCommandLineArguments(args);
        final WrapInt count = new WrapInt();
        final long ds = System.currentTimeMillis();

        final int interval = Integer.parseInt(cmd.getOptionValue("interval", "1000"));
        String name = cmd.getOptionValue("name", UUID.randomUUID().toString());
        registerShutdownHook(count, ds, interval);

        String[] url = cmd.getOptionValue("url").split("://");
        MqttClient client = null;
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
            MqttConnectOptions options = new MqttConnectOptions();
            options.setCleanSession(false);
            options.setAutomaticReconnect(true);
            options.setUserName(user);
            options.setPassword(password.toCharArray());
            client = new MqttClient("ssl://" + url[1], name, new MemoryPersistence());

            String mqttTopic = cmd.getOptionValue("destination");
            if (cmd.getOptionValue("mode").contentEquals("sender")) {
                sendMessages(client, options, mqttTopic, name, interval, count);
            } else {
                receiveMessages(client, options, mqttTopic);
            }
        } catch (Exception ex) {
            System.out.println(String.format("Error: %s", ex.getMessage()));
            System.exit(1);
        }
    }

    private static void sendMessages(MqttClient client, MqttConnectOptions options, String destination, String name, int interval, WrapInt count) throws Exception {
        client.connect(options);
        System.out.println(String.format("Successfully connected to %s", client.getServerURI()));

        while (true) {
            count.v++;

            String message = String.format("[topic://%s] [%s] Message number %s", destination.replace('/', '.'), name, count.v);
            client.publish(destination, message.getBytes(StandardCharsets.UTF_8), 1, false);

            if (interval > 0) {
                System.out.println(String.format("%s - Sender: sent '%s'", df.format(new Date()), message));
                try {
                    Thread.sleep(interval);
                } catch (InterruptedException e) {
                    System.out.println(String.format("Error: %s", e.getMessage()));
                    System.exit(1);
                }
            }
        }
    }

    private static void receiveMessages(final MqttClient client, final MqttConnectOptions options,final  String destination) throws Exception {
        new Thread(new Runnable() {
            public void run() {
                try {
                    client.setCallback(new MqttCallback() {
                        public void connectionLost(Throwable cause) {
                        }
    
                        public void messageArrived(String topic, MqttMessage message) throws Exception {
                            System.out.println(String.format("%s - Receiver: received '%s'", df.format(new Date()), new String(message.getPayload())));
                        }
    
                        public void deliveryComplete(IMqttDeliveryToken token) {
                        }
                    });
                    client.connect(options);
                    System.out.println(String.format("Successfully connected to %s", client.getServerURI()));
    
                    client.subscribe(destination);
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
        }).start();
    }

    private static CommandLine parseAndValidateCommandLineArguments(String[] args) throws ParseException {
        Options options = new Options();
        options.addOption("help", false, "Print the help message.");
        options.addOption("url", true, "The broker connection url.");
        options.addOption("user", true, "The user to connect to the broker.");
        options.addOption("password", true, "The password for the user.");
        options.addOption("mode", true, "Whether to act as 'sender' or 'receiver'");
        options.addOption("destination", true, "The name of the queue or topic");
        options.addOption("name", true, "The name of the sender");
        options.addOption("interval", true, "The interval in msec at which messages are generated. Default 1000");
        CommandLineParser parser = new DefaultParser();
        CommandLine cmd = parser.parse(options, args);

        if (cmd.hasOption("help")) {
            printUsage(options);
        }

        if (!(cmd.hasOption("url") && cmd.hasOption("mode") && cmd.hasOption("destination"))) {
            printUsage(options);
        }

        return cmd;
    }

    private static void printUsage(Options options) throws ParseException {
        HelpFormatter formatter = new HelpFormatter();
        formatter.printHelp( "java -jar mqtt-client.jar -url <url> -user <user> -password <password> -mode <sender|receiver> -destination <destination> [-name <name> -interval <interval>]", options);
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