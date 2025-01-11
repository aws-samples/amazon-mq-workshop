package org.example.activemq;

import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

// import java.util.logging.LogManager;
// import java.util.logging.Logger;
// import java.util.logging.Level;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class SQSConsumer {
    private final SqsClient sqsClient;
    private final String region;
    private final String accountId;
    private static final int ITERATIONS = 300;
    private static final long SLEEP_DURATION = 10; // 10 milliseconds
    int totalMessages = 0;
    
    static {
        // Configure logging to suppress debug messages
        // LogManager.getLogManager().reset();
        // Logger rootLogger = LogManager.getLogManager().getLogger("");
        // rootLogger.setLevel(Level.INFO);
        
        // // Suppress AWS SDK debug logging
        // Logger.getLogger("software.amazon.awssdk").setLevel(Level.OFF);
        // Logger.getLogger("org.apache.http").setLevel(Level.OFF);
        // Logger.getLogger("com.amazonaws").setLevel(Level.OFF);
        // Logger.getLogger("software.amazon.awssdk.requestId").setLevel(Level.OFF);
        // Logger.getLogger("software.amazon.awssdk.auth.signer.Aws4Signer").setLevel(Level.OFF);
        // Logger.getLogger("software.amazon.awssdk").setLevel(Level.OFF);
        // Logger.getLogger("software.amazon.awssdk.auth").setLevel(Level.OFF);
        // Logger.getLogger("software.amazon.awssdk.auth.signer").setLevel(Level.OFF);
    

    }

    public SQSConsumer() {
        this.sqsClient = SqsClient.create();
        this.region = System.getenv("AWS_REGION");
        this.accountId = System.getenv("AWS_ACCOUNT");
    }

    public void purgeQueue(String queueUrl) {
        try {
            PurgeQueueRequest purgeRequest = PurgeQueueRequest.builder()
                .queueUrl(queueUrl)
                .build();
            
            sqsClient.purgeQueue(purgeRequest);
            System.out.println("Successfully purged queue: " + queueUrl);
        } catch (Exception e) {
            System.err.println("Error purging queue " + queueUrl + ": " + e.getMessage());
        }
    }

    public int getQueueAttributes(String queueUrl) {
        try {
            GetQueueAttributesRequest request = GetQueueAttributesRequest.builder()
                .queueUrl(queueUrl)
                .attributeNames(QueueAttributeName.APPROXIMATE_NUMBER_OF_MESSAGES)
                .build();

            GetQueueAttributesResponse response = sqsClient.getQueueAttributes(request);
            return Integer.parseInt(response.attributes().get(QueueAttributeName.APPROXIMATE_NUMBER_OF_MESSAGES));
        } catch (Exception e) {
            System.err.println("Error getting attributes for queue " + queueUrl + ": " + e.getMessage());
            return 0;
        }
    }

    private String constructQueueUrl(String queueName) {
        return String.format("https://sqs.%s.amazonaws.com/%s/%s", region, accountId, queueName);
    }

    public void processQueues() {
        List<String> queueNames = List.of(
            "NEW_APPLICATION_A_CANADA",
            "NEW_APPLICATION_B_CANADA",
            "NEW_APPLICATION_C_CANADA",
            "NEW_APPLICATION_D_CANADA",
            "NEW_APPLICATION_E_CANADA"
        );

        // First purge all queues
        for (String queueName : queueNames) {
            purgeQueue(constructQueueUrl(queueName));
        }

        // Monitor message counts
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        
        for (int i = 0; i < ITERATIONS; i++) {
            totalMessages = 0;
            
            // Get attributes for each queue and sum the messages
            for (String queueName : queueNames) {
                String queueUrl = constructQueueUrl(queueName);
                totalMessages += getQueueAttributes(queueUrl);
            }

            // Print current timestamp and total message count
            String timestamp = LocalDateTime.now().format(formatter);
            if (totalMessages == 10000) {
                System.out.println(timestamp + " SQS Consumer Final Total Messages :" + totalMessages);
                System.exit(0);
            }
            else {
                System.out.println(timestamp + " SQS Consumer Total Messages :" + totalMessages);
            }

            try {
                Thread.sleep(SLEEP_DURATION);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    public static void main(String[] args) {
        SQSConsumer consumer = new SQSConsumer();
        consumer.processQueues();
    }

    // Method to close the SQS client
    public void close() {
        if (sqsClient != null) {
            sqsClient.close();
        }
    }
}
