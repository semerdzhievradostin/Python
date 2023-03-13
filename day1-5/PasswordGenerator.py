#Password Generator Project
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Randomize Letters Numbers and Symbols from the Lists
randomLetter = ''

for i in range(nr_letters):
    randomLetter += random.choice(letters)

randomNumber = ''

for i in range(nr_numbers):
    randomNumber += random.choice(numbers)

randomSymbols = ''

for i in range(nr_symbols):
    randomSymbols += random.choice(symbols)

#Combine Letters Symbols and Numbers and then Randomize them 
password = randomSymbols + randomNumber + randomLetter
random_password = list(password)
random.shuffle(random_password)
print("".join(random_password))