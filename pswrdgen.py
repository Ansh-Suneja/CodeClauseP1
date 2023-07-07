import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid password length. Please enter a positive integer.")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    password_text.delete(1.0, tk.END)
    password_text.insert(tk.END, password)

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_text = tk.Text(root, height=1, width=30)
password_text.pack()

root.mainloop()
