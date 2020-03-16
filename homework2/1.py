# 1. 写函数判断用户传入的对象（字符串、列表、元组）长度并返回给调用者

def size(obj):
    return len(obj)

L = [1, 3, 5, 7]
T = (3, 6, 9, 12)
print("列表长度:", length(L))
print("字符串长度:", length("Test String"))
print("元组长度:", length(T))
