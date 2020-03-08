# -*- encoding: utf-8 -*-
'''
@File : 第二课.py
@Time : 2020/02/21 08:41:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random as rd

# a = 'c'
# print(a[0:-1], end='')

def experiment():
    #conduct experiment and return true if all the ball was throwed in the first cup
    ball = 3
    cup = [0, 0]
    for _ in range(ball):
        endNum = 100000
        choose = rd.randint(0, endNum)
        if choose < endNum/2:
            cup[0]+=1
        else :
            cup[1]+=1
    if(cup[0]==3):
        return (True, cup[0], cup[1])
    else:
        return (False, cup[0], cup[1])

def main():
    times = 100000
    cnt = 0
    for i in range(times):
        if experiment()[0]:
            cnt+=1
    print(float(cnt) *100 / times, end='%\n')

def encode():
    s = "the username is 'root', and the password is '123456'"
    for i in s:
        print(ord(i), end=' ')

def decode(s:str):
    s = s.split(' ')
    for i in s:
        print(chr(int(i)), end='')

def test(L:list):
    L[0]=22

if __name__ == "__main__":
    for _ in range(10):
        main()
    
    a = 'hello world'
    print(a.replace('cnn', 'wor').center(25, '_'))
    print(f'{a} has length', len(a))
    b = 12.1234
    print('test format : {0} and {1:.1f}'.format(a, b))
    print('name:{name}, b={num}'.format(name=a, num=b))

    # 列表的操作以及字符串格式化
    scores = [100, 75, 65, 95, 85, 99, 77, 86, 94, 60]
    print(f'Max: {max(scores)}')
    print(f'Min: {min(scores)}')
    cnt = sum(scores)
    print(f'Sum: {cnt}')
    print(f'Everage: {cnt/len(scores)}')

    # 元组练习
    tup = ('Jack', 'Mike', 'Jason')
    app_tup = ('John',)
    tup = app_tup + tup
    print(tup[:])
    print(f'Max is {max(tup)}')

    score = (50, 60, 70)
    print(f'Max {max(score)}')

    # 字典练习
    def test(D:dict):
        del D['Jack']
    stu = {'NO':120181080111, 'Name':'Jack', 'Class':'软件1801', 'Age':19}
    anoStu = {'张三':1234, '李四':2345, '王五':444, 'Jack':555, 'Mike':666}
    test(anoStu)
    
    seq = ('a', 'b', 'c')
    val = (1, 2, 3)
    dic = dict.fromkeys(seq, val)#是为每个key都附上同样的value
    print(dic)

    stu['n'] = 'new'
    stu['Name'] = 'Mike'
    del stu['Name']
    for i in stu.items():#一个列表，一个元素是一对key和val组成的元组
        print(i)
    for i in stu:#字典迭代是
        print(f'type of {i} is {type(i)}')
    # 字典索引可以是纯数字或者字符串
    dict1 = {x : x**2 for x in range(1, 4)}
    dict1[10] = 100
    dict1['hh'] = None
    print(dict1)

    L1 = ['name', 'No', 'sex']
    L2 = ['Jack', '123', 'male']
    for l, r in zip(L1, L2):
        print(f'{l} is {r}')

    for i in reversed(L2):
        print(i)
    for i in sorted(L2):
        print(i)

    #集合
    a = {1,2,'333',4}
    s = set([1,2,3,4,5,5,5])
    print(s)
    print(str(a|s), str(s-a), str(a&s), str(a^s))
    s = set('abcdfff')
    print(s)
    s = set({'a':1, 'b':2, 'c':3})#想想迭代器迭代的东西，就能想明白为什么是这个结果
    print(s)
    s.update([1,2], [3,4])
    print(s)