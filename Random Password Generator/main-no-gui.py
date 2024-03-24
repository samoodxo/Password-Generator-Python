import string
import random

password = ""
post_password = ""

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
numbers = string.digits
random_char = string.punctuation

random_lower = random.choices(lower_alphabet, k=4)
for letter in random_lower:
    password += letter

random_higher = random.choices(upper_alphabet, k = 4)
for letter in random_higher:
    password+= letter
    
random_numbers = random.choices(numbers, k=2)
for number in random_numbers:
    password += number
    
randomchar = random.choices(random_char, k=1)
for char in randomchar:
    password+= char

finished = random.choices(password,k=8)

for char in finished:
    post_password += char
