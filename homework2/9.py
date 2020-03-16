# 9. 定义一个函数，函数接收一个数组
# 并把数组里面的数据从小到大排序(冒泡排序，也可以直接使用相关的函数)

def bubbleSort(lis: list) -> list:
    lis = lis.copy()
    for _ in range(len(lis)-1):
        for ind in range(len(lis)-1):
            if lis[ind] > lis[ind+1]:
                lis[ind], lis[ind+1] = lis[ind+1], lis[ind] 
    return lis

L = [11, 52, 6, 37, 43, 26, 8, 10, 9, 0, 4]
print(bubbleSort(L))