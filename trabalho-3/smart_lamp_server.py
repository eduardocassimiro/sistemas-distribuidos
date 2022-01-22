import grpc
from concurrent import futures
import time

# Importanto arquivos gerados
import smart_lamp_pb2
import smart_lamp_pb2_grpc

class LampadaServicer(smart_lamp_pb2_grpc.LampadaServicer):

    def ligarLampada(self, request, context):
        response = smart_lamp_pb2.LampadaStatus()
        # Vai apresentar ligada
        response.status = 1
        return response

    def desligarLampada(self, request, context):
        response = smart_lamp_pb2.LampadaStatus()
        # -1 Vai representar desligada
        response.status = 0
        return response

# Criando o servidor gRPC
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

smart_lamp_pb2_grpc.add_LampadaServicer_to_server(
        LampadaServicer(), server)

# Escutando a porta 50051
print('Iniciando servidor. Ouvindo na porta 50051.')
server.add_insecure_port('[::]:50051')
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