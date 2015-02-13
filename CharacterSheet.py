# Sasha Geist
# Lazy Character Sheet
# Character Sheet
    # Making and using a character

import shelve
from  Dice import Dice


class CharacterSheet():
    def __init__(self, sheet):
        self.your_char = sheet

    def store_dice(self):
        """Stores rolls for future use in a dictionary file"""
        print ("\nRolls can be anything you need to store for your character:")
        print ("will save, strength, attack, greatsword, hack & slash, hard, etc.")
        print ("Rolls are stored with the quantity of dice used, the dice sides, and a modifier")
        new_att= input("\nPlease enter the name of the roll you want to store (Q to quit): ")


        while new_att != "Q" and new_att != "q":
            if new_att in self.your_char:
                print ("You've already saved %s." % new_att)
            else:
                try:
                    value = input("Please enter the roll for %s in the form of #d#+# (like 2d6+0): " % new_att)
                    value.replace(" ","")
                    value= value.lower()
                    parts = value.split('d')
                    parts_two = parts[1].split('+')
                    parts_three = parts_two[1].split(' ')
                    self.your_char[new_att] = value
                except Exception:
                    print ("Rolls are stored with the quantity of dice used, the dice sides, and a modifier")
                    print ("Please try again. Enter your roll in the form: #d#+# (or xdy+z, like 1d20+0)\n")
            new_att = input("Please enter the name of the roll you want to store (Q to quit): ")   

    def use_dice(self):
        """Allows users to select from stored rolls and get results"""
        if len(self.your_char) < 1:
            print ("\nYou don't have any stored rolls. Please add some rolls to use.")
        else:
            if len(self.your_char)== 1:
                print ("\nYour stored roll is: ")
            else:
                print ("\nYour stored rolls are: ")
            for key in self.your_char:
                print (key)
            toss_the_dice = input("\nWhat roll do you want? (Q to quit) ")

            while toss_the_dice != "Q" and toss_the_dice != "q":
                if toss_the_dice in self.your_char:
                    dice_toss = Dice(toss_the_dice, self.your_char[toss_the_dice])
                    dice_toss.roll()
                else:
                    print ("You don't have a roll for %s" % toss_the_dice)
                toss_the_dice = input("\nWhat roll do you want? (Q to quit) ")
