__author__ = 'altug'

import logging
logging.basicConfig()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='id')

channel.basic_publish(exchange='',#Kuyruk ismine gore convert edicek mesaji yollayacak bos default.
                      routing_key='id',
                      body='FOTO URL !')

print " [x] Sent 'Burada URL olacak !'"

connection.close()

