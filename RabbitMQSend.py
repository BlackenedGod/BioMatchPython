__author__ = 'altug'

import logging
logging.basicConfig()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='idob')

channel.basic_publish(exchange='',#Kuyruk ismine gore convert edicek mesaji yollayacak bos default.
                      routing_key='idob',
                      body='FOTO URL !')

print " [x] Sent 'Burada URL olacak !'"

connection.close()

