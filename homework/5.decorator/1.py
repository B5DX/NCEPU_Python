# 1  编写一个装饰器，能计算其他函数的运行时间；
import time

def countTime(func):
    def getTime(times):
        begin = time.perf_counter()
        func(times)
        end = time.perf_counter()
        return end - begin
    return getTime

@countTime
def func(times) :
    for i in range(times):
        pass

if __name__ == "__main__":
    print(func(10000000))