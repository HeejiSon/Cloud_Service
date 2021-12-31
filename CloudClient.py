import socket
import time
from threading import *
import SaveFile

class CloudClient:
    def __init__(self):
        self.c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 9000
        self.c_sock.connect((self.TCP_IP, self.TCP_PORT))
        self.threadTest()

    def threadTest(self):                               # 스레드를 이용한 받기, 보내기 기능
        self.t = Thread(target=self.test)
        self.t2 = Thread(target=self.receive)
        self.t.start()
        self.t2.start()

    def test(self):
        while True:
            print("FileList :: 파일의 목록을 출력합니다.")
            print("sendFile :: 파일을 가져옵니다.")
            message = str(input("입력 "))

            if message == "FileList":
                self.c_sock.send(message.encode())              # 서버 9000에 FileList 메시지 보내기

            elif message == "sendFile":
                self.c_sock.send(message.encode())              # 서버 9000에 sendFile 메시지 보내기
                FileName = str(input("파일 이름을 입력해주세요 :: "))
                SaveFile.SaveFile(FileName)                             # 파일 받는 클라이언트 9001 포트 연결
            else:
                print("다시 입력")

            import os
            os.system('cls')

    def receive(self):
        while True:
            m1 = self.c_sock.recv(1024).decode()
            print(m1)



if __name__== "__main__":
    CloudClient()