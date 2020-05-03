# 1 将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具；
import socket
from multiprocessing import Process
# AF_INET用于Internet进程间通信，AF_UNIX用于同一台机器进程间通信
# SOCK_STREAM用于TCP协议，SOCK_DGRAM用于UDP协议

def udpSendTest():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('192.168.220.1', 8888)
    send_data = 'This is a udp test function.'
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    print(udp_socket.recv(1024))
    udp_socket.close()

def updReceiveTest():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('192.168.220.1', 8080)
    udp_socket.bind(local_addr) # 绑定端口
    recv_data = udp_socket.recvfrom(1024) # 表示本次接收的最大字节数
    print(recv_data)
    udp_socket.close()

def serverTest():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('192.168.220.1', 8080)
    udp_socket.bind(local_addr)
    while True:
        data, addr = udp_socket.recvfrom(1024)
        if data == b'exit':
            udp_socket.close()
            return
        # assert isinstance(data, bytes)
        data:bytes # 接收到的data是一个bytes对象，不是字符串！
        data = data.decode('utf-8') # 通过decode可以将data转为字符串
        print(f'receive from{addr}: {data}')
        s = f'Hello. I received you message {data}.'
        # 以下正确
        # udp_socket.sendto(s.encode('utf-8'), addr)
        # udp_socket.sendto(b'Hello. I received you message.', addr)
        # udp_socket.sendto(bytes(s.encode('utf-8')), addr) # 可以发送bytes
        # 以下不正确
        # udp_socket.sendto(u'Hello', addr) # 不可裸字符串u
        # udp_socket.sendto(bytes(s), addr) 字符串必须encode才可转为bytes

def tcpTest():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('www.sina.com.cn', 80)) # 建立连接
    tcp_socket.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = tcp_socket.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    tcp_socket.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('sina.html', 'wb') as f:
        f.write(html)

if __name__ == "__main__":
    # udpSendTest()
    # updReceiveTest()
    # serverTest()
    tcpTest()