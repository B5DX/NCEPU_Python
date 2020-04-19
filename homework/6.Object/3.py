# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class DictClass():
    def __init__(self, dic:dict):
        self.__data = dic

    def del_dict(self, key):
        if key in self.__data:
            del self.__data[key]

    def get_dict(self, key):
        if key in self.__data:
            return self.__data[key]
        else:
            return "not found"

    def get_key(self):
        return self.__data.keys()
    
    def update_dict(self, newDic):
        for i in newDic:
            if i in self.__data:
                continue
            self.__data[i] = newDic[i]
        return self.__data.values()

if __name__ == "__main__":
    d = {'a':1, 'b':2, 'd':5}
    _d = {'c':3, 'b':4}
    d1 = DictClass(d)
    d1.del_dict('a')
    print(d1.get_dict('a'))
    print(d1.get_key())
    print(d1.update_dict(_d))
    print(d1.get_dict('b'))