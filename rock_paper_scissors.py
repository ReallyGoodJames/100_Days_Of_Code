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
game_images = [rock, paper, scissors]

#input
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

#outcome graphic 1
if choice >= 0 and choice <= 3:
    print(game_images[choice])
else:
    print("Improper Selection")

#computer chose
print("Computer chose: ")

#outcome graphic 2
computer_choice = random.randint(0,2)
print(game_images[computer_choice])

#Who Won
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and choice == 2:
    print("You Lose!")
elif computer_choice > choice:
    print("You Lose!")
elif computer_choice < choice:
    print("You Win!")
elif computer_choice == choice:
    print("Tie! Play again!")


