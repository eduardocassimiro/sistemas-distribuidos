import grpc
from concurrent import futures
import time

# Importanto arquivos gerados
import smart_portao_pb2
import smart_portao_pb2_grpc

class PortaoServicer(smart_portao_pb2_grpc.PortaoServicer):

    def abrirPortao(self, request, context):
        response = smart_portao_pb2.PortaoStatus()
        # Vai apresentar ligada
        print(response)
        response.status = 1
        print(self.request.status)
        return response

    def fecharPortao(self, request, context):
        response = smart_portao_pb2.PortaoStatus()
        print(response)
        # -1 Vai representar desligada
        response.status = 0
        return response

# Criando o servidor gRPC
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

smart_portao_pb2_grpc.add_PortaoServicer_to_server(
        PortaoServicer(), server)

# Escutando a porta 50053
print('Iniciando servidor. Ouvindo na porta 50053')
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