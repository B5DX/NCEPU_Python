# 5. 写函数，检查传入字典的每一个value长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

def fun(dic):
    for k, v in dic.items():
        if len(v) > 2:
            dic[k] = v[0: 2]
    return dic

dic = {'a': [1,2,3,4,5], 'b': 'ssdlh', 'c': 123, 'd': (1,2,3,4)}
print(fun(dic))
