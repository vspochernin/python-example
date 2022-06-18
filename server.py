import socket

# Адрес и порт сервера.
HOST = "192.168.0.103"
PORT = 65432

# Открытие интернет-сокета IPv4 через протокол TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # Привязка сокета к адресу.
    s.listen() # Разрешение серверу принимать соединения.
    conn, addr = s.accept() # Принимаем соединение из addr с сокетом conn.
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
