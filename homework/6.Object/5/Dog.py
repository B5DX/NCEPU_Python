from Base import Base
from random import randint

class Dog(Base):
    def __init__(self, name):
        super().__init__('Dog', name, 20, 80)

    def injured(self, value):
        res = super().injured(value)
        self.force -= randint(1, 3)
        if self.force <= 0:
            self.force = 1
        return res