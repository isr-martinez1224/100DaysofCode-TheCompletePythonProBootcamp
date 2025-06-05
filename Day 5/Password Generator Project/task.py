letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random


#Easy Solution
# final_password = ""
#
# letters_length = len(letters) - 1
# symbols_length = len(symbols) - 1
# numbers_length = len(numbers) - 1
#
# for x in range(0, nr_letters):
#     final_password += letters[random.randint(0,letters_length)] #could use random.choice(letters)  instead
#
# for y in range(0, nr_symbols):
#     final_password += symbols[random.randint(0, symbols_length)]
#
# for z in range(0, nr_numbers):
#     final_password += numbers[random.randint(0, numbers_length)]
# print(final_password)

#Hard Solution
final_password = ""
password_list = []

for x in range(0, nr_letters):
    password_list.append(random.choice(letters))

for y in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for z in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

#Before Shuffle
print(password_list)
for change in range(0, 3):
    random.shuffle(password_list)

#After Shuffle
print(password_list)
for char in password_list:
    final_password += char
print("Your password is: " + final_password)
