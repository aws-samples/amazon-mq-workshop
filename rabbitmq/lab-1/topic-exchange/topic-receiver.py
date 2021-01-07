import ssl
import pika
import logging
import time
import sys
import argparse

message_count = 10
count = 0


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", help="RabbitMQ host")
parser.add_argument("-P", "--port", help="RabbitMQ port")
parser.add_argument("-u", "--user", help="RabbitMQ user")
parser.add_argument("-p", "--password", help="RabbitMQ password")
parser.add_argument("-e", "--exchange", help="Exchange name")
parser.add_argument("-b", "--binding_key", help="Binding key")
parser.add_argument("-q", "--queue",help="Queue to consume")

# Read arguments from the command line
args = parser.parse_args()



if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

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
                        exchange_type='topic', durable='True')
                        
    ch.queue_declare(queue=queue,durable=True, arguments=argument_list)

    ch.queue_bind(queue,exchange, routing_key=args.binding_key)
 
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



connection, channel = connect_machine(args.host,args.port,args.exchange,args.queue,args.user,args.password,args.binding_key)

channel.basic_consume(args.queue, on_message, auto_ack=False)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
