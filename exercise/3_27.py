# 序列化——转向一个字符串数据类型
# 此处的序列指的是字符串
# 因为数据存储和网络传输等情况只能读写字符串或者byte，因此要把某些东西转成字符串

# 从数据类型 -> 字符串类型  也就是序列化
# 从字符串 -> 数据类型  反序列化

# json *****
# pickle ****
# shelve (python 3 new module)

# json  通用的序列化格式
#       只有很少的数据类型能够通过json转化为字符串
# pickle  所有python数据类型
#       所有python数据类型都能转化成字符串形式
#       且部分反序列化依赖python代码（比如引入第三方包）
# shelve  使用序列化句柄直接操作，比较方便
#       

#json example
# 只有 数字、字符串、列表、字典、元组(实际上被转成了列表) 可以转换
dic1 = {'k1': 'v2'}
print(type(dic1))
import json
str_d = json.dumps(dic1) # dumps和loads是一次性读写, 想分次读可以加\n
print(type(str_d), str_d)
dic_d = json.loads(str_d)
print(type(dic_d), dic_d)

#file 
with open('jsonTest.txt', 'w', encoding='utf-8') as f:
    json.dump(dic1, f, ensure_ascii=False) #不影响读写，只是打开文件不方便看

with open('jsonTest.txt', 'r', encoding='utf-8') as f:
    dic_d = json.load(f)
    print(type(dic_d))

L = [{'a': 1}, {'b': 2}, {'c': 3}]
with open('jsonTest.txt', 'w', encoding='utf-8') as f:
    for dic in L:
        str_dic = json.dumps(dic)
        f.write(str_dic+'\n')
with open('jsonTest.txt', 'r', encoding='utf-8') as f:
    for line in f: #文件居然还能这样读写！！！（注意\n会被读进line）
        str_dic = json.loads(line.strip())
        print(str_dic)

# pickle使用方法和json一样
# open操作都要加参数'wb', 即都是二进制
# 可以分次dumps和loads，不需要想json一样手动做分行操作
# 只有json可以直接从文件看懂内容

import shelve 
f = shelve.open('shelveTest.txt', writeback=True) # writeback为True可以修改原文件，否则不可修改
f['key'] = {'a': 123, 'b': 333, 'c': 'wtf'}
f.close()
