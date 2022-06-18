import socket

# Адрес и порт сервера.
HOST = "127.0.0.1"
PORT = 65432

# Открытие интернет-сокета IPv4 через протокол TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # Привязка сокета к адресу.
    s.listen() # Разрешаем серверу принимать соединения.
    conn, addr = s.accept() # Принимаем соединение из addr с сокетом conn.
    with conn:
        print('Установлено соединение с', addr)
        while True:
            input_message = conn.recv(1024).decode()
            print("Получено сообщение:", input_message)
            parts = input_message.split(' ')
            message_number = parts[len(parts) - 1]
            output_message = "Сервером успешно было получено сообщение с номером " + message_number
            conn.sendall(output_message.encode())
