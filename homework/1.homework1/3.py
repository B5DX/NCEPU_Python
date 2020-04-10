# 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出
from random import randint
L1 = [randint(0, 20) for i in range(10)]
L2 = [randint(0, 20) for i in range(10)]

print('Way1:', list(set(L1) & set(L2)))
print('Way2:', [i for i in L1 if i in L2])
print('Way3:', list(filter(lambda x: x in L2, L1)))