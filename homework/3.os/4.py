# 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
# 将当前img目录所有以.png结尾的后缀名改为.jpg.
import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    try:
        os.mkdir('./img')
    except FileExistsError:
        print("Directory already exists. Continue to execute.")
    os.chdir('./img')
    for i in range(1, 10+1):
        with open(str(i)+'.png', 'wb') as f:
            pass
    print('Create successfully.')

    try:
        for file in os.listdir(os.getcwd()):
            os.rename(file, file[: file.rindex('.')] + '.jpg')
    except FileExistsError:
        print("File doesn't exist.")
    else:
        print('Finish')