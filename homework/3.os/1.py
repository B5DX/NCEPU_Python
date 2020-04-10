# 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    L = []
    while True:
        cur = input()
        if cur == '':
            break
        L.append(cur)
    with open('input.txt', 'w') as f:
        f.write('\n'.join(L))