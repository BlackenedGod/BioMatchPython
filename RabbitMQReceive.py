__author__ = 'altug'

import logging
logging.basicConfig()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='id')

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='id',
                      no_ack=True)

channel.start_consuming()
