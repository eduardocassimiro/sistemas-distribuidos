## Repositório da Cadeira de Sistema Distribuídos 2021.2

### Integrantes da Equipe
- Carlos Eduardo Cassimiro da Silva (402714)
- José Erivan Teixeira Filho (398698)
- Kayann Costa Soares (429866)

---

## Trabalho 1

Link para a gravação: [link-youtube](https://www.youtube.com/watch?v=x92WfJxZcUE&feature=youtu.be)

## Trabalho 2

Link para a apresentação: [link-slide](https://docs.google.com/presentation/d/1IQ-sfUSFmchnC6XoC0gYm0y0VOTEX1Q_HI2gCrR30YU/edit?usp=sharing)

### Parte 1 - Calculadora UDP
A primeira parte do trabalho consiste em, utilizando UDP, implementar uma calculadora remota que execute as 4 operações básicas (+,-,∙,÷) de números decimais. <br>

Links para os arquivos: <br>
[calculadora_cliente.py](trabalho-2/parte-1/calculadora_cliente.py)<br>
[calculadora_servidor.py](trabalho-2/parte-1/calculadora_servidor.py)<br>

### Parte 2 - Chat TCP
A segunda parte do trabalho consiste em implementar um Chat usando TCP. O Chat deve suportar múltiplos clientes e um servidor. Todos os clientes devem estar na mesma sala do chat (i.e., as mensagens enviadas por um cliente devem ser recebidas por todos os clientes). A sala do Chat deve suportar no máximo 4 pessoas conectadas. Comandos que o usuário (i.e., cliente) pode enviar:
a. /ENTRAR: ao usar esse comando, ele é requisitado a digitar IP, porta do servidor e apelido que deseja usar no chat (não pode haver apelidos repetidos). O servidor deve aceitar a conexão ou negar por já ter atingido o máximo de clientes conectados ou já haver alguém usando o mesmo apelido. <br>
b. Uma vez conectado, o cliente pode enviar mensagens para a sala do chat; <br>
c. /USUARIOS: ao enviar esse comando, o cliente recebe a lista de usuários atualmente conectados ao chat; <br>
d. /NICK: com esse comando, o cliente pode trocar seu apelido. Todos os usuários conectados ao chat devem ser notificados da mudança. <br>
e. /SAIR: ao enviar esse comando, uma mensagem é enviada à sala do chat informando que o usuário está saindo e encerra a participação no chat. <br>

Links para os arquivos: <br>
[chat_cliente.py](trabalho-2/parte-2/chat_cliente.py)<br>
[chat_servidor.py](trabalho-2/parte-2/chat_servidor.py)<br>


### Parte 3 - Ambiente Inteligente
A terceira parte do trabalho consiste em implementar um ambiente inteligente (e.g., casa, escritório, sala de aula, clínica médica, carro, etc) com as seguintes condições e
restrições: <br>
a. Uma aplicação chamada de Gateway deve ser implementada. Ela se comunica com cada um dos objetos “inteligentes” do local. A comunicação entre o Gateway e os objetos “inteligentes” deve ser implementada utilizando TCP e as mensagens definidas com Protocol Buffers. <br>
b. O ambiente inteligente deve conter, no mínimo, 3 equipamentos (e.g., lâmpadas, ar-condicionado, TV, tablet, sistema de som, sistema de irrigação). <br>
c. Os equipamentos podem ser todos simulados por software (e.g., um processo para cada equipamento), que envia de forma periódica seu status (ou quando ele se modifica) e recebe os comandos para ligar/desligar ou realizar alguma operação (e.g., aumentar a temperatura). <br>
d. O Gateway deve ter uma funcionalidade de descoberta de equipamentos inteligentes, usando comunicação em grupo. Ao iniciar o Gateway, ele deve enviar uma mensagem solicitando que os equipamentos se identifiquem. <br>
e. Ao iniciar o processo dos equipamentos inteligentes, estes devem enviar mensagem se identificando para o Gateway. A identificação significa enviar seu tipo (e.g., lâmpadas, ar-condicionado, etc), IP e Porta para o Gateway. <br>
f. Pelo menos um dos equipamentos deve atuar como um sensor contínuo, que envia a cada ciclo de X segundos um valor para o Gateway (e.g., um sensor de
temperatura). <br>
g. Pelo menos um dos equipamentos deve ter comportamento de um atuador (i.e., recebe comandos para modificar seu status, como desligar uma lâmpada); <br>
h. Usuários devem acessar as informações dos objetos inteligentes e controlá-los através de uma interface de linha de comando no próprio processo Gateway. <br>

Links para os arquivos: <br>
[gateway.py](trabalho-2/parte-3/gateway.py)<br>
[lamp.py](trabalho-2/parte-3/lamp.py)<br>
[sensor.py](trabalho-2/parte-3/sensor.py)<br>
[client-controller.py](trabalho-2/parte-3/client-controller.py)<br>
[lamp.ino](trabalho-2/parte-3/arduino/lamp/lamp.ino)<br>
[sensor.ino](trabalho-2/parte-3/arduino/sensor/sensor.ino)<br>

## Trabalho 3

O trabalho consiste em simular um ambiente inteligente (por exemplo, casa, escritório, sala de aula, clínica médica, carro, etc). Neste ambiente deverão estar presentes Sensores (que coletam dados do ambiente) e Atuadores (que podem agir no ambiente para modificá-lo de alguma forma). Por exemplo, em um ambiente residencial inteligente, podem existir sensores de temperatura que coletam periodicamente a temperatura ambiente e aparelhos como
ares-condicionados e aquecedores que podem trabalhar como atuadores e agir para modificar a temperatura ambiente.

Link para o slide: [link-slide](https://docs.google.com/presentation/d/11ZdamoBGLiml_seT4QCidYtwbpawbXPCVzFvSLg3XwA/edit?usp=sharing)

Link para a apresentação: [link-video](https://docs.google.com/presentation/d/1IQ-sfUSFmchnC6XoC0gYm0y0VOTEX1Q_HI2gCrR30YU/edit?usp=sharing)

### Arquivos
#### Interface Web
[La_pagina](trabalho-3/La_pagina.zip)<br>
#### Home Assistant
[home_assistant](trabalho-3/home_assistant.py)<br>
#### Sensores 
[sensor_luz](trabalho-3/sensor_luz.py)<br>
[sensor_temperatura](trabalho-3/sensor_temperatura.py)<br>
[sensor_campainha](trabalho-3/sensor_campainha.py)<br>
#### Atuadores
[smart_portao_server](trabalho-3/smart_portao_server.py)<br>
[smart_lamp_server](trabalho-3/smart_lamp_server.py)<br>
[smart_ventilador_server](trabalho-3/smart_ventilador_server.py)<br>
#### Protobuffer
[smart_obj.proto](trabalho-3/smart_obj.proto)<br>
[smart_ventilador.proto](trabalho-3/smart_ventilador.proto)<br>
[smart_portao.proto](trabalho-3/smart_portao.proto)<br>
[smart_lamp.proto](trabalho-3/smart_lamp.proto)<br>
[smart_obj_pb2.py](trabalho-3/smart_obj_pb2.py)<br>
[smart_lamp_pb2](trabalho-3/smart_lamp_pb2.py)<br>
[smart_portao_pb2](trabalho-3/smart_portao_pb2.py)<br>
[smart_ventilador_pb2](trabalho-3/smart_ventilador_pb2.py)<br>
#### gRPC
[smart_portao_pb2_grpc](trabalho-3/smart_portao_pb2_grpc.py)<br>
[smart_lamp_pb2_grpc](trabalho-3/smart_lamp_pb2_grpc.py)<br>
[smart_ventilador_pb2_grpc](trabalho-3/smart_ventilador_pb2_grpc.py)<br>
#### Arduino
[led_e_ventilador](trabalho-3/arduino/led_ventilador.ino)<br>
[motor_de_passos](trabalho-3/arduino/motor_de_passos.ino)
