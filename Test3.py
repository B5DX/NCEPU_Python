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

if __name__ == "__main__":
    # w, p = map(float, input('Enter the weight and price:').split())
    # print(f'Pay {buy(w, p)}')
    L = [1,2]
    print(id(L))
    chList(L)
    print(id(L))