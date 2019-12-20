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

# Componentes 
A aplicação do cliente foi escrita em Python, dividida em duas partes: _client.py, que representa o backend, e o _app.py que representa o frontend. O exemplo foi construído usando o arquivo setup.py, que está localizado em um diretório acima. O Processador de Transações (smart contract | chaincode) foi escrito em python usando a python-sawtooth-sdk no arquivo _tp.py

# Usage
Inicie o container pre construído do Docker no docker-compose.yaml file, localizado no diretório sawtooth-iot:
```bash
cd sawtooth-iot-master
docker-compose up
```
Nesse momento todos os containers devem estar rodando.

Para iniciar o cliente, você deve digitar isso:
```bash
docker exec -it iot-client bash
```

Você pode localizar o nome correto do container do cliente docker usando `docker ps`.

Exemplo de uso de comando:

```bash
#Cria o iot
sawtooth keygen iot #Isso cria as chaves públicas e privadass do iot,um pré requisito para os comandos a seguir

iot_cli # Para executar a aplicação

# Menu do aplicativo do cliente
1. Salvar um endereço MAC
2. Obter o último endereço salvo
3. Obter o histórico de endereços adicionados
4. Iniciar a fechadura 
5. Sair
```

#Usando em um raspberry
Para utilizar esse código em um raspberry podem ser necessários algumas modificações dependendo da versão e do modelo do raspberry. 
O primeiro passo a ser feito para a execução em um raspberry é a conexão dos cabos e dos equipamentos da fechadura de forma correta. 
O passo a passo para a configuração dessas peças pode ser encontrada no repositório Docker_open.
Tendo conectado o equipamento de maneira correta, agora você deve adicionar o código ao raspberry, porém só é necessário a adição da parte correspondente ao cliente, caso se deseje uma execução mais leve e que o pyprocessor esteja em um equipamento separado. Entretanto, é necessária a mudança da default URL para apontar para o local onde estará rodando o pyprocessor, feito isso, o programa deverá rodar de forma normal.
