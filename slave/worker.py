#!/usr/bin/env python

import pika
import time

time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters('LeChateauDL'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] %d*2" % n)
    response = n*2
    time.sleep(5)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [*] Awaiting RPC requests")
channel.start_consuming()
