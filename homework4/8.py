# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

from random import randint
from collections import Counter

def geneData(name:str, line:int):
    head = '172.25.254.'
    with open(name, 'w') as f:
        for _ in range(line-1):
            f.write(head+str(randint(1, 254))+'\n')
        f.write(head + str(randint(1, 254)))

def count(name:str):
    cnt = Counter()
    with open(name, 'r') as f:
        tmp = f.read()
        tmp = tmp.strip().split('\n')
        for i in tmp:
            cnt[i] += 1
    return sorted(cnt, key=lambda dicInd: cnt[dicInd], reverse=True)[:10]

if __name__ == '__main__':
    name = 'ip.txt'
    geneData(name, 1200)
    print('\n'.join(count(name)))