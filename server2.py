#!D:/python

# -*- coding: utf-8 -*-





from socket import *

import struct

import json

import os

import sys

t = socket(AF_INET, SOCK_STREAM) #AF_INET是IPv4 网络协议的套接字类型   SOCK_STREAM是TCP类型，保证数据顺序及可靠性 

ip_port = (('', 40005))#端口号与IP

buffsize = 1024#缓冲区大小

port = 40005 #端口号  

#   端口的重复利用

t.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)#描述符选项，端口重用

t.bind(ip_port)#连接

t.listen(5)#监听

print('还没有人链接')

while True:

    '''链接循环'''

    conn, addr = t.accept()#与client端IP和端口匹配

    print("开始会话")  

    print('链接人的信息:', addr)

    while True:

        if not conn:#连接失败

            print('客户端链接中断')

            break

        data = conn.recv(1024)  #接收client端输入的选项，进行判断

        data = data.decode()#解码选项字符

        '''通信循环'''

        if data=="1":#传输字符



            print('listen at port :',port)    

            print('connected by',addr)  

             

            while True:  

                data = conn.recv(1024)  #接收client端输入的字符串

                data = data.decode()#解码字符串 

                if not data:  

                    break  

                print('recieved message:',data)  #显示收到的数据

                send = input('return:')#python3.X用input  

                conn.sendall(send.encode())#再编码发送               

                if data=="bye":#输入字符串bye，则结束会话

                    break

          

        elif data=="2":



            filemesg = input('请输入要传送的文件名加后缀>>>').strip()#输入要传送的文件的文件名



            filesize_bytes = os.path.getsize(filemesg) # 得到文件的大小,字节

            filename = 'new' + filemesg#接受到的文件将以new加文件名命名

            dirc = {

                'filename': filename,

                'filesize_bytes': filesize_bytes,

            }#将文件名和文件大小写入字典

            head_info = json.dumps(dirc)  # 将字典转换成字符串（将对象编码为json字符串）

            head_info_len = struct.pack('i', len(head_info)) #  将字符串的长度打包       

            conn.send(head_info_len)  # 发送head_info的长度

            conn.send(head_info.encode('utf-8'))#将head_info进行编码



     

            with open(filemesg, 'rb') as f:

                data = f.read()

                conn.sendall(data)#读入文件中数据，并将数据全部发送



            print('发送成功')

            t.close()

        else:

            print("结束！")

            sys.exit()#退出