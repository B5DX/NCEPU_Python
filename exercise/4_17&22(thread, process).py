from multiprocessing import Process, Pool # 多进程和进程池
import threading
import time
import os
import random

def saySorry():
    print("running")
    time.sleep(1)

g_num = 0
L = [11, 22]
mutex = threading.Lock()

class MyThread(threading.Thread): # 通过继承Thread创建线程
    def __init__(self, epoch):
        threading.Thread.__init__(self)
        self.epoch = epoch

    def run(self):
        global g_num
        print(threading.Thread.name, g_num)
        for i in range(self.epoch):
            mutex.acquire()
            g_num+=1
            mutex.release()

def anotherThread(epoch, id): # 通过函数创建线程
    global g_num
    for i in range(epoch):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print(threading.Thread.name, g_num)

def process(epoch, pid):
    # L.append(id)
    print(L)

def synchronization(): # 线程同步
    t1 = threading.Thread(target=anotherThread, args=(1000, 1))
    t2 = threading.Thread(target=anotherThread, args=(1000, 2))
    t3 = MyThread(1000)
    t1.start()
    t2.start()
    t3.start()
    time.sleep(1)
    print('finish')
    print(g_num)

def multiProcess():
    L.append('wtf')
    print(id(L))
    p1 = Process(target=process, args=(1000, 1)) # 为什么进去以后L没变？难道新进程只复制最初的主进程变量吗……
    p2 = Process(target=process, args=(1000, 2)) # 解释：其实是因为mutiProcess函数在创建Process的时候拷贝的主进程变量是函数之前的变量和状态，因此在mutiProcess这个函数之前的变动都会被拷贝进子进程，之后的则不会被记录（包括在本函数内部也就是函数名后的）
    p1.start()                                   # 可以试验将L.append()语句放在multiProcess之前就会有效，函数内和函数名后面都不行
    p2.start()                                   # 需要注意，如果在if __name__ == "__main__"里面直接创建进程则拷贝的是这句if之前的
    p1.join()
    p2.join()

def worker(thread_id):
    print(os.getpid(), 'thread_name:', thread_id)
    time.sleep(0.5)

def processPool():
    p = Pool(3) # 进程池中最大的进程数
    for i in range(5):
        p.apply_async(worker, args=(i, )) # 注意添加任务的方法，和直接创建新线程或新进程相似，千万不要以为是把创建好的进程放进去
    p.close() # 关闭进程池，不可再添加新任务
    p.join() # 主进程等待进程池中所有任务执行完毕



from multiprocessing import Queue
# 使用多进程安全的Queue进行通信
def write(q):
    L = [1,2,3,4,5]
    for i in L:
        q.put(i)
        time.sleep(0.1)

def read(q:Queue):
    while not q.empty():
        print('get', q.get())
        time.sleep(0.2)

def processComminicate():
    q = Queue() # 队列中最多存放3个元素，当empty\full（可以用方法判断）时进行get(True)\put(True)时会阻塞对应进程
                 # get\put第一个参数block代表是否可以阻塞，默认True。如果维False则一旦出现上述情况会触发异常
                 # 也可以传入最大等待时间参数timeout
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    # pr.terminate() # 主动结束进程pr(pr中没有退出循环条件，需要主动结束)



if __name__ == "__main__":
    # for i in range(5):
    #     t = threading.Thread(target=saySorry)
    #     t.start() #启动线程

    # synchronization()
    
    # multiProcess() 

    # processPool()

    processComminicate()