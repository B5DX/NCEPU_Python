# 7. 随机生成20个学生的成绩，判断这20个学生成绩的等级
# A -> 成绩 >= 90
# B -> 成绩在 [80, 90)
# C -> 成绩在 [70, 80)
# D -> 成绩 < 70

from random import randint

def judge(scores):
    L = []
    for i in scores:
        if i >= 90:
            L.append('A')
        elif i >= 80:
            L.append('B')
        elif i >= 70:
            L.append('C')
        else:
            L.append('D')
    return L

scores = [randint(40, 100) for _ in range(20)]
for id, (s, c) in enumerate(zip(scores, judge(scores))):
    print('NO.{} score: {} class:{}'.format(id, s, c))
