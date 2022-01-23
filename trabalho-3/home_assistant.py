from http.server import HTTPServer, BaseHTTPRequestHandler
from django.http import response
import grpc
import pika
import threading
# ========================== LAMPS IMPORTS ========================== #
import smart_lamp_pb2_grpc  as lamp
import smart_lamp_pb2 as lampstt
# ======================== VENTILADOR IMPORTS ======================= #
import smart_ventilador_pb2_grpc as vent
import smart_ventilador_pb2 as ventstt
# ========================= PORTAO  IMPORTS ========================= #
import smart_portao_pb2_grpc as porta
import smart_portao_pb2 as portastt
# ========================= Sensors IMPORTS ========================= #
import smart_obj_pb2 as SmartObject
# ========================= Sensors Values ========================= #
luz = 0
temperatura = 0
campainha = 0

# Instânciando um Sensor
sensor = SmartObject.SmartObject()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Fila Temperatura
channel.exchange_declare(exchange='temp_log', exchange_type='fanout')
result_temp = channel.queue_declare(queue='', exclusive=True)
queue_name_temp = result_temp.method.queue
channel.queue_bind(exchange='temp_log', queue=queue_name_temp)

# Fila Luminosidade
channel.exchange_declare(exchange='luz_log', exchange_type='fanout')
result_luz = channel.queue_declare(queue='', exclusive=True)
queue_name_luz = result_luz.method.queue
channel.queue_bind(exchange='luz_log', queue=queue_name_luz)

# Fila Campainha
channel.exchange_declare(exchange='camp_log', exchange_type='fanout')
result_camp = channel.queue_declare(queue='', exclusive=True)
queue_name_camp = result_camp.method.queue
channel.queue_bind(exchange='camp_log', queue=queue_name_camp)

# --- Rotina da fila Temperatura
def callback_temp(ch, method, properties, body):
    sensor.ParseFromString(body)
    # print(' temp:',sensor.data)
    status = str(sensor.data)
    reponse = sensor.data
    global temperatura
    temperatura = status
    # print(status)
    return response

# --- Rotina da fila Luminosidade
def callback_luz(ch, method, properties, body):
    sensor.ParseFromString(body)
    # print('  luz:',sensor.data)
    status = str(sensor.data)
    reponse = sensor.data
    global luz
    luz = status
    # print(status)
    return response

# --- Rotina da fila Campainha
def callback_camp(ch, method, properties, body):
    sensor.ParseFromString(body)
    # print(' camp:',sensor.data)
    status = str(sensor.data)
    reponse = sensor.data
    global campainha
    campainha = status
    # print(status)
    return response
    
# Rotina de Consumo Temp
channel.basic_consume(queue=queue_name_temp, on_message_callback=callback_temp, auto_ack=True)    
# Rotina de Consumo Luz
channel.basic_consume(queue=queue_name_luz, on_message_callback=callback_luz, auto_ack=True)
# Rotina de Consumo Camp
channel.basic_consume(queue=queue_name_camp, on_message_callback=callback_camp, auto_ack=True)

def thread_try():
    try:
        channel.start_consuming()
    except:
        pass


# Start no Consumo das Callbacks

threader = threading.Thread(target=thread_try)
threader.start()
# threader.


# ========================= FUNCTIONS GRPC ========================= # 

def grpc_luz(comm):
    client = grpc.insecure_channel('127.0.0.1:50051') # endereço 
    stub_amigo = lamp.LampadaStub(client)
    status = lampstt.LampadaStatus()

    if comm == 0: # off luz
        response = stub_amigo.desligarLampada(status)
    elif comm == 1:
        response = stub_amigo.ligarLampada(status)
    
    print(response.status)

    if response.status == 0:
        return 'off'
    else:
        return 'on'


def grpc_vent(comm):
    client = grpc.insecure_channel('127.0.0.1:50052') # endereço 
    stub_amigo = vent.VentiladorStub(client)
    status = ventstt.VentiladorStatus()

    if comm == 0: # off ventilador
        response = stub_amigo.desligarVentilador(status)
    elif comm == 1:
        response = stub_amigo.ligarVentilador(status)
    
    print(response.status)

    if response.status == 0:
        return 'off'
    else:
        return 'on'


def grpc_port(comm):
    client = grpc.insecure_channel('127.0.0.1:50053') # endereço 
    stub_amigo = porta.PortaoStub(client)
    status = portastt.PortaoStatus()

    if comm == 0: # fecha portao
        response = stub_amigo.fecharPortao(status)
    elif comm == 1:
        response = stub_amigo.abrirPortao(status)
    
    print(response.status)
    
    if response.status == 0:
        return 'Fechado'
    else:
        return 'Aberto'

class reqs(BaseHTTPRequestHandler): # Servidor http

    def do_GET(self):
        path = self.path

        if path == '/':
            file = open('La_pagina/index.html')

            page = file.read().encode('utf8')

            file.close()

            self.send_response(200, "OK")
            self.send_header("Content-Type","text/html")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(page)

        elif path == '/values':
            global luz
            global temperatura
            global campainha

            values = f'luz:{luz}:temp:{temperatura}:camp:{campainha}'

            self.send_response(200, "OK")
            self.send_header("Content-Type","text/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(values.encode('utf8'))

 

    def do_POST(self):
        # print(self.rfile.read())
        content_len = int(self.headers.get('Content-Length'))   # Tamanho dos dados aqui no header
        path = self.path
        data =  self.rfile.read(content_len).decode('utf8')
        response_x = 'err'
        # -------------------- FIM PRINCIPAIS INFOS ---------------------------------- #
        
        if path == '/luz':
            if data == '0': # desliga luz
                response_x = grpc_luz(0)
            elif data == '1': # liga luz
                response_x = grpc_luz(1)
            self.send_response(200, 'ok')

            
        elif path == '/ventilador':
            if data == '0': # desliga vent
                response_x = grpc_vent(0)
            elif data == '1': #liga vent
                response_x = grpc_vent(1)

            self.send_response(200, 'ok')
            
        elif path == '/portao':
            if data == '0': # desliga vent
                response_x = grpc_port(0)
            elif data == '1': #liga vent
                response_x = grpc_port(1)

            self.send_response(200, 'ok')

        else:
            response_x = 'not find path'
            self.send_response(404, 'not found')
        
        # response_x = 'error'
        # self.send_response(500, 'internal')

        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response_x.encode('utf8'))

#END CLASS

def med_server(hostName, serverPort):

    server = HTTPServer((hostName, serverPort), reqs)
    
    try:
        print(f'starting server on {hostName}:{serverPort}')
        server.serve_forever()
    except:
        print("CLOSING SERVER")
        server.server_close()

    return 0
# END DEF


if __name__ == '__main__':
    med_server('0.0.0.0', 8080)
    try:
        channel.close()
    except:
        print('parando de consumir')



