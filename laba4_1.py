import socket
HOST = ''                 #  Посилання на інтерфейс/IP, у разі None -> будь-який інтерфейс
PORT = 50007       # Порт на якому сервер буде приймати з'єднання, >1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
