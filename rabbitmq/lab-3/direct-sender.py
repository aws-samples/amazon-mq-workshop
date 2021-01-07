import ssl
import pika
import logging
import time
import sys
import signal
import argparse


count = 0


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", help="RabbitMQ host")
parser.add_argument("-P", "--port", help="RabbitMQ port")
parser.add_argument("-u", "--user", help="RabbitMQ user")
parser.add_argument("-p", "--password", help="RabbitMQ password")
parser.add_argument("-e", "--exchange", help="Exchange name")
parser.add_argument("-r", "--routing_key", help="Routing key")

# Read arguments from the command line
args = parser.parse_args()


if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

def connect_machine(host,port,exchange,user,password):
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
                        exchange_type='direct', durable='True')
 
    return conn, ch


def disconnect_machine(connection):
    connection.close()

def signal_handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    disconnect_machine(connection)
    exit(0)
    


connection, channel = connect_machine(args.host,args.port,args.exchange,args.user,args.password)
signal.signal(signal.SIGINT, signal_handler)

while True:
    try:
        body_content = "Message number " + str(count)
        count = count + 1
        
        print('Routing key : %s' %(args.routing_key))
    
        channel.basic_publish(exchange=args.exchange,
                              routing_key=args.routing_key,
                              body=body_content)
    
        # disconnect_machine(connection)
        print(" [x] Sent '{}'".format(body_content))
        time.sleep(1)

    except pika.exceptions.AMQPConnectionError:
        print("Connection was closed, retrying...")
        connection, channel = connect_machine(args.host,args.port,args.exchange,args.user,args.password)
        continue
