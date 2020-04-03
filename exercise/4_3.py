# 练习1：利用闭包实现计数器
def createCounter():
    cnt = {'time': 0}
    def countFunc():
        cnt['time'] += 1
        return cnt['time']
    return countFunc
# 以下是不可改动的代码
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



# 练习2：定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;

def logFunc(func):
    def inner(a, b):
        print('call', func.__name__)
        return func(a, b)
    return inner

@logFunc
def addFunc(a:int, b:int):
    return a + b

if __name__ == "__main__":
    print(addFunc(1, 2))