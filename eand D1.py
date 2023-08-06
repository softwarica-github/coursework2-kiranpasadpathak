from tkinter import *
from tkinter import messagebox
import base64
import os
import sqlite3
import unittest

# Persistence storage using SQLite database
def save_data(encrypted_message):
    conn = sqlite3.connect('encrypted_data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT)")
    cursor.execute("INSERT INTO messages (message) VALUES (?)", (encrypted_message,))
    conn.commit()
    conn.close()

# Unit testing and code coverage
def test_encryption():
    message = "This is a test message"
    encoded_message = encrypt_message(message)
    assert encoded_message == "VGhpcyBpcyBhIHRlc3QgbWVzc2FnZQ=="

def test_decryption():
    encoded_message = "VGhpcyBpcyBhIHRlc3QgbWVzc2FnZQ=="
    decoded_message = decrypt_message(encoded_message)
    assert decoded_message == "This is a test message"

# Encryption using base64
def encrypt_message(message):
    encode_message = message.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    return base64_bytes.decode("ascii")

# Decryption using base64
def decrypt_message(encoded_message):
    decode_message = encoded_message.encode("ascii")
    base64_bytes = base64.b64decode(decode_message)
    return base64_bytes.decode("ascii")

def encrypt():
    password = code.get()

    if password == "kiran":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encrypted_message = encrypt_message(message)

        Label(screen1, text="ENCRYPT", font="arial", fg="Red", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="Red", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)

        # Save encrypted message to database
        save_data(encrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "kiran":
        messagebox.showerror("encryption", "Invalid Password")

def decrypt():
    password = code.get()

    if password == "kiran":
        screen2 = Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decrypted_message = decrypt_message(message)

        Label(screen2, text="DECRYPT", font="arial", fg="Red", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="Red", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "kiran":
        messagebox.showerror("encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Welcome to Kiran page")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter the text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="Red", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Label(text="Enter secrete key", fg="black", font=("calibre", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="Reset", height="2", width="50", bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

   
    screen.mainloop()

# Run unit tests
test_encryption()
test_decryption()

# Start the main screen
main_screen()
