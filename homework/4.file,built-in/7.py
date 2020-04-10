# 7 使用python代码统计一个文件夹中所有文件的总大小
import os

def totalSize(path):
    sum = 0
    for file in os.listdir(path):
        sum += os.stat(file).st_size
    return sum

if __name__ == '__main__':
    print('{0:.2f} kb'.format(totalSize(os.path.dirname(__file__))/1024))