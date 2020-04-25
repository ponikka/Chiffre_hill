from Decryption import decryption
from Encryption import encryption
from tkinter import *
from tkinter import messagebox

letter = ord('A')
alphabet = {chr(key): value for value, key in enumerate(range(letter, letter + 26))}

def encrypt(word, key, _alphabet = alphabet):
    text = encryption(word, key, _alphabet)
    lavl = Label(text=f'Зашифрованное слово:\n{text.upper()}')
    lavl.place(height=25, width=150, x=230, y=140)

def decrypt(word, key, _alphabet=alphabet):
    text = decryption(word,key, _alphabet)
    lavl = Label(text=f'Расшифрованное слово:\n{text.upper()}')
    lavl.place(height=25, width=150, x=230, y=140)

root = Tk()
root.geometry('600x300')
root.title("Шифр Хилла")

word = StringVar()
key = StringVar()

word_label = Label(text="Введите слово:")
key_label = Label(text="Введите ключ:")

word_label.place(height=20, width=100, x=100, y=20)
key_label.place(height=20, width=100, x=100, y=50)

word_entry = Entry(textvariable=word)
key_entry = Entry(textvariable=key)

word_entry.place(height=25, width=220, x=250, y=20)
key_entry.place(height=25, width=220, x=250, y=50)

message_button = Button(text="Зашифровать", command=lambda: encrypt(word.get().upper(), key.get().upper()))
message_button.place(height=25, width=100, x=200, y=100)

message_button = Button(text="Расшифровать", command=lambda: decrypt(word.get().upper(), key.get().upper()))
message_button.place(height=25, width=100, x=300, y=100)

root.mainloop()



