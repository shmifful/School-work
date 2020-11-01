########CALCULATOR
from tkinter import *

def main():
    menu = Tk()
    menu.geometry("250x265") #window size
    menu.title("MENU") #window title

    #asking the user what they want to calculate
    Label(menu, text = "Choose what you want to do", font = 12). pack(pady =5)
    Button(menu, text = "VAT", command = vat, width = 20).pack(pady=20)
    Button(menu, text = "Tax", command = tax, width = 20). pack()
    Button(menu, text = "Times table", command = tt, width = 20). pack(pady=20)
    Button(menu, text = "Exit", command = quit, width = 20). pack()

    menu.mainloop()

def vat():
    def calculate():
        try:
            VAT = float(1.2) #VAT rate = 20%
            p = float(price.get()) #retrieving price inputted by the user as a floating number
            newPrice = p * VAT #calcutes the price of the product/service + vat
            newPrice = "%.2f" % newPrice # rounds to 2dp
            # outputs price plus vat to the user
            Label(vatWin, text = "£"+str(newPrice), width = 30). grid(column = 1, row = 3, pady = 5)
        
        #if a string is inputted, a messege will be outputted and no error will be shown
        except ValueError:
            Label(vatWin, text = "Wrong value entered", fg = "red"). grid(column = 1, row = 3, pady = 5)
    
    vatWin = Tk()
    vatWin.geometry("325x150") # window size
    vatWin.title("VAT Calculator") # window title

    #asking what price they want to be calculated
    Label(vatWin, text = "How much does your product/service cost?", font = 12, fg = "green").grid(column = 1)
    Label(vatWin, text ="£", font = 15).grid(column =0, row = 1, pady = 20)
    price = Entry(vatWin, width = 50)
    price.grid(column = 1, row = 1)

    Button(vatWin, text = "CALCULATE", command = calculate).grid(column = 1, row = 2)

    vatWin.mainloop()

def tax():
    def calculate():
        try:
            s = int(salary.get()) #retrieves datainputted by the user
            #checking how much the user pays in tax
            if s < 0:
                Label(taxWin, text ="Be real fam", width = 30).grid(column =1, row = 3)
            elif s >= 0 and s <= 12500:
                Label(taxWin, text ="You don't need to pay tax", width = 30).grid(column =1, row = 3)
            elif s >= 12501 and s <= 50000:
                Label(taxWin, text ="Your tax rate is 20%", width = 30).grid(column =1, row = 3)
            elif s >= 50001 and s <= 150000:
                Label(taxWin, text ="Your tax rate is 40%", width = 30).grid(column =1, row = 3)
            else:
                Label(taxWin, text ="Your tax rate is 45%", width = 30).grid(column =1, row = 3)
                
        #if the user enters a string, nothing will happen, no error will be outputted
        except ValueError:
            pass
        
    taxWin = Tk()
    taxWin.geometry("325x150") #size of the window
    taxWin.title("TAX Calculator") #title of the window

    #asks the user for their salary to check how much tax they a to pay
    Label(taxWin, text = "What is your salary?", font = 12, fg = "green").grid(column = 1)
    Label(taxWin, text ="£", font = 15).grid(column =0, row = 1, pady = 20)
    salary = Entry(taxWin, width = 50)
    salary.grid(column = 1, row = 1)

    Button(taxWin, text = "CALCULATE", command = calculate).grid(column = 1, row = 2)

    taxWin.mainloop()

def tt():
        
    ttWin = Tk()
    ttWin.geometry("310x310") #size of the window
    ttWin.title("Times table") #name of the window

    #making a times table up to 10
    for i in range(1,11):
        for j in range(1,11):
            Label(ttWin, text = str(i * j), font = 20).grid(column = i, row = j, padx = 3, pady = 3)


    ttWin.mainloop()

main() #initialising
