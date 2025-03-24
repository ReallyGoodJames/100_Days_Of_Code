letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("Welcome to the PyPassword Generator!")


#--------------------------------------------------------------
#RANDOM STRING SELECTORS
#--------------------------------------------------------------
#Random Letter Selector
letters_length = len(letters) - 1
random_letter = letters[(random.randint(0, letters_length))]

#Random Number Selector
numbers_length = len(numbers) - 1
random_number = numbers[(random.randint(0, numbers_length))]

#Random Symbol Selector
symbols_length = len(symbols) - 1
random_symbol = symbols[(random.randint(0, symbols_length))]


#--------------------------------------------------------------
#HOW MANY LETTERS INTAKE
#--------------------------------------------------------------
how_many_letters = int(input("How many letters would you like in your password?\n"))
steps_letters = 0
random_letters_list = []

if steps_letters < how_many_letters:
    for steps in range(0, how_many_letters):
        random_letters_list.append(letters[(random.randint(0, letters_length))])

#--------------------------------------------------------------
#HOW MANY SYMBOLS INTAKE
#--------------------------------------------------------------
how_many_symbols = int(input(f"How many symbols would you like?\n"))
steps_symbols = 0
random_symbols_list = []

if steps_symbols < how_many_symbols:
    for steps in range(0, how_many_symbols):
        random_symbols_list.append(symbols[(random.randint(0, symbols_length))])

#--------------------------------------------------------------
#HOW MANY NUMBERS INTAKE
#--------------------------------------------------------------
how_many_numbers = int(input(f"How many numbers would you like?\n"))
steps_numbers = 0
random_numbers_list = []

if steps_numbers < how_many_numbers:
    for steps in range(0, how_many_numbers):
        random_numbers_list.append(numbers[(random.randint(0, numbers_length))])

#--------------------------------------------------------------
#PASSWORD PRINTER
#--------------------------------------------------------------

almost_final_password = random_letters_list + random_symbols_list + random_numbers_list
final_password_holder = []
final_password_holder.extend(almost_final_password)
final_password = random.sample(final_password_holder, len(final_password_holder))

print("Your Password is:\n")
print(*final_password, sep='')
