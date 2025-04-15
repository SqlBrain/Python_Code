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
choice1 = input('Hello traveller. You\'re are at a crossroad on a dirt path, where do you want to go? '
                'Type "left","right" or "straight" to begin. ').lower()

if choice1 == "left":
    cave_choice = input('You reach a cave in the mountains. '
                        'Type "enter" to walk inside. Type "stay" to stay outside the cave. ').lower()
    if cave_choice == "enter":
        print("You have found the treasure. You Win!")
    else:
        print("You were eaten by a bear. Game Over.")
elif choice1 == "right":
    lake_choice = input('You\'ve come to a lake, there is a lake house across the lake. '
                        'Type "swim" to swim across. Type "wait" to wait for a boat. ').lower()
    if lake_choice == "wait":
        house_choice = input('You make it to the lake house safely. Type "enter" to walk inside.'
                             ' Type "wait" to wait outside. ').lower()
        if house_choice == "enter":
            house2_choice = input('You make it inside the house and spot some cans of food and a bed. '
                                  'Type "food" to eat the food. Type "bed" to go to sleep. ').lower()
            if house2_choice == "bed":
                print("You ended up falling asleep forever. Game Over.")
            else:
                print("There was no food and you starved to death. Game Over.")
        else:
            print("You burn to death in the heat of the sun. Game Over")
    else:
        print("You were attacked by a school of angry salmon. Game Over.")
else:
    print("You fell off a cliff. Game Over.")