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

first = input("You see a fork in the road, do you walk left or right: \n")

if first == "right" or first == "Right":
    print("There was a cliff, and you fell down! Game Over!")
else:
    second = input("You turn left as it starts to rain, a small river has appeared across the road. Do you swim or wait: \n")
    if second == "swim":
        print("You attempt to swim, but get swept out to sea! Game Over!")
    else:

        third = input("You finally arrive at an old Treasure Keep with 3 doors. Which door do you enter, Red, Blue, or Yellow: \n")
        if third == "red":
            print("There was fire on the other side, you are toasted! Game Over!")
        elif third == "blue":
            print("There was another river behind it and you're swept out to Sea! Game Over!")
        elif third == "yellow":
            print("Yellow is the color of GOLD !!! You Win!")
        else:
            print("You chose a door that doesn't exist!")



