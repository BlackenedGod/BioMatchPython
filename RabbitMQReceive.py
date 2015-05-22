__author__ = 'altug'

import logging
logging.basicConfig()
import pika
import ParseJSON
import threading as th

connection = pika.BlockingConnection(pika.ConnectionParameters('188.166.67.19'))

channel = connection.channel()

channel.queue_declare(queue='idobj')

parseJSONInstance = ParseJSON.parseJSON()

lock = th.RLock()

def callback(ch, method, properties, body):
    with lock:
        print " [x] Received %r" % (body,)
        parseJSONInstance.downloadSpecificObject(body)
        lock.release()


channel.basic_consume(callback,
                      queue='idobj',
                      no_ack=True)

channel.start_consuming()
