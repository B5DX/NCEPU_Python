# 1  有100个同学的分数：数据请用随机函数生成；
#    A 利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#    B 利用线程池来实现；

from threading import Thread
from random import randint
from concurrent.futures import ThreadPoolExecutor # 线程池模块

students = [randint(50, 100) for _ in range(100)]
thread_num = 10
assert(len(students) / thread_num == len(students) // thread_num)

def printInfo(begin):
    for i in range(len(students) // thread_num):
        print(students[i+begin])

def A():
    step = len(students) // thread_num
    threads = [Thread(target=printInfo, args=(i*step,)) for i in range(thread_num)]
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()
    print('finish A')

def B():
    pool = ThreadPoolExecutor(4)
    step = len(students) // thread_num
    futures = []
    for i in range(thread_num):
        future = pool.submit(printInfo, *(i*step,)) # 类似创建线程
        futures.append(future) # 用于后面遍历调用result
    pool.shutdown(wait=True)
    for future in futures:
        future.result() # 不调用result不会输出结果（不懂）
    print('finish B')


if __name__ == "__main__":
    A()
    B()