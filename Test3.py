# -*- encoding: utf-8 -*-
'''
@File : Test3.py
@Time : 2020/03/06 08:14:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#  定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;  主程序中,打印这个列表的地址(传参之前,传参之后);

def buy(weight: int, price: float) :
    return weight * price

def chList(L: list) :
    print(L)
    print("L重新赋值之前的地址:",id(L))
    L.append(233)
    print(L)
    print("L重新赋值后的地址:",id(L))

def lambdaTest(): #熟悉filter, map函数用法, 注意res需要list()一下才可直接打印
    L = [i for i in range(1, 21)]
    res = filter(lambda x: x%2!=0, L)
    print(list(res))

def test(x, *args):#学习join的用法（前面的str插孔加入到后面迭代器的序列)
    print("Hi,", ', '.join(args))

def argsTest(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    # w, p = map(float, input('Enter the weight and price:').split())
    # print(f'Pay {buy(w, p)}')
    
    # L = [1,2]
    # print(id(L))
    # chList(L)
    # print(id(L))

    # lambdaTest()
    # args = ('a'+'b')
    # print('a'+'b')
    # print(args)
    # print(*args)
    argsTest(1,2,3,a=1,b=2,c=3)