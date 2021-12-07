import socket
import json

print('--- Calculadora UDP (Servidor) ---')

# Criando um socket
i = 0
HOST = ''
PORT = 6789
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
skt.bind((HOST, PORT))

while True:
    i += 1
    print('Esperando operação ' + str(i))
    result = 'Calculo inválido ' # Mensagem de verificação de status
    
    # Receber pacote
    data, address = skt.recvfrom(1024)
    host_client, port = address
    data_json = json.loads(data)
    
    # Mostrar dados do cliente e operação recebida
    print('| Cliente: '+str(host_client)+ ' - Porta: '+str(port))
    print('| Operação: '+ data_json['n1'] + data_json['op'] + data_json['n2'])
    
    # Transformar valores recebidos em inteiro
    try:
        data_json['n1'] = int(data_json['n1'])
        data_json['n2'] = int(data_json['n2'])
        
        # Avaliar operador
        if(data_json['op'] == '+'):
            result = data_json['n1'] + data_json['n2']
        elif(data_json['op'] == '-'):
            result = data_json['n1'] - data_json['n2']
        elif(data_json['op'] == '/'):
            result = data_json['n1'] / data_json['n2']
        elif(data_json['op'] == '*'):
            result = data_json['n1'] * data_json['n2']
        else:        
            result = result + '| Operador inválido'
    except:
        result = result + '| Entrada inválida de números'
        print('|| '+result)
        
    # Devolver resposta para o cliente
    try:
        skt.sendto(bytes(str(result), 'utf-8'), address)   
    except:
        print("Tempo excedido")
skt.close()