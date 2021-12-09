import socket
import struct
import sys
import json
    
def send_multicast(message):  # Enviar mensagem multicast
    multicast_group = ('224.3.29.71', 10000) # Endereço IP e porta utilizada para o multicast

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket udp

    sock.settimeout(0.2) # Delay para o multicast

    ttl = struct.pack('b', 1) # Seta o time-to-live da mensagem para 1 
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl) # Atualiza o valor do ttl

    try:
        print('Sending by multicast "%s"\n' %message)
        message = message.encode('UTF-8') # Codifica a mensagem
        sock.sendto(message, multicast_group) # Envia a mensagem no multicast

    finally:
        print('Closing multicast socket\n')
        sock.close()  # fecha o socket

def start():                # Descoberta do gateway de dispositivos
    send_multicast('IDF')   # Envia comando para os dispositivos se identificarem
    sock.settimeout(1)      # Seta o timeout para 1 para não ficar esperando resposta para sempre
    try:
        info_device, address = sock.recvfrom(1024)   # Espera resposta dos dispositivos
        info_device = json.loads(info_device)        # Transforma o JSON em dicionario
        devices[info_device['id']] = info_device     # Adiciona o id do dispositivo como chave do dict da lista
        _, devices[info_device['id']]['port'] = address  # Atualiza a posta do dispositivos nas informações
        print('Device '+ info_device['name'] +' id:'+str(info_device['id'])+' added to list') # Confirma na tela a adição
        sock.sendto(bytes('OK', 'utf-8'), (HOST,devices[info_device['id']]['port'])) # Envia uma mensagem para o objeto
    except:                                                                          # para confirmar a operação
        pass

def operate():    # Rotina do gateway
    while True:
        print('Waiting for communication')
        sock.setblocking(True)   # Seta novamente para bloqueante

        data, address = sock.recvfrom(1024)  # Fica agurando algum comano
        data = json.loads(data)  # Transforma o JSON em dicionario

        if data['operation'] == 'APRT':   # Comando de apresentação de dispositivos
            data['info'] = json.loads(data['info'])  # Desacopla o outro JSON de dentro
            if(data['info']['id'] not in devices.keys()):   # Verifica se o objeto já está na lista
                devices[data['info']['id']] = data['info']  # Adiciona o id do dispositivo como chave do dict da lista
                _, devices[data['info']['id']]['port'] = address  # Atualiza a posta do dispositivos nas informações
                print('Device '+ data['info']['name'] +' id:'+str(data['info']['id'])+' added to list')
                sock.sendto(bytes('OK', 'utf-8'), address) # Envia uma mensagem para o objeto para confirmar a operação
            else:
                print('Device is already on the list')
        elif data['operation'] == 'LAMP':  # Comando para controlar a lampada
            if data['command'] == 'ON' :   # Identificação que o comado é para ligar
                sock.sendto(bytes('ON', 'utf-8'), (HOST, devices[2]['port']))
            elif data['command'] == 'OFF' : # Identificação que o comado é para desligar
                sock.sendto(bytes('OFF', 'utf-8'), (HOST, devices[2]['port']))
        elif data['operation'] == 'ATT-SENSOR':  # Comando para atualizar o sensor do sensor
            sock.sendto(bytes('ATT', 'utf-8'), (HOST, devices[4]['port'])) # Manda o comando para o obj sensor
            data, _ = sock.recvfrom(1024)  # Espera o retorno do obj sensor
            sock.sendto(data, (HOST, devices[1]['port'])) # Devolve o valor para o cliente


devices = {}    # Dicionário para listar os dispositivos/objetos e guardar suas informações
HOST = ''       # Utilizamos o localhost pois os testes foram feitos todos no mesmo computador
PORT = 6789     # Porta utilizada para o gateway
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Criando um socket udp para o gateway
sock.bind((HOST, PORT))   # Atribuindo porta e o endereço IP explicitamente para
                          # utilziar o soquete como servidor servidor

# Execuções do gateway
start()     # Descoberta do gateway em multicast
operate()   # Rotina do gateway após a descoberta

