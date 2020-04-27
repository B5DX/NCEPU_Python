import re
# 正则表达式
def matchEmail(email:str):
    res = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$', email)
    # note: shoudn't be r'^...@163.com', '.' represents any char, so '\' is essential
    # match会从开头开始匹配，如果未必从开头要用search(search加上^就相当于match了)
    if res:
        return True
    else:
        return False
# 迭代器
class myStr:
    def __init__(self, s):
        self.s = s
    
    def __iter__(self):
        self.ind=-1
        return self

    def __next__(self):
        self.ind += 1
        if self.ind >= len(self.s):
            raise StopIteration
        return self.s[self.ind]

#生成器
def Fibonacci(n):
    a, b, cnt = 0, 1, 0
    while cnt < n:
        a, b = b, a+b
        cnt += 1
        yield (a, cnt)

# 下面写法与上方等价
# 生成器不可以raise StopIteration！！(我猜是因为生成器自动返回迭代器，是迭代器来负责raise)
# 如果是迭代器对象则__next__中要在需要终止的时候raise，for循环会在收到exception时自动结束
# 生成器是结束时直接退出函数即可，for循环不接收exception
def FibonacciStopException(n):
    a, b, cnt = 0, 1, 0
    while True:
        a, b = b, a+b
        cnt += 1
        if cnt > n:
            # raise StopIteration 报错， 直接结束函数return或者break就可以
            return
        yield (a, cnt)
        

if __name__ == "__main__":
    print(matchEmail('_wrwzx1@163.com'))
    print(matchEmail('wrwzx1@163.com'))

    s = myStr('wtf')
    for i in s:
        print(i, end='')
    else:
        print()
    # 以下是等价的循环方法
    s_iter = iter(s)
    while True:
        try:
            print(next(s), end='')
        except StopIteration:
            print()
            break

    for i in Fibonacci(10):
        print(i)
    for i in FibonacciStopException(5):
        print(i)

    # 等价for循环
    f = Fibonacci(5) # 直接由生成器返回迭代器，不需要用iter()
    while True:
        try:
            print(next(f), end='')
        except StopIteration:
            print()
            break

    f = FibonacciStopException(5)
    while True:
        try:
            print(next(f), end='')
        except StopIteration:
            print()
            break
    