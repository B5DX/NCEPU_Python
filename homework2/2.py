# 2. 编写一个函数，接收n个数字，求这些参数数字的和
# 使用不定长参数

def multiSum(*args):
    return sum(args)

tup = (19, 33, 5, 37, 9)
print(multiSum(19, 33, 5, 37, 9))
print("传入元组调用:", multiSum(*tup))
