import socket
import json

print('--- Calculadora UDP (Cliente) ---')

# Números e operador
number1=input('Digite o número 1: ')
operacao = input('Digite a operação: ')
number2=input('Digite o número 2: ')

# Criando um socket
data = {'n1': number1, 'n2': number2, 'op': operacao}
data_json = json.dumps(data)
HOST = "127.0.0.1"
PORT = 6789
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
skt.settimeout(1)

# Enviando dados
try:
    skt.sendto(bytes(data_json, 'utf-8'), (HOST, PORT))
except:
    print("Tempo excedido")
    
# Recebendo resposta
data, address = skt.recvfrom(1024)
server, port = address
data = data.decode('utf-8')
print('Resultado: '+ data)
print('| Servidor: '+str(server)+ ' - Porta: '+str(port))
skt.close()