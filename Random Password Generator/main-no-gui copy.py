import string
import random


lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
numbers = string.digits
random_char = string.punctuation


password = ""
characters = [lower_alphabet + upper_alphabet + numbers + random_char]
Char_amt = int(input("How many characters do you want to generate?: "))

for lists in characters:
    generated_pass = random.choices(lists,k=Char_amt)
    for char in generated_pass:
        password += char
        
print(f"Your Password is {password}")
        