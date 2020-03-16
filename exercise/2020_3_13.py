#sorted是python内置函数，总是返回list，如果是字典则返回键的list
def learnSort(): 
    grades = {
        'a':85,
        'b':69,
        'c':63,
        'd':93,
        'e':58,
        'f':76,
        'g':88,
        'h':96,
        'i':35,
        'j':100
    }

    L = list(grades.items())
    s_L = sorted(L, key=lambda t: t[1], reverse=True) 
    _L = sorted(L, key=lambda t: (t[1], t[0])) #优先按照t[1]排序，当t[1]相同时根据t[0]排序
    L.sort(key=lambda t: t[1])

    for key, value in L:
        print(key, value)

def learnCount():
    L = [10, 50, 40, 60, 20, 30]
    sentence = 'You can do what you think you can.'
    res = {word: sentence.strip('.').split().count(word) for word in set(sentence.split())}
    for word, freq in res.items():
        print('{}: {}'.format(word, freq))

def test(): 
    pass

if __name__ == "__main__":
    # learnCount()
    pass
    