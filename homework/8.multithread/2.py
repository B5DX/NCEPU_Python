# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"
#   数据文件（1000个网址）：

import requests
from threading import Thread
import os, time
os.chdir(os.path.dirname(__file__))

rows = 1000
thread_num = 10

assert(rows / thread_num == rows // thread_num)

def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"

def readFile(path):
    urls = []
    with open('url_data.txt', 'r') as f:
        for line in f:
            urls.append(line)
    return urls

def tryConnect(begin, L):
    for url in L[begin: begin + rows // thread_num]:
        getHtmlText(url)
    
def main():
    threads = []
    step = rows // thread_num
    urls = readFile('url_data.txt')
    for i in range(thread_num):
        thr = Thread(target=tryConnect, args=(i*step,urls)) # target=容易忘记，忘记的话会报错提示group参数的问题！
        threads.append(thr)
        thr.start()
    for i in threads:
        i.join()
    print('finish')

if __name__ == "__main__":
    begin = time.perf_counter()
    main()
    end = time.perf_counter()
    print('time: ', end-begin)