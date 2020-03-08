# 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资
# 将这10个员工，按照工资从高到低打印输出
Stuffs = [
    {'NO': 1, 'Name': "a", 'Age': 23,'Salary': 3500},
    {'NO': 2, 'Name': "b", 'Age': 22,'Salary': 3500},
    {'NO': 3, 'Name': "c", 'Age': 42,'Salary': 4500},
    {'NO': 4, 'Name': "d", 'Age': 12,'Salary': 5500},
    {'NO': 5, 'Name': "e", 'Age': 52,'Salary': 5500},
    {'NO': 6, 'Name': "f", 'Age': 22,'Salary': 6500},
    {'NO': 7, 'Name': "g", 'Age': 42,'Salary': 3500},
    {'NO': 8, 'Name': "h", 'Age': 22,'Salary': 8500},
    {'NO': 9, 'Name': "i", 'Age': 22,'Salary': 5500},
    {'NO': 10, 'Name': "j", 'Age': 32,'Salary': 2500}
]
Stuffs = sorted(Stuffs, key = lambda d: d['Salary'], reverse = True)
print('\n'.join([str(i)[1:-1] for i in Stuffs]))
