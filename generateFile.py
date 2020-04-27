import os

def generateFiles(sum: int) -> None:
    for i in range(1, sum+1):
        with open(str(i) + '.py', 'w') as f:
            pass

if __name__ == "__main__":
    assert 'homework' in __file__
    os.chdir(os.path.dirname(__file__))
    generateFiles(4)
    print('Finish')