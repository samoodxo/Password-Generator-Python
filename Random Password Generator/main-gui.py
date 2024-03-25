import string
import random
import customtkinter as ctk



App = ctk.CTk()
App.geometry("500x500")
App.maxsize(500,500)
App.title("Samees Password Generator")

Pass_Gen_Label = ctk.CTkLabel(App,text="Password Generator",font=("inter",18,"bold"))
Pass_Gen_Label.pack(pady=20)
Blank_var = ctk.StringVar()

def generate_password():
    password = ""
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    numbers = string.digits
    random_char = string.punctuation
    
    characters = [lower_alphabet + upper_alphabet + numbers + random_char]
    if Pass_Gen_TextBox:
        get = Pass_Gen_TextBox.get("1.0","end-1c")
        for lists in characters:
            generated_pass = random.choices(lists,k=int(get))
            for char in generated_pass:
                password += char

    Blank_var.set(password)

Pass_Gen_Label_Inp = ctk.CTkLabel(App,text="How Many Characters would you like to generate?",font=("inter",18,"bold"))
Pass_Gen_Label_Inp.pack(pady=20)

Pass_Gen_TextBox = ctk.CTkTextbox(App,width=200,height=40)
Pass_Gen_TextBox.pack(pady=20)

Pass_Gen_Button = ctk.CTkButton(App,text="Generate Random Password",font=("inter",14,"bold"),command=generate_password)
Pass_Gen_Button.pack()

Blank_var.set("Password Will Appear Here")

Blank_Label = ctk.CTkLabel(App, textvariable=Blank_var)

Blank_Label.pack(pady=20)


App.mainloop()