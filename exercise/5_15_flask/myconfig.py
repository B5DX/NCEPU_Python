DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'wrwzx'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'

# 'mysql+pymysql://root:'+password+'@localhost/test'
SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

POOL_SIZE = 5

MAX_OVERFLOW = 10

SQLALCHEMY_TRACK_MODIFICATIONS = True
