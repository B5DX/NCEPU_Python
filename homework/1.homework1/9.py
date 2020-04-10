# 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
import random as rd

N, maxNum = 10, int(input("Input the upper bound(minimum is 1), you can guess less than 10 times: "))
target = rd.randint(1,maxNum)

for i in range(N):
    tryNum = int(input("Input the number you guess:"))
    if tryNum == target:
        print(f"Congratulations！You guessed {i+1} times and finally get it!")
        break
    elif tryNum > target:
        print("Actual number is less than it.")
    else:
        print("Actual number is greater than it.")
else:
    print("Failed")