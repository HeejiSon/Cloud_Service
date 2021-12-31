import os
import socket
from threading import *

class CloudServer2:         #파일 전송용 서버 소켓
    def __init__(self):
        self.p_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 9001
        self.p_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.p_socket.bind((self.TCP_IP, self.TCP_PORT))
        self.p_socket.listen(5)
        self.c_socket, addr = self.p_socket.accept()
        self.receive()


    def receive(self):
        print("9001 포트 대기중")
        message = self.c_socket.recv(1024).decode()     #메세지 받기
        print(message)
        self.sendFile(message)          #파일 이름 넘겨서 파일 전송

    def sendFile(self, filename):
        data_transferred = 0

        with open("./files/" + filename, 'rb') as f:
            try:
                data = f.read(1024)  # 1024바이트 읽는다
                while data:  # 데이터가 없을 때까지
                    data_transferred +=self.c_socket.send(data)  # 1024바이트 보내고 크기 저장
                    data = f.read(1024)  # 1024바이트 읽음
            except Exception as ex:
                print(ex)
        print("전송완료 %s, 전송량 %d" % (filename, data_transferred))
