import os
import socket
from threading import *
import CloudServer2

file_list = os.listdir('./files')
file_list.sort()
print(file_list)

str_file_list = str(file_list)


class CloudServer:
    def __init__(self):
        self.p_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 9000
        self.p_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.p_socket.bind((self.TCP_IP, self.TCP_PORT))
        self.p_socket.listen(5)

        self.c_socket, addr = self.p_socket.accept()  # 클라이언트 소켓 accept

        self.receive()  # 함수 호출

    def receive(self):
        while True:
            message = self.c_socket.recv(1024).decode()  # 9000 포트 메시지 받기
            print(message)

            if message == "FileList":  # FileList 메시지 이면
                self.c_socket.send(str_file_list.encode())  # files 폴더의 파일들 리스트를 보내기
            elif message == "sendFile":
                CloudServer2.CloudServer2()


if __name__ == "__main__":  # 시작함수
    CloudServer()