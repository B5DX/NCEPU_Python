# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#     封装方法，求单个学生的总分，平均分，以及打印学生的信息。
class Student:
    def __init__(self, name, age, sex, *grades):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__grades = grades

    def getSum(self):
        return sum(self.__grades)
    
    def getAvr(self):
        return sum(self.__grades) / len(self.__grades)

    def getInfo(self):
        print('Name: {}, Sex: {}, Year:{}, Grades:{}'.format(self.__name, self.__sex, self.__age, ' '.join(map(str, self.__grades))))
    
a = Student('aa', 18, 'male', 55, 66, 88)
print(a.getSum())
print(f"{a.getAvr():.2f}")
a.getInfo()