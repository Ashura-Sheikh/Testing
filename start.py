from tkinter import *  # Using TK
import tkinter as tk

# Creating a new window
def create_window():
    window = tk.Toplevel(root)
    window.title("New-window")
    window.geometry("500x500")
    window.configure(bg='black')
    window = tk.Button(window, text="Shall we start then?").grid(row=0)
    #label_c = tk.Label(window, text="Files kept here for Work-Purposes", fg="green", bg="black", command=add_file)
    #label.grid(row=1, column=1, padx=10, pady=5)


root = tk.Tk()
create_new = tk.Button(root, text="Open-Files",fg="green", bg="black", command=create_window)
create_new.grid(row=2, column=6)

#def add_file():
    #return None

def new_task():
    new_task = tk.StringVar(window)
    print(new_task)



root.title("Shall we go to War?",)
root.configure(bg='black')
root.geometry("400x600")

e = Entry(root, width=50, borderwidth=5) # Entry input
e.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

myLabel = Label(root, text="Ashura-Corp",fg="green", bg="black")  # labeling
myLabel.grid(row=0,column=0)

e.insert(0, END)
e.get()

class button_click():

# Define Butons
    def button_click():
        button_click == button
        return None

button_1 = Button(root, text="New-Window",fg="green", bg="black", padx=10, pady=5, command=create_window)
button_2 = Button(root, text="Project List?",fg="green", bg="black", padx=10, pady=5, command=create_new)
button_3 = Button(root, text="Black-Book?",fg="green", bg="black", padx=10, pady=5, command=button_click)
button_4 = Button(root, text="Youtube?",fg="green", bg="black", padx=10, pady=5, command=button_click)


# Putting buttons as grid

button_1.grid(row=4, column=0)
button_2.grid(row=6, column=0)

button_3.grid(row=4, column=1)
button_4.grid(row=6, column=1)





















root.mainloop() # using to loop the GUI consintently
