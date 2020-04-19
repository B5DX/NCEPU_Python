# 五  请写一个小游戏，人狗大站;  规则:
# 1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#     人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
# 2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#    人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
# 3   对战规则: 
#  A  随机决定,谁先开始攻击; 
#  B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#  C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
# 提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 
# 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
from Human import Human
from Dog import Dog
from random import randint

class Fight():
    humans = []
    dogs = []
    npcs = set(('Human', 'Dog'))
    cur = set()

    def __init__(self):
        self.humans = [Human(str(i)) for i in range(2)]
        self.dogs = [Dog(str(i)) for i in range(3)]
        self.cur.add('Human' if randint(0,1) else 'Dog')

    def next(self):
        if len(self.humans) == 0:
            print('Dogs succeed')
            return False
        elif len(self.dogs) == 0:
            print('Humans succeed')
            return False
        
        humanInd = randint(0, len(self.humans)-1)
        dogInd = randint(0, len(self.dogs)-1)
        if 'Human' in self.cur:
            res = self.humans[humanInd].attack(self.dogs[dogInd])
            # print('human', self.humans[humanInd].name, 'attacked dog', self.dogs[dogInd].name)
            if res <= 0: # died
                self.print()
                del self.dogs[dogInd]
                
        else :
            res = self.dogs[dogInd].attack(self.humans[humanInd])
            # print('dog', self.humans[humanInd].name, 'attacked human', self.dogs[dogInd].name)
            if res <= 0:
                self.print()
                del self.humans[humanInd]
        self.cur = self.npcs - self.cur
        return True

    def print(self):
        for h in self.humans:
            print('human', h.name, h.blood, h.force)
        for d in self.dogs:
            print('dogs', d.name, d.blood, d.force)

if __name__ == "__main__":
    f = Fight()
    while f.next():
        pass
    print('Exit successfully.')