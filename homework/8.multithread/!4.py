# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；另外一个进程接收并打印消息；
from multiprocessing import Queue, Process, Lock
import sys, os

# python中子进程是不可以input的，默认标准输入只能在父进程，一个解决办法是将标准输入描述符，传入子进程函数：
def sender(Q:Queue, fileno, printloc:Lock):
    sys.stdin = os.fdopen(fileno)
    while True:
        printloc.acquire()
        tmp = input('please input str(# to exit): ')
        printloc.release()
        Q.put(tmp)
        if tmp == '#':
            print('finish send')
            return
        
def receiver(Q:Queue, printloc:Lock):
    while True:
        if not Q.empty():
            printloc.acquire()
            while not Q.empty():
                flag = 1
                tmp = Q.get()
                if tmp == '#':
                    print('finish receive')
                    return
                print(tmp)
            printloc.release()

# 使用sys.stdin.fileno()获取标准输入描述符可以解决，但是不懂还麻烦，还不如主进程接受输入……
# if __name__ == "__main__":
#     Q = Queue(5)
#     mutex = Lock()
#     fn = sys.stdin.fileno() # 不懂
#     sendProcess = Process(target=sender, args=(Q, fn, mutex))
#     receiveProcess = Process(target=receiver, args=(Q, mutex))
#     sendProcess.start()
#     receiveProcess.start()
#     sendProcess.join()
#     receiveProcess.join()
#     print('finish all')

# 建议父进程作为sender，就不会遇到无法input的问题
if __name__ == "__main__":
    Q = Queue()
    mutex = Lock() # 用锁保证receiver输出与input提示语不冲突
    rec = Process(target=receiver, args=(Q,mutex))
    rec.start()
    while True:
        mutex.acquire()
        tmp = input('please input str(# to exit): ')
        mutex.release()
        Q.put(tmp)
        if tmp == '#':
            print('finish send')
            break
    rec.join()
    print('finish all')