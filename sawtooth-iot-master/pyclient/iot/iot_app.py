import os
from iot.iot_client import IoTClient
from datetime import datetime
import time
#import bluetooth
#import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.OUT)
#ReleCanal1 = 8  # controle do GPIO23 (este controla o canal 1 do modulo de reles)
#ReleCanal2 = 8  # controle do GPIO24 (este controla o canal 2 do modulo de reles)
DISTRIBUTION_NAME = 'iot'
DEFAULT_URL = 'http://rest-api:8008'

def _get_keyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.priv'.format(key_dir, customerName)

def _get_pubkeyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.pub'.format(key_dir, customerName)

def store_sensor_data():
    client = "iot"
    state = input("MAC: ")
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    response = iot_cli.store_sensor_data(state)
    print("Response: {}".format(response))

def get_sensor_data():
    client = "iot"
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_data()

    if data is not None:
        print("\n{} have a state = {}\n".format(client, data.decode()))
    else:
        raise Exception("state not found: {}".format(client))

def get_sensor_history():
    client = "iot"
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_history()

    if data is not None:
        for i in data:
            print(i.decode())
    else:
        raise Exception("history not found: {}".format(client))

def start_scan():
    y = 0
    x = 0
    while True:
        print("[SCAN] Scan BLE sendo realizado. Aguarde...")
        results = search()
        print("[SCAN] Fim do scan BLE.")
        if len(results) > 0:
            for addr in results:
                print("Dispositivo encontrado: {0}".format(addr))
                mac(addr)
                y = 0
        else:
            print("Nenhum dispositivo BLE encontrado.")
            y = y + 1
            if y > 4:
                break

        print(results)
        time.sleep(1)
        x = x + 1
        print("Fim do ciclo {}".format(x))
        break

def mac(bl_mac):
    client = "iot"
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_history()
    if data is not None:
        for i in data:
            valor = i.decode()
            if valor[18:] == bl_mac:
                abrir()

    else:
        raise Exception("history not found: {}".format(client))

def search():
    devices = ("48:2C:A0:BA:95:4C","64:32:A8:8D:CA:33")
    #devices = bluetooth.discover_devices(duration=5, lookup_names=True)
    return devices

def abrir():
    print("Abrindo fechadura, {}".format(datetime.now()))
#    GPIO.output(ReleCanal2, GPIO.LOW)
#    GPIO.output(ReleCanal1, GPIO.LOW)
#    time.sleep(5)
#
#    GPIO.output(ReleCanal1, GPIO.HIGH)
#    GPIO.output(ReleCanal2, GPIO.HIGH)

def fechar():
    print("Fechando fechadura")
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(ReleCanal1, GPIO.OUT)
    #GPIO.setup(ReleCanal2, GPIO.OUT)

    # desaciona os reles
    #GPIO.output(ReleCanal1, GPIO.HIGH)
    #GPIO.output(ReleCanal2, GPIO.HIGH)

def main():
    op = "-1"
    while op != "5":
        print("\n1 - store sensor data\n2 - get sensor data\n3 - get sensor history\n4 - start scan\n5 - exit\n")
        op = input("Operation: ")
        if op == "1":
            store_sensor_data()
        elif op == "2":
            get_sensor_data()
        elif op == "3":
            get_sensor_history()
        elif op == "4":
            start_scan()