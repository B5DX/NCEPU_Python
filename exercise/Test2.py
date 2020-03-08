# -*- encoding: utf-8 -*-
'''
@File : Test2.py
@Time : 2020/03/04 08:07:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# str1 = input("输入字符串转换成元组:(空格分隔)").split()
# print(tuple(str1))

# weight = int(input("The amount of apple you buy(kg):"))
# price = int(input('The price per kilogram(dollar):'))
# print(f'You should pay {price*weight} $.')

# username = input('username:') 
# password = input('password:') 
# print(username,password)

# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + \
#     age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
# print(info)

# info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary)
# print(info1)

# info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary)
# print(info)

# info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, name, age, skill, salary) 
# print(info)

# nums = list(range(10))
# print(nums)
# for i in nums:
#     if(i % 2 == 0):
#         print(i, end=' ')

# for i in range(2, 10):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(f'{i}是质数')

def test(a,*args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

test(1, 3, b=2)

ls = [1,2,3]
it = iter(ls)
print(next(it))