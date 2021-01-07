# Process:
# Import necessary libraries
# Get spreadsheet location and name
# Store values in variables
# Make the input text of the name of the stock uppercase 
# Present a small menu which will allow to either edit, add, or view
# Create functions for each with proper logic

import openpyxl
import os

def setup():
    directory = "C:\\Users\\shrey\\Desktop"
    directory = directory.lower()
    os.chdir(directory)
    spreadname = "Stocks.xlsx"
    workbook = openpyxl.load_workbook(spreadname)
    sheet_Arr = workbook.sheetnames
    answer = ''
    sheetname = ''
    while answer != 'Y':
        for x in sheet_Arr:
            answer = input(x + ": Is this the sheetname which you are trying to access? (Y/N)  ")
            answer = answer.upper()
            if (answer == 'Y'):
                sheetname = sheet_Arr[0]
                break
    print(sheetname)
    sheet = workbook[sheetname]
    choose(sheet)

def choose(sheet):
    choice = ''
    while choice != 'V' or choice != 'E' or choice != 'A': 
        choice = input("Would you like to view (V), edit (E), or add (A) a stock?  ")
        choice = choice.upper()
        if choice == 'V':
            showStock(sheet)
            break
        elif choice == 'E':
            editStock(sheet)
            break
        elif choice == 'A':
            addStock(sheet)
            break
        else:
            print("Please enter a valid option") 
    

def showStock(sheet):
    stockName = input("What is the name of the stock which you are trying to view? Example: TSLA    Stock Name: ")
    stockRow = 0
    for i in range(1, 5):
        if sheet.cell(row=i, column = 1).value == stockName:
            stockRow = i
    print("Here is the info for " + str(stockName) + ":")
    for i in range(1, 5):
        print(f {sheet.cell(row = 1, column = i).value} + ": " + str(sheet.cell(row = stockRow, column = i).value))

def editStock(sheet):
    return None

def addStock(sheet):
    return None
    
def main():
    setup()

main()