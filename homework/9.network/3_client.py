import socket
def client():
    client_addr = ('192.168.220.1', 8888)
    server_addr = ('192.168.220.1', 8080)
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(client_addr)
    s = input('Client: ')
    # while True:
    soc.sendto(s.encode('utf-8'), server_addr)
    while True:
        data, addr = soc.recvfrom(1024)
        if data == b'#':
            soc.close()
            return
        try:
            data = data.decode('utf-8')
        except UnicodeDecodeError:
            data = data.decode('gbk')
        s = input(f'Received {data}. Client: ')
        soc.sendto(s.encode('utf-8'), server_addr)
        if s == '#':
            return

if __name__ == "__main__":
    client()