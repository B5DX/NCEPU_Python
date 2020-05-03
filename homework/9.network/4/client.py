# 4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
# Client
from server import Server
from threading import Thread
import socket

class Client:
    def __init__(self):
        super().__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(Server.getServerAddr())
        while True:
            info = self.verifyInfo()
            self._socket.send(info.encode('utf-8'))
            flag = self._socket.recv(1024).decode('utf-8')
            if flag == 'Y':
                break
            else:
                print('Name has been registered. Please reinput a new name.')
        self._userName = info
        self._sendThread = Thread(target=self.sendMsg)
        self._recvThread = Thread(target=self.recvMsg)

    def startClient(self):
        self._sendThread.start()
        self._recvThread.start()
        self._recvThread.join()
        self._socket.close()
        exit(0)

    def sendMsg(self):
        while True:
            s = input('ME: ')
            self._socket.send(s.encode('utf-8'))

    def recvMsg(self):
        while True:
            try:
                s = self._socket.recv(1024)
                self.print(s)
            except Exception as e:
                print('\b'*4 + 'Server has been shut down. Forced to exit.')
                return
    
    def print(self, s):
        print('\b'*4 + s.decode('utf-8') + '    ' + '\n' + 'ME: ', end='')
        # 不知道为什么下面再写一句print好像不见得一下就会执行……
    
    @staticmethod
    def verifyInfo():
        while True:
            info = input('input user name to join(do not contain \' \'): ')
            if ' ' in info:
                print('\' \' shound\'t accur. Input again.')
                continue
            break
        return info

if __name__ == "__main__":
    client = Client()
    client.startClient()
