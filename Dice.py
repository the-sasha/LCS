# Sasha Geist
# Lazy Character Sheet
# Dice with modified rolls
    # builds dice, generates and displays results


from random import randint

class Dice(object):
    def __init__(self, name, xdy):
        """Takes in name/type, dice needs, modifier"""
        self.name = name
        self.xdy = xdy
        self.values =[1,1,0]
        self.results = 0
        self.mod = 0

    def build_dice(self):
        """makes dice to use in attribute"""
        parts = self.xdy.split('d')
        parts_two = parts[1].split('+')
        count = int(parts[0]) 
        sides = int(parts_two[0]) 
        mod = int(parts_two[1])
        self.values = [count, sides, mod]
        return self.values
        
        
    def roll(self):
        """returns result of rolling xDy + a modifier"""
        rolldie = self.build_dice()
        count = rolldie[0]
        sides = rolldie[1]
        mod = rolldie[2]
        unmod =0
        for x in range(0, count):
            r = randint(1, sides)
            unmod += r
        self.results = unmod + mod
        print ("\n%s roll: %d" % (self.name, self.results))
        return self.results


    
# TODO: results that prompt another result (like attack then damage),
# TODO: trackable attributes, like damage, xp



#next lines for testing only
#test = Dice("testing", "2d6+3")
#print (test.build_dice())
#test.roll()

