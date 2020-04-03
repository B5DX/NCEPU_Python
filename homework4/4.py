# 4  (继续上面的练习) 模拟用户登录:
# 5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
# 系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  
# 如果都正确,打印提示, 您登录成功(失败);

import os
from hashlib import md5
from random import randint
os.chdir(os.path.dirname(__file__))

def strToHash(text:str) -> str:
    # 千万注意！必须新建一个对象，同一个md5按照不同顺序对同一个字符串处理结果不同！！！
    secr = md5() 
    secr.update(text.encode('utf-8'))
    return secr.hexdigest()  

if __name__ == "__main__":
    L = [chr(i) for i in range(ord('a'), ord('z')+1)]
    print('Input name, account, password (shouldn\'t contain \' \')')
    for i in range(1):
        name = input(f'Input for the {i+1}th student:\n')
        account = input()
        password = input()
        assert((name+account+password).find(' ') == -1)
        with open('accounts.txt', 'a') as f:
            f.write(name+' '+account+' '+strToHash(password)+'\n')
    cache = str()
    with open('accounts.txt', 'r') as f:
        cache = f.read().strip()
    cache = cache.split('\n')
    name = input('Input name: ')
    for ind, data in enumerate(cache):
        data = data.strip().split(' ')
        cache[ind] = data 
        if name in data:
            break
    else:
        print("Can't find name!")
        exit(0)
    account = input('Input account: ')
    if not data[1] == account:
        print("Wrong account!")
        exit(0)
    password = input('Input password: ')
    if not data[2] == strToHash(password):
        print("Wrong password!")
        exit(0)
    print('Succeed!')