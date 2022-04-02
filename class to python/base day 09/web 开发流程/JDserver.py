import socket

# (1) 构建套接字对象, 确定通信协议
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# (2) 绑定ip和端口
ip_port = ("127.0.0.1", 8888)  # 设置为元祖格式
sock.bind(ip_port)  # 因为bind只接收一个参数, 所以设置成元祖

# (3) 监听最大排队数, 最大连接数
sock.listen(5)
while 1:
    # (4) 阻塞等待, 等待客户端的连接
    print("server is waitting......")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    with open("E:\\代码保存\\py\\base day 09\\web 开发流程\\index.html", "rb") as f:
        conn.send(b"HTTP/1.1 200 ok \r\n\r\n" + f.read())
    print(data.decode())
sock.close()
