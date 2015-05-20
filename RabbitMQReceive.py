__author__ = 'altug'

import logging
logging.basicConfig()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='url')

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='url',
                      no_ack=True)

channel.start_consuming()
