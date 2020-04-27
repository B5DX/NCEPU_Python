# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#   说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#   提示：要用到requests库，BeautifulSoup库
import requests
from bs4 import BeautifulSoup
import re
import os
os.chdir(os.path.dirname(__file__))

def main():
    outF = open('test.txt', 'w', encoding='utf-8')
    pat = []
    pat.append(re.compile(r'<a href="(.*)">.*(企业介绍|关于我们|企业发展|发展历史|企业概况).*</a>'))
    pat.append(re.compile(r'^(http|https):.*\.html'))
    pat.append(re.compile(r'^.*\.html'))
    with open('output.txt', 'r', encoding='utf-8') as f:
        for ind, line in enumerate(f):
            line = line.strip()
            getAbout(line, outF, pat)
            if ind%50 == 0:
                print(ind)
            if ind > 1000:
                break
    outF.close()

# <a href="http://www.cttp.net.cn/list-13-1.html">关于我们</a>
def getAbout(url, outputFile, rePattern):
    try:
        r = requests.get(url, timeout=(1,2))
        html = r.text
        res = rePattern[0].search(html)
        if res:
            target = res.group(1)
            for ind, i in enumerate(rePattern[1:]):
                cont = i.search(target)
                if cont:
                    if ind == 0:
                        outputFile.write(cont.group())
                    else:
                        outputFile.write(url + '/' + cont.group() + '\n')
                    break
            # outputFile.write('&&&' + url + ' ' + target + '\n')
    except Exception as e:
        # print(e)
        pass

if __name__ == "__main__":
    main()