# 5  通过Python来模拟实现一个txt文件的拷贝过程;

import os

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

if __name__ == "__main__":
    dist = os.path.join(os.getcwd(), 'output')
    os.mkdir(dist)
    copyFiles(os.path.dirname(__file__), dist)