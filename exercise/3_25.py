import os, sys, time

os.system('cls') #清屏

file = r'F:\test\testPy.txt' # raw string
print(file)

def listDirs(dirPath:str)->list:
    tmpList = []
    for name in os.listdir(dirPath):
        f = os.path.join(dirPath, name)
        if os.path.isdir(f):
            tmp = listDirs(f)
            if len(tmp) == 0:
                continue
            else:
                tmpList.append(tmp)
        else:
            tmpList.append(f)
    return tmpList

def jindu(): #??not good
    for i in range(21):
        sys.stdout.write('\n')
        sys.stdout.write(' {}%    {}'.format(int(i/20 * 100), i*4*'*'))
        sys.stdout.flush()
        time.sleep(0.1)

def copyFiles(src:str, dist:str):
    #copy files from srcDir to distDir, except dirs
    try:
        os.mkdir(dist)
    except FileExistsError:
        pass

    L = []
    for name in os.listdir(src):
        curFile = os.path.join(src, name)
        if os.path.isdir(curFile):
            continue
        else:
            L.append(curFile)
    for f in L:
        distFile = os.path.join(dist, os.path.basename(f))
        if os.path.exists(distFile):
            continue
        with open(f, 'rb') as rf:
            with open(distFile, 'wb') as wf:
                wf.write(rf.read())


def doSth():
    for i in range(1000):
        pass

from datetime import datetime

def learnDatetime():
    #注意！是datetime里的datetime！
    d = datetime.now().replace(microsecond=0)
    print(d)

    d1 = datetime.now()
    doSth()
    d2 = datetime.now()
    print((d1-d2))

import collections
def learnColle():
    Point = collections.namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)

if __name__ == "__main__":
    # L = listDirs(r'F:\Py Project\Learn\NCEPU_Python')
    # print(L)

    # print(sys.argv[0])
    # print(__file__)
    # print(dir(sys))

    # jindu()

    # copyFiles(r'F:\Py Project\Learn\NCEPU_Python', r'F:\Py Project\Learn\NCEPU_Python\test')
    # print('finish')
    
    # learnDatetime()

    learnColle()