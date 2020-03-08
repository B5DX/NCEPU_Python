#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数
from math import sqrt
def isPrimeNum(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    L = [i for i in range(51)]
    print(f'Odd number: {str([i for i in L if i%2 == 1])}')
    print(f'Even number: {str([i for i in L if i%2 == 0])}')
    print(f'Prime number: {list(filter(isPrimeNum, L))}')
    print(f'can be divided by 2 and 3: {list(filter(lambda x: True if x % 2 == 0 and x % 3 == 0 else False, L))}')