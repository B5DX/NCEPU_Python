a = 10

def test1():
    b = a
    a = 1

def test2(): # only this function is correct
    b = a
    print(b)

def test3():
    b = a
    a = b+1

def test4():
    a = a + 1 # will raise Error
    print(a)

# test4()
# 解释：由于先从局部域寻找变量，当在函数内找到a后便不再向外寻找，然后发现局部a未定义故会报错，因此global的a根本未被发现

print(__name__)
