import socket

class SaveFile:
    def __init__(self, filename):
        self.c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 9001
        self.c_sock.connect((self.TCP_IP, self.TCP_PORT))

        print('연결에 성공했습니다.')
        self.c_sock.send(filename.encode())         #받고자하는 파일 이름 보내기

        data = self.c_sock.recv(1024)
        data_transferred = 0

        with open("./" + filename, 'wb') as f:  # 현재dir에 filename으로 파일을 받는다
            try:
                while data:  # 데이터가 있을 때까지
                    f.write(data)  # 1024바이트 쓴다
                    data_transferred += len(data)
                    data = self.c_sock.recv(1024)  # 1024바이트를 받아 온다
            except Exception as ex:
                print(ex)
        print('파일 %s 받기 완료. 전송량 %d' % (filename, data_transferred))

if __name__== "__main__":
    SaveFile()