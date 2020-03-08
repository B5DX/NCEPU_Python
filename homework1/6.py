# 前面2个元素为0，1，输出100以内的斐波那契数列
Fibonacci = [0,1]

while True:
    temp = Fibonacci[-1] + Fibonacci[-2]
    if temp > 100:
        break
    Fibonacci.append(temp)

print(f"100以内的斐波那契数列为: {Fibonacci}")
