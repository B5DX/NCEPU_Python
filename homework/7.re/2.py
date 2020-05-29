# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#   说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#   提示：要用到requests库，BeautifulSoup库
import requests
from bs4 import BeautifulSoup
import re
import os
os.chdir(os.path.dirname(__file__))


def main():
    output_file = open('about.txt', 'w', encoding='utf-8')
    cnt = 0
    with open('output.txt', 'r', encoding='utf-8') as f:
        for ind, line in enumerate(f):
            line = line.strip()
            try:
                r = requests.get(line, timeout=(1, 1))
                html = r.text
                soup = BeautifulSoup(html, features='lxml')
                for i in soup.find_all('a'):
                    res = re.search(r"(我们|关于|介绍|历史|概况|企业)", str(i))
                    if res is not None:
                        url = i.attrs['href']
                        if 'www.' in url:
                            print(url)
                            output_file.write(url + '\n')
                        else:
                            print(line + url)
                            output_file.write(line + url + '\n')
                        # print(str(i).replace('\n', ' '))
            except Exception:
                cnt -= 1
                continue
            finally:
                cnt += 1
                if cnt == 100:
                    output_file.close()
                    return

                if ind % 20 == 0:
                    print(ind)
                    # exit()
                if ind > 1000:
                    break
    output_file.close()


if __name__ == "__main__":
    main()
