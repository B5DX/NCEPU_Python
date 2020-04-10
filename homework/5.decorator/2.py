# 2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
import os
os.chdir(os.path.dirname(__file__))
import logging
from logging import handlers

sh = logging.StreamHandler()
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024, backupCount=5)
fh = handlers.TimedRotatingFileHandler(filename='2.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[fh,sh],
    level=logging.DEBUG
)

def callLog(func):
    def log(*args):
        logging.debug('Function "'+ str(func.__name__) + '" was called')
        func(*args)
    return log

@callLog
def test(a, b):
    print(a)
    print(b)

if __name__ == "__main__":
    test(1, 2)