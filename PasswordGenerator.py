letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '€', '?', '^',]

total = [letters,numbers,symbols]

print("=== Welcome to the MyPassword Generator! ===")
nr_letters = int(input("How many LETTERS would you like in your password?\n"))
nr_symbols = int(input("How many SYMBOLS would you like?\n"))
nr_numbers = int(input("How many NUMBERS would you like?\n"))

import random

password = []

for char in range(0, nr_letters):
    password.append(letters[char])
for char in range(0, nr_numbers):
    password.append(numbers[char])
for char in range(0, nr_symbols):
    password.append(symbols[char])

random.shuffle(password)
pw = "".join(password)

print(pw)
