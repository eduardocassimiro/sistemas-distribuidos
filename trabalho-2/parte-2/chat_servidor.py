import socket
import threading

# Ip LocalHost do Servidor
host = socket.gethostbyname(socket.gethostname())
# Porta utilizada
port = 1819

# Tupla Endereço - Retorna (IpServidor & Porta)
address = (host, port)
char_format = 'utf-8'

# Iniciando uma conexão IPV4, do tipo sockets de fluxo com protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Associa o socket a porta
server.bind(address)
# Socket no modo servidor, e enfileira as conexões.
server.listen()

print("Servidor Online!")
print("IP Servidor: ", address)

# Lista de Clientes e de seus Nicknames
clients = []
nicknames = []

# Todos as máquinas que estão com o servidor rodando vão receber a mensagem enviada pelo cliente.
def broadcast(mensagem):
    for client in clients:
        client.send(mensagem)

# Função para mostrar todos os usuarios conectados
def usuarios(client):
    client.send('{}'.format(nicknames).encode(char_format))

# Função para trocar o Nickname
def novo_nick(client, nickname):
    client.send('/NICK'.encode(char_format))

    novonick = client.recv(1024).decode(char_format)
    remove = nickname + ': '
    novonick = novonick.replace(remove,'')

    for i in range(len(nicknames)):
        if nicknames[i] == nickname:
            nicknames[i] = novonick
    broadcast('{} mudou o nickname para {}'.format(nickname,novonick).encode(char_format))

# Função de comandos
def comandos(client, mensagem, nickname):
    if mensagem == '/USUARIOS':
        usuarios(client)
    elif mensagem == '/NICK':
        novo_nick(client,nickname)
    else:
        client.send("Invalido, TENTE NOVAMENTE.".encode(char_format))

# Função para desconectar o Client
def desconectar(client, nickname):
    client.send('Desconectando...'.encode(char_format))
    index = clients.index(client)
    clients.remove(client)
    client.send('Desconectado!'.encode(char_format))
    client.close()
    nickname = nicknames[index]
    print('{} Saiu!'.format(nickname))
    broadcast('{} Saiu!'.format(nickname).encode(char_format))
    nicknames.remove(nickname)

# Função de Abstração
def handle(client, nickname):
    while True:
            mensagem = client.recv(1024)
            mensagem_decodificada = mensagem.decode(char_format)
            if mensagem_decodificada[0] == '/':
                if mensagem_decodificada == '/SAIR':
                    desconectar(client, nickname)
                    break
                elif mensagem_decodificada == nickname == '/NICK':
                    novo_nick(client, nickname)
                comandos(client, mensagem_decodificada, nickname)
            else:
                broadcast(mensagem)

# Função de recebimento de Acessos
def receber():
    while True:
        if(len(clients)<4):
            # Espera por novas solicitações de conexões.
            client, address = server.accept()
            print("Conectado com {}".format(str(address)))
        else:
            # Avisa que o servidor esta lotado
            client.send('Servidor Lotado!'.encode(char_format))
            print("SERVIDOR LOTADO!!!")
            desconectar(client, nickname)
            client.close()

        client.send('NICK'.encode(char_format))
        nickname = client.recv(1024).decode(char_format)
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname: {}".format(nickname))
        broadcast("{} Entrou no Chat!".format(nickname).encode(char_format))
        client.send('Conectado ao Servidor!!'.encode(char_format))

        # Criando a instancia da thread e passando os argumentos
        thread = threading.Thread(target=handle, args=(client,nickname))
        # Start na thread
        thread.start()

receber()
