__author__ = 'altug'

import logging
logging.basicConfig()
import pika
import Main

connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='idobj')

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    mainInstance = Main.Main
    mainInstance.jsonStart()


channel.basic_consume(callback,
                      queue='idobj',
                      no_ack=True)


channel.start_consuming()