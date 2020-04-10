class Dog():
    # count = 0
    __count = 0

    def __init__(self, color, name, voice):
        self.color = color
        self.name = name
        Dog.__count += 1
    
    def bark(self):
        print(self.name + 'is barking')

    @classmethod
    def getCnt(cls):
        return cls.__count
    
    @staticmethod
    def test():
        # need no param
        print('This is a static method')

if __name__ == "__main__":
    d1 = Dog('white', 'bobo', 1)
    d2 = Dog('black', 'nono', 2)
    d3 = Dog('grey', 'yoyo', 3)
    d1.bark()
    print(d3.getCnt())