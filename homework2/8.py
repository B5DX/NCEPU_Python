# 8. 定义一个函数，给定一个字符串
# 找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数
# 例如，输入 aaaabbc，输出：a:4

def countMost(s: str):
    dic = {}
    maxNum = 0
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        maxNum = max(dic[i], maxNum)
    for k, v in dic.items():
        if v == maxNum:
            print(f'{k}: {v}')

countMost("aaaabbc")