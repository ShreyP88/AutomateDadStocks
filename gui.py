import tkinter as tk
from tkinter import Frame, StringVar, Toplevel
import logic 
import time

def raise_frame(frame):
    frame.tkraise()
window = tk.Tk()
window.configure(background='black')


addFrame = Frame(window)
editFrame = Frame(window)


window.geometry("800x500")
initialMessage = tk.Label(window, text = "Welcome, please select an option below.", width = 500, height = 5, fg = 'white', bg = 'black', font = ("Courier", 15))
initialMessage.pack()



def viewClicked():
    viewFrame = Toplevel()
    viewFrame.geometry("800x500")
    viewFrame.configure(background="black")
    #raise_frame(viewFrame)
    viewLab = tk.Label(viewFrame, text = "View Stock", width = 500, height = 5, fg = 'white', bg = 'black', font = ("Courier", 15))
    viewLab.pack()
    entry = tk.Entry(viewFrame, fg="black", bg="yellow", width=50)
    entry.place(x = 0, y = 100)
    entry.insert(0,"Stock Symbol:")
    submit=tk.Button(viewFrame, height=1, width=5, text="Submit", command=lambda: performProcessing(entry))
    submit.place(x = 320, y = 100)
    
    
def performProcessing(entry):
    toShow = logic.showStock(str(entry.get()[13:].strip()))
    print(toShow)
    

def addClicked():
    print("Add Clicked!")

def editClicked():
    print("Edit Clicked!")


viewButton = tk.Button(window,
    text = "View Stocks",
    width = 30,
    height = 3,
    fg = 'black',
    bg = 'yellow',
    command = lambda: viewClicked()
)
viewButton.place(x = 0, y = 250)

addButton = tk.Button(window,
    text = "Add Stocks",
    width = 30,
    height = 3,
    fg = 'black',
    bg = 'yellow',
    command = lambda: addClicked()
)
addButton.place(x = 585, y = 250)

editButton = tk.Button(window,
    text = "Edit Stocks",
    width = 30,
    height = 3,
    fg = 'black',
    bg = 'yellow',
    command = lambda: editClicked()
)
editButton.place(x = 295, y = 250)
    

window.mainloop()