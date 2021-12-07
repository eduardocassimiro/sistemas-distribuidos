import socket
import threading
import struct
import sys
import json
    
def send_multicast(message):
    multicast_group = ('224.3.29.71', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.settimeout(0.2)

    # Seta o time-to-live da mensagem para 1 
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        print('Sending by multicast "%s"\n' %message)
        message = message.encode('UTF-8')
        sock.sendto(message, multicast_group)

    finally:
        print('Closing multicast socket\n')
        sock.close()

def start():
    send_multicast('IDF')
    sock.settimeout(1)
    try:
        info_device, address = sock.recvfrom(1024)
        info_device = json.loads(info_device)
        devices[info_device['id']] = info_device
        _, devices[info_device['id']]['port'] = address
        print('Device '+ info_device['name'] +' id:'+str(info_device['id'])+' added to list')
        sock.sendto(bytes('OK', 'utf-8'), (HOST,devices[info_device['id']]['port']))
    except:
        pass

def operate():
    while True:
        print('Waiting for communication')
        sock.setblocking(True)

        data, address = sock.recvfrom(1024)
        data = json.loads(data)

        if data['operation'] == 'APRT':
            data['info'] = json.loads(data['info'])
            if(data['info']['id'] not in devices.keys()):
                devices[data['info']['id']] = data['info']
                _, devices[data['info']['id']]['port'] = address
                print('Device '+ data['info']['name'] +' id:'+str(data['info']['id'])+' added to list')
                sock.sendto(bytes('OK', 'utf-8'), address)
            else:
                print('Device is already on the list')
        elif data['operation'] == 'LAMP':
            if data['command'] == 'ON' :
                sock.sendto(bytes('ON', 'utf-8'), (HOST, devices[2]['port']))
            elif data['command'] == 'OFF' :
                sock.sendto(bytes('OFF', 'utf-8'), (HOST, devices[2]['port']))
        elif data['operation'] == 'ATT-SENSOR':
            sock.sendto(bytes('ATT', 'utf-8'), (HOST, devices[4]['port']))
            data, _ = sock.recvfrom(1024)
            sock.sendto(data, (HOST, devices[1]['port']))


devices = {}
HOST = ''
PORT = 6789
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
address = 0

start()
#sock.sendto(bytes('ON', 'utf-8'), (HOST, devices[2]['port']))
#sock.close()
operate()

