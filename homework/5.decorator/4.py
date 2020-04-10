# 4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
#      可以观看给的视频材料，仿照示例来做；
from math import sqrt, ceil
from time import perf_counter

def decorator(func):
    def main(*args):
        b = perf_counter()
        tmp = func(*args)
        e = perf_counter()
        print(func.__name__, 'takes', e-b, 'ms')
        return tmp
    return main

def isPrimeNum(num:int)->bool:
    if num == 2:
        return True
    for i in range(2, ceil(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

@decorator
def A():
    for i in range(2, 20001):
        if isPrimeNum(i):
            print(i, end=',')
@decorator
def B()->int:
    cnt = 0
    for i in range(2, 10001):
        if isPrimeNum(i):
            cnt += 1
    return cnt

@decorator
def C(M:int):
    cnt = 0
    for i in range(2, M+1):
        if isPrimeNum(i):
            cnt += 1
    return cnt


if __name__ == "__main__":
    A()
    print('this is the return of B', B())
    print('this is the return of C(100)', C(100))