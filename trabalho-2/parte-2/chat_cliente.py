import socket
import threading

char_format = 'utf-8'
connected = 0

# Função de recebimento de dados/comandos
def receber(client_socket, nickname):
    global connected
    while True:
        try:
            msn = client_socket.recv(1024).decode(char_format)
            if msn == 'NICK':
                client_socket.send(nickname.encode(char_format))
            elif msn == '/SAIR':
                connected = 0
                client_socket.close()
                break
            elif msn == '/NICK':
                print("Insira o novo Nickname: ")
                novonick = input('')
                client_socket.send(novonick.encode(char_format))
            else:
                print(msn)
        except Exception as e:
            print(e)

# Função de ESCRITA
def escrever(client_socket, nickname):
    global connected
    while True:
        try:
            if connected == 1:
                text = input('')
                if text[0] == '/':
                    client_socket.send(text.encode(char_format))
                else:
                    message = '{}: {}'.format(nickname, text)
                    client_socket.send(message.encode(char_format))
        except Exception as e:
            print(e)

if connected == 0:
    print('Bem Vindo - uCHAT \nDigite /ENTRAR para Iniciar')
    input_i = input('')
    if input_i == '/ENTRAR':
        print("Login no uCHAT: IP_Servidor, Porta e seu Nickname.")
        server = input("IP_Servidor: ")
        port = input("Porta: ")
        nickname = input("Nickname: ")

        # Tupla de endereço - Ip_Servidor e Porta
        address = (server, int(port))

        try:
            # Iniciando uma conexão IPV4, do tipo sockets de fluxo com protocolo TCP
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Conectando o client ao servidor passado no endereço
            client_socket.connect(address)

            connected = 1
            # Criando a instancia da thread e passando os argumentos
            rcve_thread = threading.Thread(target=receber, args=(client_socket, nickname))
            # Iniciando a thread
            rcve_thread.start()

            # Criando a instancia da thread e passando os argumentos
            wrte_thread = threading.Thread(target=escrever, args=(client_socket, nickname))
            # Iniciando a thread
            wrte_thread.start()

        except Exception as e:
            print(e)