import socket

# (1) 构建套接字对象, 确定通信协议, 要和server端保持一致
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# (2) 连接服务端
ip_pord = ("127.0.0.1", 8892)  # 地址, 端口和server保持一致
sock.connect(ip_pord)

while True:
    input_Data = input("请输入命令: ")
    if input_Data == "q":
        break
    else:
        sock.send(input_Data.encode())
        cmd_res_bytes_len = sock.recv(1024)
        res_total = int(cmd_res_bytes_len.decode())
        recv_num = 0
        while recv_num < res_total:
            data = sock.recv(1024)
            print(data.decode())
            recv_num += len(data)
        print("接收的长度: ", res_total)
