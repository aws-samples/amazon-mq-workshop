import ssl
import pika
import logging
import time
import sys

message_count = 10
count = 0


def connect_machine(host,port,exchange,queue,user,password,binding_key):
    logging.basicConfig(level=logging.INFO)
    credentials = pika.PlainCredentials(user, password)
    argument_list = {'x-queue-master-locator': 'random'}
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.verify_mode = ssl.CERT_NONE
    # context.load_verify_locations('/Users/mithumal/Projects/AmazonMQ/rabbitmq-stuff/certs/certificate.pem')

    cp = pika.ConnectionParameters(port=port, host=host,
                                   credentials=credentials, ssl_options=pika.SSLOptions(context))

    conn = pika.BlockingConnection(cp)

    ch = conn.channel()
    ch.exchange_declare(exchange=exchange,
                        exchange_type='fanout', durable='True')
                        
    ch.queue_declare(queue=queue,durable=True, arguments=argument_list)

    ch.queue_bind(queue,exchange, routing_key='')
 
    return conn, ch


def disconnect_machine(connection):
    connection.close()



def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

if len(sys.argv) < 5:
    sys.exit("usage: fanout-receiver.py host port user password exchange binding_key queue [vhost]")
    
print("Argument List:", str(sys.argv))

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
exchange = sys.argv[5]
binding_key = sys.argv[6]
queue = sys.argv[7]

connection, channel = connect_machine(host,port,exchange,queue,user,password,binding_key)

channel.basic_consume(queue, on_message, auto_ack=False)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
