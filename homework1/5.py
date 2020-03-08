# 使用random模块，生成随机数，来初始化一个列表，元组
import random as rd

L = []
T = ()
for i in range(20):
    L.append(rd.randint(1,50))
    T += (rd.randint(1,50),) #注意此方法
print(f"随机列表：{L}")
print(f"随机元组：{T}")