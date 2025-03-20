rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#-----------
#Ascii Art Above
#-----------

import random

#input
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

#outcome graphic 1
if choice == 0:
    player = rock
    print(rock + "\n")

elif choice == 1:
    player = paper
    print(paper + "\n")

elif choice == 2:
    player = scissors
    print(scissors + "\n")

else:
    print("Improper Selection")


#computer chose
print("Computer chose: \n")

#outcome graphic 2

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(rock + "\n")

elif computer_choice == 1:
    print(paper + "\n")

elif computer_choice == 2:
    print(scissors + "\n")

#Who Won

if choice == 0:
    if computer_choice == 0:
        print("You Tie!")
    elif computer_choice == 1:
        print("You Lose!")
    else:
        print("You Win!")

if choice == 1:
    if computer_choice == 0:
        print("You Win!")
    elif computer_choice == 1:
        print("You Tie!")
    else:
        print("You Lose!")

if choice == 2:
    if computer_choice == 0:
        print("You Lose!")
    elif computer_choice == 1:
        print("You Win!")
    else:
        print("You Tie!")
