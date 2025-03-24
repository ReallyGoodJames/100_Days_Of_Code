password = ""
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_symbols):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f"Your Password is: {password}")
