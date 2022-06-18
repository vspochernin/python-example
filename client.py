import socket
import random
from time import sleep

# Адрес и порт сервера.
HOST = "192.168.0.103"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = "Сообщение серверу под номером " + str(random.randint(0, 1000))
        s.sendall(data.encode())
        message = s.recv(1024).decode()
        print("Получено сообщение:", message)
        sleep(random.randint(1,2))