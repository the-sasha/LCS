# Sasha Geist
# Lazy Character Sheet
# Attributes
    # Dice in action

from Dice import Dice

class Attribute(object):
    def __init__(self, name, xdy):
        """Takes in name/type, dice needs, modifier"""
        self.name = name
        self.xdy = xdy
        self.att_dice = Dice(1,20,0)

    def build_dice(self):
        """makes dice to use in attribute"""
        parts = self.xdy.split('d')
        parts_two = parts[1].split('+')
        c = int(parts[0]) 
        s = int(parts_two[0]) 
        m = int(parts_two[1]) 
        self.att_dice = Dice(c, s, m)
        return self.att_dice

    def display_result(self):
        """Prints out result of rolling that attribute"""
        dices = self.build_dice()
        roll_result = dices.roll()
        print ("\n%s roll: %d" % (self.name, roll_result))
        return roll_result
    
