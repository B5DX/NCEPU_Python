# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class Student:
    def __init__(self, name, age, *grades):
        self.name = name
        self.age = age
        self.score = grades

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_score(self):
        return max(self.score) 
aa = Student('aa', 11, 22, 33, 44)
print(aa.get_age())
print(aa.get_name())
print(aa.get_score())

bb = Student('bb', 55, 66, 77, 88)
print(bb.get_name())
print(bb.get_age())
print(bb.get_score())