# 3. 编写一个函数, 传入一个数字列表, 输出列表中的奇数
# 数字列表请用随机数函数生成

from random import randint

def printOdd(L):
    for i in L:
        if i % 2 == 1:
            print(i, end=' ')

L = [randint(0, 100) for _ in range(10)]
printOdd(L)
