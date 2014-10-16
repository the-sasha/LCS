# Sasha Geist
# Lazy Character Sheet

    # A command line dice-roller with named and stored rolls, grouped by character
    # Dice, Attributes, and CharacterSheet are all distinct files for multiuse

from CharacterSheet import CharacterSheet
import shelve
import os.path


def create_sheet(name):
    """Creates a new file in LCS folder for a new character"""
    file_name = name.lower()
    file_name = file_name + '.txt'
    full_file = file_name +'.db'
    testing = os.path.isfile(full_file)
    if testing == False:
        your_char = shelve.open(file_name, 'n')
    else:
        while testing == True:
            print ("%s already exists." % name)
            task2 = input("Do you want to open %s [o], create a new character [c], or quit[q] " % name)
            task2 = task2.upper()
            if task2 == "O":
                your_char = shelve.open(file_name, 'c')
                testing = False
            elif task2 == "C":
                name = input("What is your character's name? ")
                file_name = name.lower()
                file_name = file_name + '.txt'
                full_file = file_name +'.db'
                testing = os.path.isfile(full_file)
                if testing == False:
                    your_char = shelve.open(file_name, 'n')
            elif task2 == "Q":
                exit()
            else:
                while task2 != "O" and task2 != "C" and task2 != "Q":
                    task2 = input("Please enter 'o' to open %s, 'c' to create a new character, or 'q' to quit. " % name)
                    if task2 == "O":
                        your_char = shelve.open(file_name, 'c')
                        testing == False
                    elif task2 == "C":
                        name = input("What is your character's name? ")
                        file_name = name.lower()
                        file_name = file_name + '.txt'
                        full_file = file_name +'.db'
                        testing = os.path.isfile(full_file)
                        if testing == False:
                            your_char = shelve.open(file_name, 'n')
                    elif task2 == "Q":
                        exit()
    return your_char

def open_sheet(name):
    """Opens an existing file in LCS folder for an existing character"""
    file_name = name.lower()
    file_name = file_name + '.txt'
    full_file = file_name + '.db'
    testing = os.path.isfile(full_file)
    if testing == True:
        your_char = shelve.open(file_name, 'c')
    else:    
        while testing == False:
            print ("There is no file for %s." % name)
            task2 = input("Do you want to create %s[c], open an existing character[0], or quit[q]? " % name)
            task2 = task2.upper()
            
            if task2 == "O":
                name = input("What character do you want to use? ")
                file_name = name.lower()
                file_name = file_name + '.txt'
                full_file = file_name + '.db'
                testing = os.path.isfile(full_file)
                if testing == True:
                    your_char = shelve.open(file_name, 'c')
                    
            elif task2 == "C":
                your_char = shelve.open(file_name, 'n')
                testing = True
                
            elif task2 == "Q":
                exit()
                
            else:
                while task2 != "O" and task2 != "C" and task2 != "Q":
                    task2 = input("Please enter 'c' to create %s or 'o' to open a character. " % name)
                    if task2 == "O":
                        name = input("What character do you want to use? ")
                        file_name = name.lower()
                        file_name = file_name + '.txt'
                        full_file = file_name + '.db'
                        testing = os.path.isfile(full_file)
                        if testing == True:
                            your_char = shelve.open(file_name, 'c')
                    elif task2 == "C":
                        your_char = shelve.open(file_name, 'n')
                        testing == True
                    elif task2 == "Q":
                        exit()
    return your_char
        



 



# IT ALL STARTS RIGHT HERE


print ('Welcome to the Lazy Character Sheet generator.\n')
task = input('Do you want to create a new character [c] or open an exiting one? [o] ')

task = task.upper()

if task == 'C':
    name = input("What is your character's name? ")
    your_char = create_sheet(name)
            
elif task == 'O':
    name = input("What character do you want to use? ")
    your_char = open_sheet(name)

else:
    while task != 'C' and task != 'O':
        task = input('Please type "c" to create or "o" to open: ')
        task = task.upper()
        if task == 'C':
            name = input("What is your character's name? ")
            your_char = create_sheet(name)
            
        elif task == 'O':
            ame = input("What character do you want to use? ")
            your_char = open_sheet(name)


            
sheet = CharacterSheet(your_char)
             
next_task = input("\nDo you want to add rolls [a], use rolls [u], or quit[q]? ")
next_task = next_task.upper()
while next_task != 'Q':
    if next_task == 'A':
        sheet.store_attributes()

    elif next_task == 'U':
        sheet.use_attributes()

    else:
        while next_task != 'A' and next_task != 'U':
            next_task = input('Please type "a" to add or "u" to use: ')
            next_task = next_task.upper()

            if next_task == 'A':
                sheet.store_attributes()

            elif next_task == 'U':
                sheet.use_attributes()
    next_task = input("\nDo you want to add rolls [a], use rolls [u], or quit[q]? ")
    next_task = next_task.upper()



your_char.close()


