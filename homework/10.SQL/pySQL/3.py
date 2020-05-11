# 3  对2中的表结构，用SQLAchemy模块来实现同样的操作；

from sqlalchemy import Column, String, DATETIME, INTEGER, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def getTime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

# 创建对象基类
Base = declarative_base()

class Message(Base):
        # 表名
        __tablename__ = 'message_board'

        id = Column(INTEGER(), primary_key=True)
        content = Column(String(511))
        name = Column(String(20))
        time = Column(DATETIME())
        is_deleted = Column(INTEGER())

def check(content=None, name=None, time=None):
    '''
    检查所给值是否符合表头数据类型和长度的要求
    :param content: content列内容，type=str, len < 511
    :param name: 留言人，type=str, len<20
    :param time: 留言时间，type=datetime, %Y-%m-%d %H:%M:%S, 使用datetime类，由getTime()获取
    :return: 无返回值，需要异常捕获
    '''
    datas = {
        'content': (str, 511),
        'name': (str, 20),
        'time': (str, 19),
        'is_deleted': (int, 1)
    }
    L = [content, name, time]
    data_type = ['content', 'name', 'time']
    try:
        for ind, i in enumerate(L):
            if i != None:
                tp = datas[data_type[ind]]
                assert isinstance(i, tp[0])
                assert len(i) <= tp[1]
    except Exception as e:
        print('invalid data.')
        raise e

def decorator(func):
    def res(*args):
        try:
            func(*args)
        except Exception as e:
            print('operation failed.')
            print(e)
    return res

class SQL:
    def __init__(self, password):
        self.__tablename = Message.__tablename__
        self.__engine = create_engine('mysql+pymysql://root:' + password + '@localhost/test')
        self.__DBSession = sessionmaker(bind=self.__engine)
        self.__session: Session = self.__DBSession()

    @decorator
    def insert(self, content, name, time):
        # 由于主键id默认了自增加，所以新建时为写id的值
        new_message = Message(content=content, name=name, time=time, is_deleted=0)
        self.__session.add(new_message)
        self.__session.commit()

    def search(self, id=None, name=None):
        session = self.__session
        if isinstance(id, int):
            res =  session.query(Message).filter(Message.id==id).all()
        elif isinstance(name, str):
            res =  session.query(Message).filter(Message.name==name).all()
        else:
            res =  session.query(Message).all()
        return res

    @decorator
    def update(self, id, new_content, new_time):
        self.__session.query(Message).filter(Message.id==id).update({'content':new_content, 'time':new_time})
        self.__session.commit()

    @decorator
    def delete(self, id):
        self.__session.query(Message).filter(Message.id==id).update({'is_deleted':1})
        self.__session.commit()

    @decorator
    def completeDelete(self, id=None):
        if not id:
            return
        session = self.__session
        session.query(Message).filter(Message.is_deleted==1, Message.id==id).delete()
        session.commit()

    @decorator
    def clearRecycleBin(self):
        session = self.__session
        session.query(Message).filter(Message.is_deleted==1).delete()
        session.commit()

    @decorator
    def close(self):
        self.__session.close()


if __name__ == '__main__':
    sql = SQL(input('Input password to connect DataBase: '))
    sql.insert('test', '小明', getTime())
    sql.delete(10)
    sql.update(1, 'changed', getTime())
    for msg in sql.search(name='wzx'):
        msg: Message
        print(msg.content)
    sql.close()