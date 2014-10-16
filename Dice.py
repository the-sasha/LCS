# Sasha Geist
# Lazy Character Sheet
# Dice with modified rolls

from random import randint

class Dice(object):
    def __init__(self, count, sides, mod):
        self.count = count
        self.sides = sides
        self.results = 0
        self.mod = mod

    def roll(self):
        """returns result of rolling xDy"""
        unmod =0
        for x in range(0, self.count):
            r = randint(1, self.sides)
            unmod += r
        self.results = unmod + self.mod
        return self.results
