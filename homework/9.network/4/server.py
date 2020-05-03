# 4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
# Server
import socket
from threading import Thread
from multiprocessing import Process

class Server:
    _addr = ('192.168.220.1', 8888)
    def __init__(self):
        super().__init__()
        self._users = {}
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._thread_queue = []

    @classmethod
    def getServerAddr(cls):
        return cls._addr

    def startServer(self):
        try:
            self._socket.bind(self._addr)
            self._socket.listen(5)
        except Exception as e:
            print(e)
            self.closeServer()
        p = Process(target=self.serverConnect)
        p.start()

        print('Server start. Input \'#\' to exit.')
        while True:
            cmd = input()
            if cmd == '#':
                p.kill()
                self.closeServer()
                return

    def serverConnect(self):
        while True:
            soc, addr = self._socket.accept()
            # info = self._socket.recvfrom(1024) 是不对的，udp才用这个，tcp是用accept以后的一对一的唯一socket直接recv
            while True:
                info = soc.recv(1024).decode('utf-8')
                flag = True
                for i in self._users.values():
                    if info in i['name']:
                        flag = False
                        break
                if flag:
                    soc.send(bytes('Y', encoding='utf-8'))
                    break
                else:
                    soc.send(bytes('N', encoding='utf-8'))
            self._users[addr] = {'socket': soc, 'name': info}
            print(f'{addr} connected. there\'s {len(self._users)} users.')
            t = Thread(target=self.recv, args=(soc, addr))
            t.start()
            self._thread_queue.append(t)

    def recv(self, soc:socket.socket, addr):
        name = self._users[addr]['name']
        hello = f'      {name} connected. there\'s {len(self._users)} users.      '
        self.broadCast(soc, hello)
        while True:
            try:
                response = soc.recv(1024)
                code = 'utf-8'
                try:
                    response = response.decode('utf-8')
                except UnicodeDecodeError as e:
                    response = response.decode('gbk')
                    code = 'gbk'
                name = self._users[addr]['name']
                msg = f'USER {name}: ' + response
                print(f'{addr} sent {response}')

                self.broadCast(soc, msg)
            except ConnectionResetError:
                print(f'{addr} exits. {len(self._users)-1} left.')
                name = self._users[addr]['name']
                s = f'   {name} exits. {len(self._users)-1} left.   '
                self.broadCast(soc, s)
                del self._users[addr]
                break

    def closeServer(self):
        for user in self._users.values():
            user['socket'].close()
        self._socket.close()
        exit(0)

    def broadCast(self, soc, msg):
        for s in self._users.values():
            if s['socket'] == soc:
                continue
            s['socket'].send(bytes(msg, encoding='utf-8'))

if __name__ == "__main__":
    server = Server()
    server.startServer()