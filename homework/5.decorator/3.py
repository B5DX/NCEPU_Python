# 3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
from hashlib import md5

account = 'abc'
password = ''

def genePass():
    m = md5()
    m.update('123456'.encode('utf-8'))
    global password
    password = m.hexdigest()

def identify(func):
    def main(*args):
        acc = input('Input the account: ')
        if not acc == account:
            print('Wrong account')
            return
        m = md5()
        tmp = input('Input password to call the function: ')
        m.update(tmp.encode('utf-8'))
        if m.hexdigest() == password:
            func(*args)
        else:
            print('Failed')
    return main

@identify
def func():
    print('Call func successfully')

@identify
def fun():
    print('Call fun successfully')

if __name__ == "__main__":
    genePass()
    func()
    fun()