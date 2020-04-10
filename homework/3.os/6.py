# 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
# 请读取文章内容,进行词频的统计;
# 并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);

import os

def readFiles() -> (str, str) :
    try:
        with open('cmp1.txt', 'r', encoding='utf-8') as f:
            cmp1 = f.read()
        with open('cmp2.txt', 'r', encoding='utf-8') as f:
            cmp2 = f.read()
    except FileExistsError:
        print(FileExistsError.args)
    # else:
    #     print('Read sucessfully')
    return (cmp1, cmp2)

def buildDict(wordList: list) -> dict :
    #return a dict that have count the frequency of words
    dic = dict()
    for word in wordList:
        if word in dic:
            dic[word] += 1
        else :
            dic[word] = 1
    return dic

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    cmp1, cmp2 = readFiles()
    cmp1, cmp2 = cmp1.lower(), cmp2.lower()
    tmpSet = set(cmp1) | set(cmp2)
    replaceSet = set()
    for i in tmpSet:
        if not i.isalnum():
            replaceSet.add(i)
    for i in replaceSet:
        cmp1.replace(i, ' ')
    cmp1 = cmp1.split()
    cmp2 = cmp2.split()
    #finish cuting words
    
    dict1 = buildDict(cmp1)
    dict2 = buildDict(cmp2)

    sortedDic1 = list(sorted(dict1, reverse=True, key=lambda dicKey: dict1[dicKey]))
    sortedDic2 = list(sorted(dict2, reverse=True, key=lambda dicKey: dict2[dicKey]))

    # for i in range(10):
    #     print(sortedDic1[i], str(dict1[sortedDic1[i]]), '|', sortedDic2[i], str(dict2[sortedDic2[i]]))
    try:
        length = 10
        set1 = set(sortedDic1[0:length])
        set2 = set(sortedDic2[0:length])
        intersection = set1 & set2
        rate = len(intersection) / length

        with open('cmpResult.txt', 'w') as f:
            for i in intersection:
                print(i)
                f.write(i+'\n')
            res = 'Repeatibility: {0: .2f}%'.format(rate * 100)
            print(res)
            f.write(res)
    except IndexError:
        print('please minus length.')