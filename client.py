import socket
import random
from time import sleep

# Адрес и порт сервера.
HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        output_message = "Сообщение серверу под номером " + str(random.randint(0, 1000))
        s.sendall(output_message.encode())
        input_message = s.recv(1024).decode()
        print("Получено сообщение:", input_message)
        sleep(random.randint(1,2))
