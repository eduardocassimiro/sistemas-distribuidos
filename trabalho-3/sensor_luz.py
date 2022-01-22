import pika
import sys
from random import randrange,random
import time
import smart_obj_pb2 as SmartObject

# --- Definição da classe serializável do sensor

sensor = SmartObject.SmartObject()
sensor.id = 1
sensor.name = 'R2D2-TEMP'
sensor.type = SmartObject.TypeObject.Value('SENSOR')

# --- Conexão RabbitMQ

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='luz_log', exchange_type='fanout')

#device_info = {'id': 1,'name': 'TEMP', 'type': 'sensor'}
#message = {'info': device_info,'data':0}

# --- Enviando os dados

while(True):
    sensor.data = str(randrange(500,550)) # Gera um número aleatório
    message = sensor.SerializeToString(sensor) # Serializa todo o objeto para string
    channel.basic_publish(exchange='luz_log', routing_key='', body=message) # enviar para fila
connection.close()
