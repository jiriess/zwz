#！D:linux/python
# -*- encoding: utf-8 -*-  encoding指定的编码格式

import socket  
import sys  #system模块
import struct
import json
import os
IP = '192.168.83.130' #填写服务器端的IP地址  
port = 40005 #端口号必须一致  
buffsize = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET是IPv4 网络协议的套接字类型   SOCK_STREAM是TCP类型，保证数据顺序及可靠性 
try:  
    s.connect((IP,port))  #匹配IP地址和端口
    print("开始会话")
    print("传输字符请输入1(输入bye结束对话)，传输文件请输入2，输入其他数字结束")
except Exception as e:  #异常情况
    print('server not find or not open')  
    sys.exit()  #从程序中退出，但会产生systemExit异常
while True:  #循环
    send_data=input("请选择：")
    s.sendall(bytes(send_data,encoding="utf8"))#将输入的选项编码发送
    if send_data=="1":
    	while True:
            trigger = input("send:")  #输入字符，触发转码
            s.sendall(trigger.encode())  #以encoding指定的编码格式编码字符串
            data = s.recv(1024)  #每次最多接收1024个字节
            data = data.decode()  #以encoding指定的编码格式解码字符串
            print('recieved:',data) #接收数据
            if trigger.lower() == "bye" :#发送bye结束连接  lower将大写转化为小写 
                break 
    elif send_data=="2":
        head_struct = s.recv(4)  # 接收报头的长度,
        if head_struct:
            print('已连接服务端,等待接收数据')
        head_len = struct.unpack('i', head_struct)[0]  # 解析出报头的字符串大小
        data = s.recv(head_len)  # 接收长度为head_len的报头内容的信息 (包含文件大小,文件名的内容)

        head_dir = json.loads(data.decode('utf-8'))#解码
        filesize_b = head_dir['filesize_bytes']#返回文件大小
        filename = head_dir['filename']#返回文件名


        recv_len = 0
        recv_mesg = b''
        f = open(filename, 'wb')#打开文件
        while recv_len < filesize_b:#接收到的文件小于文件本身的大小

            if filesize_b - recv_len > buffsize:#放入缓冲区分段接收

                recv_mesg = s.recv(buffsize)
                f.write(recv_mesg)
                recv_len += len(recv_mesg)
            else:
                recv_mesg = s.recv(filesize_b - recv_len)
                recv_len += len(recv_mesg)
                f.write(recv_mesg)

        print("文件已接收！")

        f.close()
    else:
        print("结束！")
        sys.exit()

