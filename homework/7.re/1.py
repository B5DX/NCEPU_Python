# 1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#   提示，文件有1000行，注意控制每次读取的行数；
import re
import os
os.chdir(os.path.dirname(__file__))

def main():
    f_write = open('output.txt', 'w', encoding='utf-8')
    with open('webspiderUrl.txt', 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f:
            res = re.search(r"'(http|https)://.*'", line)
            # 'http://www.skandia-bsam.cn'
            if res:
                res = re.split(r'(?:;\s|;|<br>)', res.group()[1:-1])
                cnt += 1
                f_write.write('\n'.join(res))
                f_write.write('\n')
            else:
                print(line.strip())
    print('finish\n' + f'cnt={cnt}')
    f_write.close()

if __name__ == "__main__":
    main()