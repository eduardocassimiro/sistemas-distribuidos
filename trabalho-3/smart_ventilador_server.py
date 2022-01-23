import grpc
from concurrent import futures
import time
import serial

# Importanto arquivos gerados
import smart_ventilador_pb2
import smart_ventilador_pb2_grpc

ser1 = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1.8)

class VentiladorServicer(smart_ventilador_pb2_grpc.VentiladorServicer):

    def ligarVentilador(self, request, context):
        response = smart_ventilador_pb2.VentiladorStatus()
        # 1 Vai apresentar ligado
        ser1.write(str.encode('a'))
        print(response)
        print("Ventilador Ligado")
        response.status = 1
        return response

    def desligarVentilador(self, request, context):
        response = smart_ventilador_pb2.VentiladorStatus()
        ser1.write(str.encode('s'))
        print(response)
        print("Ventilador Desligado")
        # 0 Vai representar desligado
        response.status = 0
        return response

# Criando o servidor gRPC
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

smart_ventilador_pb2_grpc.add_VentiladorServicer_to_server(
        VentiladorServicer(), server)


# Escutando a porta 50052
print('Iniciando servidor. Ouvindo na porta 50052.')
server.add_insecure_port('[::]:50052')
server.start()

"""
Tratamento de Erro
Se o Server não Iniciar, 
um loop de espera será iniciado.
Caso contrario, para o server.
"""
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)