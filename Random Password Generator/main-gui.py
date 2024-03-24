import string
import random
import customtkinter as ctk



App = ctk.CTk()
App.geometry("500x500")
App.maxsize(500,500)
App.title("Samees Password Generator")

Pass_Gen_Label = ctk.CTkLabel(App,text="Password Generator",font=("inter",18,"bold"))
Pass_Gen_Label.pack(pady=20)


def generate_password():
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

    Blank_var.set(post_password)


Pass_Gen_Button = ctk.CTkButton(App,text="Generate Random Password",font=("inter",14,"bold"),command=generate_password)
Pass_Gen_Button.pack()

Blank_var = ctk.StringVar()
Blank_var.set("Password Will Appear Here")

Blank_Label = ctk.CTkLabel(App, textvariable=Blank_var)

Blank_Label.pack(pady=20)


App.mainloop()