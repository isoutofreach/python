import socket
import subprocess

# (1) 构建套接字对象, 确定通信协议
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# (2) 绑定ip和端口
ip_port = ("127.0.0.1", 8892)  # 设置为元祖格式
sock.bind(ip_port)  # 因为bind只接收一个参数, 所以设置成元祖

# (3) 监听最大排队数, 最大连接数
sock.listen(5)
while 1:
# (4) 阻塞等待, 等待客户端的连接
    print("server is waitting......")
    # conn, addr = sock.accept()  # conn 是客户端的信息
    conn, addr = sock.accept()
    while True:
        cmd = conn.recv(1024).decode()
        if cmd == "" or cmd == "q":
            break
        else:
            cmd_res_bytes = subprocess.getoutput(cmd).encode() # 拿到命令结果
            print("返回的结果字符长度: ", len(cmd_res_bytes))
            cmd_res_bytes_len = str(len(cmd_res_bytes)).encode()
            conn.send(cmd_res_bytes_len)
            conn.send(cmd_res_bytes)

