import socket
import os
import json

# (1) 构建套接字对象, 确定通信协议, 要和server端保持一致
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# (2) 连接服务端
ip_pord = ("127.0.0.1", 6666)  # 地址, 端口和server保持一致
sock.connect(ip_pord)

while True:
    params = input("请输入命令(比如上传文件 put 文件路径): ")
    cmd, local_path = params.split(" ")
    # 将文件信息传给服务端
    file_size = os.path.getsize(local_path)  # 获取文件大小
    file_name = os.path.basename(local_path)  # 获取文件名
    file_params = {"file_name": file_name, "file_size": file_size}
    data = {"cmd": cmd, "params": file_params}
    print("data", data)
    sock.send(json.dumps(data).encode())

    # 循环读取文件, 传给server端
    with open(local_path, "rb") as f:
        for line in f:  # 用循环的方式一行行的读, 保证不会因为文件太大一口气读, 导致内存问题
            sock.send(line)
    print("文件发送完毕")
