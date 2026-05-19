#Password Generator..................

import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", "Z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
    "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", 
    ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "`", "~"
]

print("===== Welcome to Password Generator =====")

n_letters = int(input("How many letters you want in password? "))
n_symbols = int(input("How many symbols you want in password? "))
n_numbers = int(input("How many numbers you want in password? "))

"""
for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

# Convert list to string
password = "".join(password_list)

print(f"\nGenerated Password: {password}")
"""

password_list=[ ]
for i in range(1,n_letters+1):
    char= random.choice(letters)
    password_list += char
for i in range(1,n_symbols+1):
    char= random.choice(symbols)
    password_list += char
for i in range(1,n_numbers+1):
    char= random.choice(numbers)
    password_list += char
#will get order wise input ->nleeteers,symbols,numbers
print(password_list)
# Shuffle to make the password random in order
random.shuffle(password_list)
print(password_list)

# Convert list to string
password=" "
for char in password_list:
    password += char
print(password)