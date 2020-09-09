from tkinter import *  # Using TK
import tkinter as tk

# Creating a new window
def create_window():
    window = tk.Toplevel(root)

root = tk.Tk()
create_new = tk.Button(root, text="Create new window", command=create_window)
create_new.grid(row=2, column=6)

def new_task():
    new_task = tk.StringVar(window)
    print(new_task)





root.title("How can I help you Today?",)
root.configure(bg='black')
root.geometry("400x600")



e = Entry(root, width=55, borderwidth=5) # Entry input
e.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

myLabel = Label(root, text="Hello Sheikho")  # labeling
myLabel.grid(row=0,column=0)

e.insert(0, "Enter today's search?")
e.get()




class button_click():

# Define Butons
    def button_click():
        button_click == button
        return None



button_1 = Button(root, text="Pending work?", padx=10, pady=10, command=create_window)
button_2 = Button(root, text="Project List?", padx=10, pady=10, command=create_new)
button_3 = Button(root, text="Planning?", padx=10, pady=10, command=button_click)
button_4 = Button(root, text="Want to chill?", padx=10, pady=10, command=button_click)


# Putting buttons as grid

button_1.grid(row=4, column=0)
button_2.grid(row=6, column=0)

button_3.grid(row=4, column=1)
button_4.grid(row=6, column=1)





















root.mainloop() # usingto loop the GUI consintently
