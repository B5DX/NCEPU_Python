# 6. 定义一个函数, 打印输出n以内的斐波那契数列

def fib(n):
    a, b = 0, 1
    while b <= n:
        print(b)
        a, b = b, a + b

fib(10)