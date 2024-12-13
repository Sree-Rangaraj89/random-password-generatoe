import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length=8):
    characters = '0123456789'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password():
    password = generate_password()
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

app = tk.Tk()
app.title("Random Password Generator")

label_length = tk.Label(app, text="Fixed Password Length: 8 Characters (Only Numbers)")
label_length.pack(pady=10)

button_generate = tk.Button(app, text="Generate Password", command=display_password)
button_generate.pack(pady=10)

entry_password = tk.Entry(app, width=30)
entry_password.pack(pady=5)

app.mainloop()
