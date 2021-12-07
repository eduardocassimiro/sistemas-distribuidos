import socket
import threading

char_formato = 'utf-8'

def receber(client_socket, nickname):
    global conexoes
    while True:
        try:
            mensagem = client_socket.recv(1024).decode(char_formato)
            if mensagem == 'NICK':
                client_socket.send(nickname.encode(char_formato))
            elif mensagem == 'Desconectado!!':
                print(mensagem)
                conexoes = 0
                client_socket.close()
                break
            else:
                print(mensagem)
        except Exception as e:
            print(e)

def escrever(client_socket, nickname):
    global conexoes
    while True:
        try:
            if conexoes == 1:
                text = input('')
                if text[0] == '/':
                    client_socket.send(text.encode(char_formato))
                else:
                    message = '{}: {}'.format(nickname, text)
                    client_socket.send(message.encode(char_formato))
        except Exception as e:
            print(e)
