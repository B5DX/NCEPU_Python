import time
from functools import reduce

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def dev(a, b):
    return a / b

def operate(a, b, func):
    return func(a, b)

def ff(lis):
    def f():
        sum = 0
        for i in lis:
            sum += i
        return sum
    return f # 返回时，相关参数变量存在了返回的函数中

def notEmpty(s):
    return s.strip()

def out_closure():
    fs = []
    L = [3, 4]
    for i in range(1, 3):
        def f():
            print(L, id(L))
        fs.append(f)
        L.append(i)
    return fs

if __name__ == "__main__":
    # print(operate(5, 8, mul))
    
    # l = ['a','b','', ' ', 'c']
    # print(list(filter(notEmpty, l)))
    
    fs = out_closure()
    for i in fs:
        i()