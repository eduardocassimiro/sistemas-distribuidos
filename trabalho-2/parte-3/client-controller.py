import socket
import struct
import sys
import json
import serial


def receive_multicast():
    multicast_group = '224.3.29.71' # Enviar mensagem multicast
    server_address = ('', 10000) # Endereço IP e porta utilizada para o multicast

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket udp

    # Solicita ao sistema operacional para adicionar o socket ao grupo multicast em todas as interfaces
    group = socket.inet_aton(multicast_group) # Converte um endereço IPv4 do formato de string pontilhado
    mreq = struct.pack('4sL', group, socket.INADDR_ANY) # Empacota uma lista de valores em uma representação string do tipo especificado
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1) # Habilita que varios sockets se conectem na mesma porta
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq) # Habilita socket ingressar em um grupo multicast IPv4 em uma interface IPv4 local

    sock.bind(server_address) # Atribuindo porta e o endereço IP explicitamente para
    sock.settimeout(1) # Delay

    try:
        while True:
            print('\nWaiting to receive message by multicast\n')
            data, address = sock.recvfrom(1024) # Espera mensagem
            
            print('Received %s bytes from %s\n' % (len(data), address))

            if data != None:
                return (data, address)
    except:
        return(bytes('TIMEOUT', 'utf-8'), None)

def waiting_conection(): # Espera por uma descoberta d gateway
    global CONNECTED
    msg, address  = receive_multicast() # Espera a mensagem multicast
    msg = msg.decode('utf-8') # Decodifica a mensagem
    print(msg)
    if msg == 'IDF': # Verifica o comando
        s.sendto(bytes(info, 'utf-8'), (HOST,PORT)) # Envia informações
        CONNECTED = True
 
def inicialize():  # Ao ligar, o obj se apresenta para o servidor
    global CONNECTED
    msg = json.dumps({'operation':'APRT', 'info':info}) # JSON da operação de apresentação com as informações do obj
    s.sendto(bytes(msg, 'utf-8'), (HOST,PORT)) # Enviar os dados
    s.settimeout(1) # Delay para esperar resposta
    try:
        msg, _ = s.recvfrom(1024)        # Espera a confirmação do gateway
        if(msg.decode('utf-8') == 'OK'): # Confirmação
            CONNECTED = True             # Muda o status para conectado
    except:
        pass

def operate():  # Rotina do objeto
    global CONNECTED
    while True:
        if(CONNECTED == False): # Laço para espera pelo gateway
            waiting_conection()
        else:   # Caso já esteja conetado, começa a rotina de fato
            try:
                print('Waiting for a command')
                cmd = input()    # Espera o usuário inserir alguma comando

                if cmd == 'LAMP-ON':  # Comando para acender a lampada
                    data = json.dumps({'operation':'LAMP', 'command':'ON'}) # Define o JSON do comando
                    s.sendto(bytes(data, 'utf-8'), (HOST,PORT)) # Envia o comando para o gateway
                elif cmd == 'LAMP-OFF':  # Comando para desligar a lampada
                    data = json.dumps({'operation':'LAMP', 'command':'OFF'}) # Define o JSON do comando
                    s.sendto(bytes(data, 'utf-8'), (HOST,PORT)) # Envia o comando para o gateway
                elif cmd == 'ATT-SENSOR': # Comando para receber o valor do sensor
                    data = json.dumps({'operation':'ATT-SENSOR'}) # Define o JSON do comando
                    s.sendto(bytes(data, 'utf-8'), (HOST,PORT)) # Envia o comando para o gateway
                    s.setblocking(True) # Seta para bloqueante para espera a resposta do servidor
                    valor, _ = s.recvfrom(1024)  # Espera o retorno do gateway 
                    print('Valor do sensor: '+valor.decode('utf-8'))
            except:
                continue

HOST = "127.0.0.1"  # IP do servidor e do objeto (ambos local)
PORT = 6789         # Porta do servidor
CONNECTED = False   # Variavel de status de conexão
# informações do objeto
info = json.dumps({'id': 1,'name': 'client-controller', 'type': 'controller', 'ip': HOST, 'port': PORT})

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Instância um socket para o obj

# Rotina do objeto
inicialize()   # Ao inciar, tenta se apresentar para o gateway
operate()      # Rotina de fato


