#OS And Exception
import os

def oslist():
    print(os.getcwd())
    os.chdir('./learn/NCEPU_Python/')
    for root, dirs, files in os.walk(os.getcwd()): #对子目录也会进入并且递归遍历
        print(root)
        print(dirs)
        print(files)
    for names in os.listdir(os.getcwd()):
        if os.path.isdir(names):
            pass
        elif os.path.isfile(names):
            pass
        print(names)

def learnPath():
    # os.getcwd()
    # os.mkdir()
    # os.chdir()
    # os.rmdir()
    # os.rename()
    
    pwd = os.path.abspath('.')
    print( os.path.abspath(pwd + '/learn/') )
    print( os.path.basename(pwd + '/learn/NCEPU_Python') )
    print( os.path.dirname(pwd + '/learn/NCEPU_Python') )
    print( os.path.split(pwd + '/learn/NCEPU_Python') )
    print( os.path.join(pwd, 'learn', 'NCEPU_Python') )
   
    file = './learn/NCEPU_Python/Note.txt'
    print( os.path.normpath(file) )

def openFile():
    #abstract pathh
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    fileLocList = [os.path.abspath('.')+'\\test1.txt',
        '..\\test2.txt', 
        '..\\homework1\\test3.txt'
    ]
    with open(fileLocList[0], 'w') as f:
        pass
    with open(fileLocList[1], 'w') as f:
        pass
    with open(fileLocList[2], 'w') as f:
        pass
    for i in fileLocList:
        os.remove(i)

def readText():
    pwd = os.path.dirname(__file__)
    lines = []
    with open(pwd + '.\\3_18.txt', 'r', encoding='utf-8') as f:
        for curline in f.readlines():
            print(curline)
            lines.append(curline.split())
    # with open(pwd + '.\\3_18.txt', 'rb', encoding='utf-8') as fromFile:
    #     with open(pwd + '.\\3_18_copy.txt', 'wb', encoding='utf-8') as targetFile:
    #         targetFile.write(fromFile.read())
    lines[1:] = sorted(lines[1:], key=lambda line: line[2], reverse=True)

    with open(pwd + '\\3_18_out.txt', 'w', encoding='utf-8') as f:
        for curline in lines:
            s = '{}{}{}'.format(curline[0], curline[1].center(13, ' '), curline[2])
            print(s)
            f.write(s + '\n')


if __name__ == "__main__":
    # oslist()
    # learnPath()
    # openFile()
    readText()
