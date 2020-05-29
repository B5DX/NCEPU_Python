# 4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
#     文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
# https://www.programcreek.com/python/example/56591/matplotlib.pyplot.plot

import requests
from bs4 import BeautifulSoup
import os


class Examples(object):
    def __init__(self, url):
        # 伪装成浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '74.0.3724.8 Safari/537.36'
        }
        self.url = url
        self.html = requests.get(url, headers=self.headers).text
        self.bs = BeautifulSoup(self.html, features='lxml')

    def __iter__(self):
        # self.ind = 0
        self.all_pre = iter(self.bs.find_all('pre'))
        self.all_td = iter(self.bs.find_all(self.__is_exam_td))
        return self

    def __next__(self) -> (dict, str):
        # cur_td = self.all_td[self.ind]
        cur_td, cur_pre = next(self.all_td), next(self.all_pre)
        td_attrs = {}
        flag = None
        for i in self.iter_child(cur_td):
            if flag is not None:
                td_attrs[flag] = str(i.string).strip()
                flag = None
            if 'Project' in i:
                flag = 'Project'
                continue
            elif 'Author' in i:
                flag = 'Author'
                continue
            elif 'File' in i:
                flag = 'File'
                continue

        return td_attrs, cur_pre.string

    @staticmethod
    def __is_exam_td(tag):
        return tag.name == 'td' and 'Project' in tag.next

    @staticmethod
    def iter_child(td):
        s = ''
        for i in td.children:
            if 'File' in s:
                # 说明上一行是File，目前的i.span就是文件名所在的地方
                yield i.span
            s = str(i).strip()
            if s == '':
                # 去除空行
                continue
            yield i


def main():
    os.chdir(os.path.dirname(__file__))
    file_name = 'examples.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        example = Examples('https://www.programcreek.com/python/example/56591/matplotlib.pyplot.plot')
        for ind, (td_attrs, code) in enumerate(example):
            if ind != 0:
                f.write('***************************************' + '\n')
            f.write(f'Example {ind + 1}' + '\n')
            for key, v in td_attrs.items():
                f.write(f'{key}: {v}' + '\t')
            else:
                f.write('\n')
            f.write(code + '\n')
    print('finish', ind)


if __name__ == '__main__':
    main()
