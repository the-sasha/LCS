# Sasha Geist
# Lazy Character Sheet
# Dice with modified rolls
    # returns the roll of a number of multisided dice plus a modifying constant

from random import randint

class Dice(object):
    def __init__(self, count, sides, mod):
        """Dice don't have to be legal polyhedrons, so for ex d11 is allowed"""
        self.count = count
        self.sides = sides
        self.results = 0
        self.mod = mod

    def roll(self):
        """returns result of rolling xDy + a modifier"""
        unmod =0
        for x in range(0, self.count):
            r = randint(1, self.sides)
            unmod += r
        self.results = unmod + self.mod
        return self.results
