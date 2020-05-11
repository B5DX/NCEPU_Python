# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

# id, content, name, datetime, is_deleted
# int, varchar(511), varchar(20), time, bit(1)

import pymysql as sql
from datetime import datetime

class SQL(object):
    def __init__(self, password):
        '''
        用于初始化创建connect和cursor对象，执行SQL语句
        :param password: 连接数据库的密码
        '''
        try:
            # 数据库名
            self.__base_name = 'test'
            # connect对象
            self.__db = sql.connect(
                'localhost',
                'root',
                password,
                self.__base_name
            )
            # 创建cursor，用于执行后续的SQL语句
            self.__cursor = self.__db.cursor()
            # 数据库中默认的操作表
            self.__default_table = 'message_board'
            # 默认表中的数据类型以及最大长度
            self.__datas = {
                'content': (str, 511),
                'name': (str, 20),
                'time': (str, 19),
                'is_deleted': (int, 1)
            }

        except Exception as e:
            print('connect failed.')
            exit(0)

    def __check(self, content=None, name=None, time=None):
        '''
        检查所给值是否符合表头数据类型和长度的要求
        :param content: content列内容，type=str, len < 511
        :param name: 留言人，type=str, len<20
        :param time: 留言时间，type=datetime, %Y-%m-%d %H:%M:%S, 使用datetime类，由getTime()获取
        :return: 无返回值，需要异常捕获
        '''
        L = [content, name, time]
        data_type = ['content', 'name', 'time']
        try:
            for ind, i in enumerate(L):
                if i != None:
                    tp = self.__datas[data_type[ind]]
                    assert isinstance(i, tp[0])
                    assert len(i) <= tp[1]
        except Exception as e:
            # print(data_type[ind])
            print('invalid data.')
            raise e

    def insert(self, content, name, time):
        '''
        插入数据，必须给出所有参数。is_deleted默认为0不可设置
        :return: 无返回值，已做异常处理
        '''
        try:
            self.__check(content, name, time)
        except Exception as e:
            return
        try:
            sqlcmd = f"INSERT INTO {self.__default_table} " \
                     f"(content, name, time, is_deleted) " \
                     f"VALUES ({repr(content)}, {repr(name)}, {repr(time)}, 0)"
            # print(sqlcmd)
            self.__cursor.execute(sqlcmd)
            self.__db.commit()
        except Exception as e:
            print('sql error.')
            return

    def delete(self, id):
        '''
        根据id删除数据
        删除即将is_deleted设为1，相当于移入垃圾桶，并未真正删除
        :param id: 删除id对应的行
        :return: 无返回，已做异常处理
        '''
        try:
            assert isinstance(id, int)
            self.__cursor.execute(f'UPDATE {self.__default_table} SET is_deleted=1 WHERE id={repr(id)}')
            self.__db.commit()
        except Exception as e:
            print('delete failed.')
            return

    def completeDelete(self, id):
        '''
        将数据从数据库删除
        需要先调用delete再调用此函数才能实现
        相当于把已经移入垃圾箱的信息彻底删除
        '''
        try:
            assert isinstance(id, int)
            self.__cursor.execute(f'DELETE FROM {self.__default_table} WHERE id={repr(id)} AND is_deleted=1')
            self.__db.commit()
        except Exception as e:
            print('delete failed.')
            return

    def update(self, id, new_content, new_time):
        '''
        针对对应id修改内容，用于用户修改留言内容，完成后会更新time到最新修改日
        '''
        try:
            assert isinstance(id, int)
            self.__check(content=new_content, time=new_content)
            cmd = f'UPDATE {self.__default_table} SET content={repr(new_content)}, time={repr(new_time)} WHERE id={id}'
            self.__cursor.execute(cmd)
            self.__db.commit()
        except Exception as e:
            print('update failed.')
            return

    def search(self, id=None, name=None):
        '''
        传入id或name或不传参
        一旦传入id则根据id查找
        否则，传入name根据name查找
        不传入则调出全部数据
        :return: 返回cursor.fetchall(): list
        '''
        try:
            # assert (id or name)
            if id:
                self.__cursor.execute(f'SELECT * FROM {self.__default_table} WHERE id={repr(id)} ORDER BY time DESC')
            elif name:
                self.__cursor.execute(f'SELECT * FROM {self.__default_table} WHERE name={repr(name)} ORDER BY time DESC')
            else:
                self.__cursor.execute(f'SELECT * FROM {self.__default_table}')
            return self.__cursor.fetchall()
            # print(f'SELECT * FROM {self.__default_table} WHERE name={repr(name)}')
        except Exception as e:
            print('invalid search index')
            raise e

    def exit(self):
        '''
        关闭数据库连接并退出程序
        '''
        try:
            self.__cursor.close()
            self.__db.close()
            print('exit finish.')
        except Exception as e:
            print('exit failed.')
        finally:
            exit(0)

def getTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def clearTable(sql:SQL):
    cmd = input('This operation will completely clear the whole table. Want to continue?(y/n)')
    if cmd == 'n':
        return
    for i in sql.search():
        sql.delete(i[0])
        sql.completeDelete(i[0])
    print('table cleared.')

if __name__ == '__main__':
    sql = SQL(input('input password to connect to DataBase: '))
    # clearTable(sql)
    sql.insert('first message', 'wzx', getTime())
    sql.insert('second message', '小明', getTime())
    sql.insert('你好', '张三', getTime())

    for line in sql.search(name='张三'):
        print(line)
        sql.delete(line[0])

    sql.update(sql.search(name='wzx')[0][0], 'changed', getTime())
    sql.exit()