print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Which direction do you choose, left or right?\n ")
if direction == "right" and not direction == "left":
    print("You fell into a hole...Game Over!")
else:
    import time 
    print("Walking...")
    time.sleep(5) #Number of seconds
    lakechoice = input("You got to a lake...\n Now What?\n Swim or wait? \n")
    if lakechoice == "swim":
        print("You have been attacked by unkown predator...\n Game Over!")
    else:
        print("Waiting...")
        time.sleep(5)
        print("You fell asleep...The sound of a boat coming woke you up.")
        time.sleep(5)
        print("The people from the boat drove you to the other side of the lake near a house...")
        doors = input("There are 3 doors and a window. Which one do you choose, Red, Blue, Yellow or the Window?\n ")
        if doors == "Red" or doors == "red":
            print("You have been burned by a explosion...\n Game Over!")
        elif doors == "Blue" or doors == "blue":
            print("You have been eaten by a Wizli... \n Game Over!")
        elif doors == "Yellow" or doors == "yellow":
            print ("!!!Congratulations you saved Jolka and Yasen, you WIN !!!")
        else:
            print("You have been killed by Freddy Mercury in Pajamas...\n Game Over!")
        
    