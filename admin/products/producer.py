# 
import pika
import json


params = pika.URLParameters('amqps://hsfvjmxb:NnXl1xRXc4nx5YPeGhalfOkCm6S6O0Hx@possum.lmq.cloudamqp.com/hsfvjmxb')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='main',
        body=json.dumps(body),
        properties=properties
        )