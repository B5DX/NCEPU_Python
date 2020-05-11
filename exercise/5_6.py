import pymysql as pm
import traceback

db = pm.connect(
    host='localhost',
    user='root',
    passwd='wrwzx',
    database='test'
)

# 创建cursor对象，用来发送SQL命令，操作数据库
cursor = db.cursor()

# cursor.execute('CREATE TABLE user (id varchar(10), name varchar(20))')

# id(主键)会自动增长，因此插入时可以不写主键
sql = """INSERT INTO user (id, name, age)
        VALUES('1', 'John', 20)
        """

# 进行数据交互的时候要异常处理！
try:
    cursor.execute(sql)
    db.commit() # 提交到数据库
except Exception as e:
    print(e)
    # 将异常输出到日志文件
    f = open('log.txt', 'w')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
finally:
    # 关闭cursor和connect对象
    cursor.close()
    db.close()
    
    
# 使用SQLAlchemy    
from sqlalchemy import Column, String, LargeBinary, DATETIME, INTEGER, create_engine
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
    is_deleted = Column(LargeBinary())


password = 'wrwzx'
# create_engine()初始化数据库连接，字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:'+password+'@localhost/test')
# 创建DBSession类型
# 由于有了ORM，想数据库添加一行记录可以视为添加一个Message对象
DBSession = sessionmaker(bind=engine)
# 以上代码完成SQLAlchemy初始化和具体每个表class定义。如果有多个表就继续定义其他class

def insert(content, name, time):
    # 由于主键id默认了自增加，所以新建时为写id的值
    new_message = Message(content=content, name=name, time=time, is_deleted=0)
    # 关键是获取session，然后把对象添加到session，最后提交并关闭
    # DBSession可视为当前数据库连接
    session = DBSession()
    session.add(new_message)
    session.commit()
    session.close()

def search(id=None, name=None):
    session: Session = DBSession()
    res = None
    if id_:
        res =  session.query(Message).filter(Message.id==id).all()
    elif name:
        res =  session.query(Message).filter(Message.name==name).all()
    else:
        res =  session.query(Message).all()
    return res

