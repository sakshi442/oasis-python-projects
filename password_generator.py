import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# ---------------- PASSWORD GENERATION ---------------- #

def generate_password():
    try:
        length = int(length_var.get())
    except:
        messagebox.showerror("Error", "Enter valid length")
        return

    if length <= 0:
        messagebox.showerror("Error", "Length must be greater than 0")
        return

    character_set = ''
    if uppercase_var.get():
        character_set += string.ascii_uppercase
    if lowercase_var.get():
        character_set += string.ascii_lowercase
    if digits_var.get():
        character_set += string.digits
    if symbols_var.get():
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

    check_strength(password)


# ---------------- PASSWORD STRENGTH ---------------- #

def check_strength(password):
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif strength == 3 or strength == 4:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="lime")


# ---------------- COPY PASSWORD ---------------- #

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied successfully!")
    else:
        messagebox.showwarning("Warning", "No password to copy")


# ---------------- SHOW / HIDE PASSWORD ---------------- #

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# ---------------- UI DESIGN ---------------- #

root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("500x550")
root.configure(bg="#0f0f0f")

# Title
title = tk.Label(root, text="⚡ PASSWORD GENERATOR ⚡",
                 font=("Courier", 18, "bold"),
                 fg="lime",
                 bg="#0f0f0f")
title.pack(pady=20)

frame = tk.Frame(root, bg="#0f0f0f")
frame.pack()

# Length
tk.Label(frame, text="Password Length:",
         fg="white", bg="#0f0f0f",
         font=("Courier", 12)).grid(row=0, column=0, sticky="w", pady=5)

length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var,
                        font=("Courier", 12),
                        bg="black", fg="lime",
                        insertbackground="lime")
length_entry.grid(row=0, column=1, pady=5)

# Checkboxes
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

options = [
    ("Uppercase Letters", uppercase_var),
    ("Lowercase Letters", lowercase_var),
    ("Numbers", digits_var),
    ("Special Symbols", symbols_var)
]

for i, (text, var) in enumerate(options):
    tk.Checkbutton(frame,
                   text=text,
                   variable=var,
                   bg="#0f0f0f",
                   fg="lime",
                   selectcolor="black",
                   activebackground="#0f0f0f",
                   font=("Courier", 11)).grid(row=i+1, column=0, columnspan=2, sticky="w")

# Generate Button
generate_btn = tk.Button(root,
                         text="GENERATE",
                         command=generate_password,
                         bg="lime",
                         fg="black",
                         font=("Courier", 14, "bold"),
                         width=20)
generate_btn.pack(pady=20)

# Password Entry
password_entry = tk.Entry(root,
                          font=("Courier", 16),
                          justify="center",
                          bg="black",
                          fg="lime",
                          insertbackground="lime",
                          show="*")
password_entry.pack(pady=10, ipadx=10, ipady=5)

# Show password
show_var = tk.BooleanVar()
tk.Checkbutton(root,
               text="Show Password",
               variable=show_var,
               command=toggle_password,
               bg="#0f0f0f",
               fg="white",
               font=("Courier", 10)).pack()

# Strength Label
strength_label = tk.Label(root,
                          text="Strength: ",
                          font=("Courier", 12, "bold"),
                          bg="#0f0f0f",
                          fg="white")
strength_label.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root,
                     text="COPY TO CLIPBOARD",
                     command=copy_password,
                     bg="#1f1f1f",
                     fg="lime",
                     font=("Courier", 12, "bold"),
                     width=25)
copy_btn.pack(pady=10)

root.mainloop()