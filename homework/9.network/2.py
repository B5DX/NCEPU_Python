# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
import socket
def udpReceiver():
    local_addr = ('192.168.220.1', 8080)
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(local_addr)
    while True:
        data, addr = soc.recvfrom(1024)
        if data == b'#':
            soc.close()
            return
        try:
            data = data.decode('utf-8')
        except UnicodeDecodeError as e:
            data = data.decode('gbk')
        print(data)

if __name__ == "__main__":
    udpReceiver()
