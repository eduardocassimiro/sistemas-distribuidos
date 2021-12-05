import socket
import threading
import utilcliente

conexoes = 0

if conexoes == 0:
    input_i = input('')
    if input_i == '/ENTRAR':
        print("Insira o IP e a Porta do Servidor e seu Nickname.")
        server = input("IP_Servidor: ")
        port = input("Porta_Servidor: ")
        nickname = input("Seu Nickname: ")

        ADDR = (server, int(port))

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(ADDR)
            print("Servidor Conectado!")

            conexoes = 1
            receber_thread = threading.Thread(target=receber, args=(client_socket, nickname))
            receber_thread.start()

            escrever_thread = threading.Thread(target=escrever, args=(client_socket, nickname))
            escrever_thread.start()

        except Exception as e:
            print(e)