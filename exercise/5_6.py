#设置密码输入，显示为******
import msvcrt,sys
def pwd_input():    
    chars = []   
    while True:  
        try:  
            newChar = msvcrt.getch().decode(encoding="utf-8")  
        except:  
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")  
        if newChar in '\r\n': # 如果是换行，则输入结束               
             break   
        elif newChar == '\b': # 如果是退格，则删除密码末尾一位并且删除一个星号   
             if chars:    
                 del chars[-1]   
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光标回退一格  
                 msvcrt.putch( ' '.encode(encoding='utf-8')) # 输出一个空格覆盖原来的星号  
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光标回退一格准备接受新的输入                   
        else:  
            chars.append(newChar)  
            msvcrt.putch('*'.encode(encoding='utf-8')) # 显示为星号  
    return (''.join(chars) )  
  
print("Please input your password:")
pwd = pwd_input()

import mysql.connector as sql

conn = sql.connect(
    host='localhost',
    user='root',
    passwd=pwd,
    database='test'
)

# 创建cursor对象，用来发送SQL命令，操作数据库
cursor = conn.cursor()

cursor.execute('CREATE TABLE user (id varchar(10), name varchar(20))')
# cursor.execute('INSERT INTO user (id, name) (%s, %s)', ('1', 'Mike'))

# 关闭cursor和connect对象
conn.commit()
cursor.close()


