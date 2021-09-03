import hashlib
from tkinter import *

# Creating a root
root = Tk()
# setting Title for root window
root.title("Password Encryption")
# Entering size of Window
root.geometry("500x500")
# Setting color of the window
root.config(bg="#000000")
# Creating heading label
Heading = Label(root, bg="#000000", fg="#FFFFFF", text="Text Encryption", font=("Times New Roman", 14, "bold"), pady=5)
Heading.place(relwidth=1)
# Creating a line under the heading
line = Label(root, width=580, bg="#FE6726")
line.place(relwidth=1, rely=0.07, relheight=0.012)
# Creating label1: "Enter Text: "
Text = Label(root, text="Enter Text: ", font=("Times New Roman", 12), fg="#FFFFFF", bg="#000000")
Text.place(relheight=0.2, relx=0.1, rely=0.2)
# Creating textField1 to enter the text
textField = Entry(root, font=("Times New Roman", 10), fg="#14213D")
textField.place(relwidth=0.6, relheight=0.05, relx=0.31, rely=0.27)
textField.focus()
# Creating label2: "Encrypted text: "
encryptedText = Label(root, text="Encrypted Text: ", font=("Times New Roman", 12), fg="#FFFFFF", bg="#000000")
encryptedText.place(relheight=0.2, relx=0.1, rely=0.4)
# Creating textField2 for receiving the encrypted text
textField2 = Entry(root, font=("Times New Roman", 10), fg="#14213D")
textField2.place(relwidth=0.6, relheight=0.05, relx=0.31, rely=0.47)


# creating a function to encrypt the text
def encrypt():
    val = textField.get()
    output = hashlib.md5(val.encode()).hexdigest()
    textField2.insert(0, output)


# Creating submit button to submitting the text
submit = Button(root, text="Submit", font=("Times New Roman", 14), bg="#FFFFFF", fg="#14213D",
                activeforeground="#14213D", activebackground="#FFFFFF", command=encrypt)
submit.place(relx=0.3, rely=0.65)


# creating a clear function
def cleartf():
    textField.delete(0, END)
    textField2.delete(0, END)


# Creating clear button to clear both text fields
clear = Button(root, text="Clear", font=("Times New Roman", 14), bg="#FFFFFF", fg="#14213D", activeforeground="#14213D",
               activebackground="#FFFFFF", command=cleartf)
clear.place(relx=0.6, rely=0.65)
# mainloop
root.mainloop()

