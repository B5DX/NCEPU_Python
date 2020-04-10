# 给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出
text = 'legitimate conscious solidify refuge\
 refuge hybrid commute legitimate'

words = text.split(' ')
d = {}
for cur in words:
    if cur in d:
        d[cur] += 1
    else:
        d[cur] = 1

ans = sorted(d.items(), key = lambda x: x[1], reverse = True)
print('\n'.join([(str(i))[1: -1] for i in ans]))