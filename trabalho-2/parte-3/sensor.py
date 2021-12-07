import socket
import struct
import sys
import json
import serial
import time


def receive_multicast():
    multicast_group = '224.3.29.71'
    server_address = ('', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Solicita ao sistema operacional para adicionar o socket ao grupo multicast em todas as interfaces
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    sock.bind(server_address)
    sock.settimeout(1)

    try:
        while True:
            print('\nWaiting to receive message by multicast\n')
            data, address = sock.recvfrom(1024)
            
            print('Received %s bytes from %s\n' % (len(data), address))

            if data != None:
                return (data, address)
    except:
        return(bytes('TIMEOUT', 'utf-8'), None)

def waiting_conection():
    global CONNECTED
    msg, address  = receive_multicast()
    msg = msg.decode('utf-8')
    print(msg)
    if msg == 'IDF':
        s.sendto(bytes(info, 'utf-8'), (HOST,PORT))
        CONNECTED = True

def inicialize():
    global CONNECTED
    msg = json.dumps({'operation':'APRT', 'info':info})
    s.sendto(bytes(msg, 'utf-8'), (HOST,PORT))
    s.settimeout(1)
    try:
        msg, _ = s.recvfrom(1024)
        if(msg.decode('utf-8') == 'OK'):
            CONNECTED = True
    except:
        pass

def operate():
    global CONNECTED
    while True:
        if(CONNECTED == False):
            waiting_conection()
        else:
            try:
                print('Waiting for a command')
                s.setblocking(True)
                msg, _ = s.recvfrom(1024)
                msg = msg.decode('utf-8')

                if msg == 'ATT':
                    ser = serial.Serial('/dev/ttyACM2', 9600)
                    data = ser.readline().decode()
                    s.sendto(bytes(data, 'utf-8'), (HOST,PORT))
                    print('> Sensor value has been updated')
                elif msg == 'IDF':
                    s.sendto(bytes(info, 'utf-8'), (HOST,PORT))
            except:
                continue

HOST = "127.0.0.1"
PORT = 6789
CONNECTED = False
info = json.dumps({'id': 4,'name': 'LDR', 'type': 'sensor', 'ip': HOST, 'port': 6789})

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect((HOST,6788))
inicialize()
operate()


