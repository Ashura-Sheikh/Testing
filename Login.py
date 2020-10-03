from tkinter import *
from tkinter import Label


window = Tk()
window.title("Welcome to Ashura")
window.geometry("500x500")
window.configure(background="black")

def delete():
    window1.destroy()

def delete1():
    window2.destroy()

def error():
    global window1
    window1 = Toplevel(window)
    window1.geometry("200x200")
    window1.title("Warning Error")
    window1.configure(background="black")
    Label(window1,text="All Fields Mandatory *", fg="red", bg="black").pack()
    Button(window1, text="OK", command=delete, fg="Green", bg="Black").pack()

def success():
    global window2
    window2 = Toplevel(window)
    window2.geometry("300x300")
    window2.title("Logged Succesfully..")
    window2.configure(background="black")
    Label(window2, text= "Welcome to Ashura", fg="Green", bg="Black").pack()
    Button(window2, text="OK", command=delete1,fg="Green", bg="Black").pack()

def register():
    user_text = user_name.get()
    password_text = password.get()

    if user_text == "":
        error()
    elif password_text == "":
        error()
    else:
        success()



heading = Label(text="Login Required For Ashura Access..", fg="Green", bg="black").pack()


Label(text="User Name * ", fg="Green", bg="Black").place(x= 15, y= 70)
Label(text="Password *", fg="Green", bg="Black").place(x= 15, y= 140)

user_name = StringVar()
password = StringVar()


Entry(window, textvariable=user_name).place(x=15, y=90)
Entry(window, textvariable=password).place(x=15, y=160)

Button(window, text="Submit", width="7",fg="Green", bg="Black", command= register).place(x=15, y=190)

window.mainloop()
