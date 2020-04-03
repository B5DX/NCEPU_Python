# 1 定义一个10个元素的列表，
# 通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
# 提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)

from collections import deque
import time
from random import randint

data = [randint(0, 100) for i in range(1000)]

def cntTime(tp:str):
    if tp == 'list' :
        L = []
        # time.perf_counter()
        # time.process_time()
        listHeadInBegin = time.perf_counter()
        for i in data:
            L.insert(0, i)
        listHeadInEnd = time.perf_counter()
        listRearInBegin = time.perf_counter()
        for i in data:
            L.append(i)
        listRearInEnd = time.perf_counter()
    else:
        L = deque()
        listHeadInBegin = time.perf_counter()
        for i in data:
            L.appendleft(i)
        listHeadInEnd = time.perf_counter()
        listRearInBegin = time.perf_counter()
        for i in data:
            L.append(i)
        listRearInEnd = time.perf_counter()
    print(tp + '-headInsert:', str(listHeadInEnd - listHeadInBegin))
    print(tp + '-rearInsert:', str(listRearInEnd - listRearInBegin))

if __name__ == "__main__":
    cntTime("list")
    cntTime("deque")