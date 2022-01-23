import grpc
from concurrent import futures
import time
import serial

# Importanto arquivos gerados
import smart_portao_pb2
import smart_portao_pb2_grpc

ser2 = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1.8)

class PortaoServicer(smart_portao_pb2_grpc.PortaoServicer):

    def abrirPortao(self, request, context):
        response = smart_portao_pb2.PortaoStatus()
        # 1 Vai apresentar aberto
        ser2.write(str.encode('z'))
        response.status = 1
        print("Portão Aberto")
        return response

    def fecharPortao(self, request, context):
        response = smart_portao_pb2.PortaoStatus()
        # 0 Vai apresentar Fechado
        ser2.write(str.encode('x'))
        response.status = 0
        print("Portão Fechado")
        return response

# Criando o servidor gRPC
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

smart_portao_pb2_grpc.add_PortaoServicer_to_server(
        PortaoServicer(), server)

# Escutando a porta 50053
print('Iniciando servidor X. Ouvindo na porta 50053.')
server.add_insecure_port('[::]:50053')
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