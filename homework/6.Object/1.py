# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
# 实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
from random import randint

# 理解property:
# print(Dog.color), 输出<property object at ...>, 如果使用Dog.color=..., 会改变property然后实例里面的也会改变
# print(Dog(1,1,1).color), 会根据property进行方法调用
# tips:
# python的__init__方法只有一个，后面的会覆盖前面的……

class Dog:
    def __init__(self, *args):
        if len(args) == 0:
            return
        c, n, p = args
        self.__info = {
            'color':c, 
            'number':n, 
            'price':p
        }

    def transact(self, num):
        cur = self.__info['number']
        if cur < num:
            # print('Deficient')
            return
        else:
            cur -= num
            self.__info['number'] = cur
            # print(cur, 'dogs left.')
    
    def setPrice(self, p):
        if p <= 0:
            print('Invalid price')
        else:
            self.__info['price'] = p
    def getPrice(self):
        return self.__info['price']
    
    def setNum(self, n):
        if n <= 0:
            print('Invalid number')
        else:
            self.__info['number'] = n
    def getNum(self):
        return self.__info['number']
    
    def setColor(self, c):
        self.__info['color'] = c
    def getColor(self):
        return self.__info['color']
    price = property(getPrice, setPrice)
    color = property(getColor, setColor)
    num = property(getNum, setNum)

if __name__ == "__main__":
    dogList = []
    for i in range(5):
        dogList.append(Dog('black', (i+1)*5, randint(100, 500)))
    dogList[1].color = 'white'
    dogList[3].color = 'brown'
    print('Initial:')
    for ind, i in enumerate(dogList):
        print('Dog', ind, i.price, i.color, i.num)
    for i in range(5):
        dogList[i].transact(randint(3, 15))
    print('After:')
    for ind, i in enumerate(dogList):
        print('Dog', ind, i.price, i.color, i.num)