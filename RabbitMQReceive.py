__author__ = 'altug'

import logging
logging.basicConfig()
import pika
from ParseJSON import parseJSON


connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='objand')

def callback(ch, method, properties, body):
    print " [x] Received %r" % body
    #connection.close()
    #mainInstance = Main.Main()
    parseJSON().downloadSpecificObject(body)
    #maskingClass(retArray[0], retArray[1])


channel.basic_consume(callback,
                      queue='objand',
                      no_ack=True)

channel.start_consuming()
