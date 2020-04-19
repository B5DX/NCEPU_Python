# 六  用面向对象,实现一个学生Python成绩管理系统;
#     学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#     实现对学生信息及成绩的增,删,改,查方法;
import os
import pickle as pk

class Student:
    __stuList = []
    __nums = []
    def __init__(self, cls, num, name, grade, *args):
        if num in Student.__nums:
            raise Exception('Duplicated Main Key(num)')
            return
        self.__cls = cls
        self.__num = num
        self.__name = name
        self.__grade = {
            'Python': int(grade)
        }
        if args == None: # normal create (else for load data)
            Student.__stuList.append(self)
            Student.__nums.append(num)
        
    def __setGrade(self, gradeDict):
        self.__grade = gradeDict

    def getName(self):
        return self.__name
    
    def getNum(self):
        return self.__num

    def addGrade(self, gradeName, grade):
        self.__grade[gradeName] = grade
    
    def delGrade(self, gradeName):
        if gradeName in self.__grade:
            del self.__grade[gradeName]
        else:
            raise Exception('Key not exist')
    
    def chGrade(self, gradeName, newGrade):
        if gradeName in self.__grade:
            self.__grade[gradeName] = newGrade
        else:
            raise Exception('Key not exist')
    
    def getGrade(self):
        return self.__grade

    @classmethod
    def save(cls):
        # os.remove('stuInfo.data')
        with open('stuInfo.data', 'wb') as f:
            pk.dump(len(cls.__stuList), f)
            for stu in cls.__stuList:
                L = (stu.__cls, stu.__num, stu.__name, stu.__grade)
                # print(L)
                for i in L:
                    pk.dump(i, f)
                
    @classmethod
    def load(cls):
        cls.__stuList = []
        if os.path.exists('stuInfo.data'):
            with open('stuInfo.data', 'rb') as f:
                num = pk.load(f)
                # print(num)
                for i in range(num):
                    L = []
                    for i in range(3):
                        L.append(pk.load(f))
                    s = Student(*L, 0, False)
                    s.__setGrade(pk.load(f))
                    cls.__stuList.append(s)

    @classmethod
    def addStu(cls):
        L = input('cls, num, name, grade(split by space):')
        L = L.split()
        cls.__stuList.append(Student(*L))

    @classmethod
    def findStudent(cls, num):
        for i in cls.__stuList:
            if i.__num == num:
                return i
        return None

    @staticmethod
    def test():
        Student.__stuList.append('WTF')
        print(Student.__stuList)

def testInput():
    stuNum = 1
    cls = 'PE1801'
    num = '120192020303'
    name = 'Jack'
    grade = {'Python':100}
    L = [stuNum, cls, num, name, grade]
    with open('stuInfo.data', 'wb') as f:
        for i in L:
            pk.dump(i, f) # pickle can automatically split different varibles



if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    # testInput()
    Student.load()
    s = Student.findStudent('120192020303')
    if s == None:
        testInput()
        Student.load()
        s = Student.findStudent('120192020303')
    while True:
        op = input(f'Current Student: {s.getName()}, num: {s.getNum()}\n\
Input operation: addGrade, delGrade, chGrade, getGrade, CS(change student) or exit:\n')
        if op == 'exit':
            Student.save()
            exit(0)
        elif op == 'addGrade':
            L = input('Input grade name and grade: ').split()
            print(L)
            s.addGrade(*L)
        elif op == 'delGrade':
            L = input('Input grade name: ')
            s.delGrade(L)
        elif op == 'chGrade':
            L = input('Input grade name and new grade: ').split()
            s.chGrade(*L)   
        elif op == 'getGrade':
            d = s.getGrade()
            for i in d:
                print(i, d[i])
        elif op == 'CS':
            num = input('Next student num: ')
            tmp = Student.findStudent(num)
            if tmp:
                s = tmp
                print('succeed')
                continue
            else:
                choose = input('not exist, want to creat?(y/n)')
                if choose == 'y':
                    Student.addStu()
                else:
                    continue
        else:
            print('wrong input')
