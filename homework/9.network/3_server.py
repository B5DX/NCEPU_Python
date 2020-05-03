# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
import socket
def server():
    server_addr = ('192.168.220.1', 8080)
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(server_addr)
    while True:
        data, addr = soc.recvfrom(1024)
        if data == b'#':                
            soc.close()
            return
        try:
            data = data.decode('utf-8')
        except UnicodeDecodeError:
            data = data.decode('gbk')
        s = input(f'Received {data}. Server: ')
        soc.sendto(s.encode('utf-8'), addr)
        if s == '#':
            return

if __name__ == "__main__":
    server()