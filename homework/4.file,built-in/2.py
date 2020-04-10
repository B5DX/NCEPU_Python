# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
# 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

from datetime import datetime

if __name__ == "__main__":
    str_date = input('Input a date(2020-03-29): ').replace('-', '')
    date = datetime.strptime(str_date, r'%Y%m%d')
    calen = date.isocalendar()
    print('这是{}的第{}周，是周{}'.format(calen[0], calen[1], calen[2]))

    Y = str_date[:4]
    beginDate = datetime(int(Y), 2, 17)
    endDate = datetime(int(Y), 8, 23)
    if beginDate <= date <= endDate:
        beginCalen = beginDate.isocalendar()
        print('这是我校校历的第{}周'.format(calen[1] - beginCalen[1] + 1))