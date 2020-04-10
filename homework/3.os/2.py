# 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open('input.txt', 'r') as f:
        tmp = f.read()
    for ind, data in enumerate(tmp.split('\n')):
        if data == '': 
            continue
        print(f'第{ind+1}行： {data}')