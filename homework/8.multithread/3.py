# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
from multiprocessing import Process
# from multiprocessing.queues import Queue  这是不可以的, 下面的引入才是正确的
from multiprocessing import Queue
from math import sqrt
from time import perf_counter

L = [i for i in range(1, 100001)]
Q = Queue()

def isPrimeNum(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def multiJudge(L, Q):
    cnt = 0
    for i in L:
        cnt += isPrimeNum(i)
    Q.put(cnt)

def decorator(func):
    def main(*args):
        non_multi_begin = perf_counter()
        cnt = func(*args)
        non_multi_end = perf_counter()
        print(f' {args[0] if len(args)!=0 else 1} process-> time: {non_multi_end - non_multi_begin}. cnt: {cnt}.')
    return main
@decorator
def nonMultiProcess():
    cnt = 0
    for i in L:
        cnt += isPrimeNum(i)
    return cnt

@decorator
def multiProcess(pro_num):
    processes = []
    step = len(L) // pro_num
    cnt = 0
    for i in range(pro_num):
        p = Process(target=multiJudge, args=(L[i*step:i*step+step], Q))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    while not Q.empty():
        cnt += Q.get()
    return cnt

if __name__ == "__main__":
    nonMultiProcess()
    multiProcess(2)
    multiProcess(4)
    multiProcess(10)