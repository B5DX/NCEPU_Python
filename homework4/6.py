# 6  通过Python来实现显示给定文件夹下的所有文件和文件夹,
# 以及时间，如果是文件，显示大小; 输出格式效果如下:
import os
import time

space_args = {
    'Name': 15,
    'Date': 20,
    'Type': 8,
    'Size': 6
}

def padding(ind:str, length:int)->str:
    return ' '*(space_args[ind] - length)

def showDir(path):
    files = os.listdir(path)
    for ind in space_args:
        print(f'{ind}', end=padding(ind, len(ind)))
    print()
    for file in files:
        fileInfo = os.stat(file)
        Name = file
        Date = time.localtime(fileInfo.st_atime)
        L1 = [Date.tm_year, Date.tm_mon, Date.tm_mday]
        L2 = [Date.tm_hour, Date.tm_min, Date.tm_sec]
        Date = '-'.join(list(map(lambda x: str(x), L1))) + ' ' + ':'.join(list(map(lambda x: str(x), L2)))
        Type = 'Folder' if os.path.isdir(file) else 'File'
        Size = fileInfo.st_size / 1024
        for ind in space_args:
            if ind == 'Size':
                continue
            print(f'{eval(ind)}', end=padding(ind, len(str(eval(ind)))))
        print(f'{Size:.1f}kb')

if __name__ == '__main__':
    showDir(os.path.dirname(__file__))