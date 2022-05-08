import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8888))
sock.listen(5)

while 1:
    print("server is waiting ...")
    conn, addr = sock.accept()  # 等待客户端链接

    # 接收客户端(浏览器)的消息
    data = conn.recv(1024)
    print(data)
    # 获取路径
    data = data.decode()
    path = data.split("\r\n")[0].split(" ")[1]
    # 基于路径分发
    if path == "/login":
        conn.send(b"HTTP/1.1 200 ok \r\n\r\n hello login ")
    elif path == "/index":
        conn.send(b"HTTP/1.1 200 ok \r\n\r\n hello index ")
    else:
        conn.send(b"HTTP/1.1 200 ok \r\n\r\n hello 404 ")









