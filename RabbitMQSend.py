__author__ = 'altug'

import logging
logging.basicConfig()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='url')

channel.basic_publish(exchange='',#Kuyruk ismine gore convert edicek mesaji yollayacak bos default.
                      routing_key='url',
                      body='FOTO URL !')

print " [x] Sent 'Burada URL olacak !'"

connection.close()

