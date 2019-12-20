# fechadura-blockchain
Um exemplo de aplicação sawtooth "iot" transaction family (processor + client), aplicada em um raspberry para abrir uma fechadura

# Introdução

Esse é um exemplo de uma aplicação sawtooth 1.0. Nesse exemplo é o usuário pode:
1. Salvar um endereço MAC
2. Obter o último endereço salvo
3. Obter o histórico de endereços adicionados
4. Iniciar a fechadura 

Ao iniciar a fechadura ele roda em um loop infinito procurando por endereços MAC usando bluetooth, quando encontra ele verifica se o endereço foi adicionado na aplicação, caso sim, ele destrava a porta.

O usuário é identificado por um nome de usuário e uma chave publica correspondente. Os endereços MAC são salvos em um endereço hash SHA 512 derivado da chave publica do usuário e do namespace da família de transação IOT.

# Components
The client application is written in Python, written in two parts: _client.py file representing the backend stuff and the _app.py representing the frontend stuff. The example is built by using the setup.py file located in one directory level up. The Transaction Processor (smart contract | chaincode) is written in Python using python-sawtooth-sdk in _tp.py file.

# Usage

Start the pre-built Docker containers in docker-compose.yaml file, located in sawtooth-iot directory:
```bash
cd sawtooth-iot
docker-compose up
```
At this point all the containers should be running.

To launch the client, you could do this:
```bash
docker exec -it iot-client bash
```

You can locate the right Docker client container name using `docker ps`.

Sample command usage:

```bash
#Create a iot
sawtooth keygen iot #This creates the public/private keys for iot, a pre-requisite for the following commands

iot_cli # To execute app

# Client App Menu
1 - store sensor data
2 - get sensor data
3 - get sensor history
4 - exit
```
