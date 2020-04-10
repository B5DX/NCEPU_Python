# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数);
# 然后按照分数从高到低进行排序输出

import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    try:
        with open('Students.txt', 'r') as f:
            tmp = f.read()
            tmp = tmp.split('\n')
            tmp = list(map(lambda lis: lis.split(','), tmp))
            tmp = sorted(tmp, reverse=True, key=lambda line: int(line[-1][-2:]))
        with open('StudentsSorted.txt', 'w', encoding='utf-8') as f:
            f.write('学号        姓名        Python分数'+'\n')
            for line in tmp:
                f.write(f'{line[0]}        {line[1]}        {line[2]}\n')
    except FileExistsError:
        print("File doesn't exist")
    else:
        print('Finish')
