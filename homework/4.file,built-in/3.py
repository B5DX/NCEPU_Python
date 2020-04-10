# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX   
from hashlib import md5

if __name__ == "__main__":
    f = open('accounts.txt', 'w')
    for i in range(5):
        account = input("Input account and password:(password should not contain '#'): ")
        password = input()
        secr = md5()
        secr.update(password.encode('utf-8'))
        power = 'admin' if i == 0 else 'user'
        f.write(account+'#'+secr.hexdigest()+'\n')
    f.close()
    s = input('input the 1st password, we will check it:')
    f = open('accounts.txt', 'r')
    line = f.readline().strip()
    secr = md5()
    secr.update(s.encode('utf-8'))
    print(secr.hexdigest() == line[line.rindex('#')+1:])
    f.close()