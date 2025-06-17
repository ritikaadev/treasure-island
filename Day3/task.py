print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
Way1 = input('You\'re at a cross road.Which way do you want to go Left or right? Type"left" to go left or "right" to go right.').lower()
if Way1=="left":
    Way2=input('You have come to a lake.There is an island across the lake.Type "swim" to swim across or "wait" to wait for the boat.').lower()
    if Way2== "wait":
        Way3= input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?").lower()
        if Way3 =="yellow":
            print("You win!You found the treasure!")
        elif Way3 =="red":
            print("Game over.You enter a room full of fire.")
        elif Way3 =="blue":
            print("Game over.You enter a room full of beasts.")
        else:
            print("Game over.You choose a door that dosen\'t exist.")
    else:
        print("Game over.You were attacked by an angry trout.")

else:
    print("Game over.You fell into a hole.")
