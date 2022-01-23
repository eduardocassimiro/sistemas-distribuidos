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

channel.exchange_declare(exchange='camp_log', exchange_type='fanout')

#device_info = {'id': 1,'name': 'TEMP', 'type': 'sensor'}
#message = {'info': device_info,'data':0}

# --- Enviando os dados
cont = 1
while(True):
    if cont == 5:
        sensor.data = '1'
        cont = 0
    else:
        sensor.data = '0'
        cont += 1

    message = sensor.SerializeToString(sensor) # Serializa todo o objeto para string
    channel.basic_publish(exchange='camp_log', routing_key='', body=message) # enviar para fila
    time.sleep(3)
connection.close()
