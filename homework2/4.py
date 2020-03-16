# 4. 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符并返回结果

# 返回(letter, number, space, other)
def count(s: str)->tuple:
    letter, number, space, other = 0, 0, 0, 0
    for cur in s:
        if cur.isalpha():
            letter += 1
        elif cur.isdigit():
            number += 1
        elif cur == ' ':
            space += 1
        else:
            other += 1
    return letter, number, space, other

test = "Tshg3828 293g\n wi92.*)#"
print('letter: {0}\nnumber: {1}\nspace: {2}\nother: {3}'.format(*count(test)))
