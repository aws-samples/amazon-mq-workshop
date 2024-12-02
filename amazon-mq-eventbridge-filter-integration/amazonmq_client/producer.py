import ssl
import stomp

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str, help="AmazonMQ Host URL")
parser.add_argument("username", type=str, help="Username")
parser.add_argument("password", type=str, help="Password")

args = parser.parse_args()

conn = stomp.Connection11(
    host_and_ports=[
        (args.host, "61614")
    ]
)
conn.set_ssl(
    for_hosts=[
        (args.host, "61614")
    ],
    ssl_version=ssl.PROTOCOL_TLSv1_2,
)
conn.connect(args.username, args.password, wait=True)
conn.send(
    body="Message for Application_A",
    destination="/queue/EVENT_BRIDGE_INBOUND",
    headers={
        "message_type": "new",
        "country": "canada",
        "description": "sending to APPLICATION_A",
    },
)
conn.send(
    body="Message for Application_B",
    destination="/queue/EVENT_BRIDGE_INBOUND",
    headers={
        "message_type": "new",
        "country": "canada",
        "description": "sending to APPLICATION_B",
    },
)
conn.send(
    body="Message for Application_C",
    destination="/queue/EVENT_BRIDGE_INBOUND",
    headers={
        "message_type": "new",
        "country": "canada",
        "description": "sending to APPLICATION_C",
    },
)
conn.send(
    body="Message for Application_D",
    destination="/queue/EVENT_BRIDGE_INBOUND",
    headers={
        "message_type": "new",
        "country": "canada",
        "description": "sending to APPLICATION_D",
    },
)
conn.send(
    body="Message for Application_E",
    destination="/queue/EVENT_BRIDGE_INBOUND",
    headers={
        "message_type": "new",
        "country": "canada",
        "description": "sending to APPLICATION_E",
    },
)
conn.disconnect()

