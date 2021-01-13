import tkinter as tk
from tkinter import Frame, StringVar, Toplevel
import logic
import openpyxl
import os

from openpyxl import workbook
from openpyxl import load_workbook

def raise_frame(frame):
    frame.tkraise()
window = tk.Tk()
window.configure(background='black')


addFrame = Frame(window)
editFrame = Frame(window)


window.geometry("800x500")
initialMessage = tk.Label(window, text = "Welcome, please select an option below.", width = 500, height = 5, fg = 'white', bg = 'black', font = ("Courier", 15))
initialMessage.pack()


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

def viewClicked():
    viewFrame = Toplevel()
    viewFrame.geometry("800x500")
    viewFrame.configure(background="black")
    viewLab = tk.Label(viewFrame, text = "View Stock", width = 500, height = 5, fg = 'yellow', bg = 'black', font = ("Courier", 15))
    viewLab.pack()
    entry = tk.Entry(viewFrame, fg="white", bg = 'gray', width=50)
    entry.place(x = 0, y = 120)
    entry.insert(0,"Stock Symbol: ")
    submit=tk.Button(viewFrame, height=1, width=5, text="Submit", command=lambda: performProcessing(entry, viewFrame))
    submit.place(x = 320, y = 118)
    
    
def performProcessing(entry, viewFrame):
    toShow = logic.showStock(str(entry.get()[14:].strip()).upper())
    showLabel = tk.Label(viewFrame, text = toShow, fg = 'black')
    showLabel.place(x = 0, y = 150)
    entry.delete(14, 'end')


def addClicked():
    print("Add Clicked!")

def editClicked():
    editFrame = Toplevel()
    editFrame.geometry("1200x800")
    editFrame.configure(background="black")
    viewLab = tk.Label(editFrame, text = "Edit Stock", width = 500, height = 5, fg = 'yellow', bg = 'black', font = ("Courier", 17))
    viewLab.pack()
    currentStocks = logic.showCurrentStocks()
    currentStockLab = tk.Label(editFrame, text = currentStocks, fg = 'black')
    currentStockLab.place(x = 0, y = 100)
    entry = tk.Entry(editFrame, fg="white", bg = 'gray', width=50)
    entry.place(x = 250, y = 100)
    entry.insert(0,"Stock Symbol to Edit: ")
    submit=tk.Button(editFrame, height=1, width=5, text="Submit", command=lambda: processEdit(entry, editFrame))
    submit.place(x = 575, y = 95)

def processEdit(entry, editFrame):
    symbol = str(entry.get()[22:].strip().upper())
    toShow = logic.showStock(str(entry.get()[22:].strip().upper()))
    showLabel = tk.Label(editFrame, text = toShow, fg = 'black')
    showLabel.place(x = 0, y = 100)
    entry.delete(22, 'end')
    editEntry = tk.Entry(editFrame, fg = 'white', bg = 'gray', width = 50)
    editEntry.place(x = 250, y = 125)
    editEntry.insert(0, "Line Number to Edit: ")
    submit1=tk.Button(editFrame, height=1, width=5, text="Submit", command = lambda: performProcessingEdit(editFrame, editEntry, symbol))
    submit1.place(x = 575, y = 125)
    #get the line number and the stock symbol is in toShow
    #call logic function 

def performProcessingEdit(editFrame, entry, symbol):
    lineNum = str(entry.get()[20:].strip())
    entry.delete(21, 'end')
    changeEntry = tk.Entry(editFrame, fg = 'white', bg = 'gray', width = 50)
    changeEntry.place(x = 250, y = 160)
    changeEntry.insert(0, "New Line " + str(lineNum) + ": ")
    accept = tk.Button(editFrame, height = 1, width = 12, text = "Accept Changes", command = lambda: returnEdit(lineNum, symbol, changeEntry, editFrame))
    accept.place(x = 575, y = 160)

def returnEdit(lineNum, symbol, changeEntry, editFrame):
    lineNum = int(lineNum)
    if lineNum == 7 or lineNum == 2 or lineNum == 1 or lineNum == 3:
        change = str(changeEntry.get()[11:].strip())
    else:
        change = float(changeEntry.get()[11:].strip())
    logic.editStock(lineNum, symbol, change)
    edited = logic.showStock(symbol)
    changeEntry.delete(12, 'end')
    editedStockLabel = tk.Label(editFrame, text = edited, fg = 'black')
    editedStockLabel.place(x = 0, y = 100)

window.mainloop()