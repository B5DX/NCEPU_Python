# 10. 编写一个函数calculate, 可以实现2个数的运算（加、减、乘、除）

def calculate(a, b, operation):
    if operation == 'ADD':
        return a + b
    elif operation == 'SUB':
        return a - b
    elif operation == 'MUL':
        return a * b
    elif operation == 'DEV':
        return a / b
    else:
        print("Wrong Operation")
        return None

print('10 + 25 =', calculate(10, 25, 'ADD'))
print('5 / 2 =', calculate(5, 2, 'DEV'))
print('44 * 4 =', calculate(44, 4, 'MUL'))