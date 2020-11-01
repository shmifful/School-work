########CALCULATOR
from tkinter import *

def main():
    menu = Tk()
    menu.geometry("250x265")
    menu.title("MENU")

    Label(menu, text = "Choose what you want to do", font = 12). pack(pady =5)
    Button(menu, text = "VAT", command = vat, width = 20).pack(pady=20)
    Button(menu, text = "Tax", command = tax, width = 20). pack()
    Button(menu, text = "Times table", command = tt, width = 20). pack(pady=20)
    Button(menu, text = "Exit", command = quit, width = 20). pack()

    menu.mainloop()

def vat():
    def calculate():
        try:
            VAT = float(1.2)
            p = float(price.get())
            newPrice = p * VAT
            newPrice = "%.2f" % newPrice
            Label(vatWin, text = "£"+str(newPrice), width = 30). grid(column = 1, row = 3, pady = 5)
        except ValueError:
            Label(vatWin, text = "Wrong value entered", fg = "red"). grid(column = 1, row = 3, pady = 5)
    
    vatWin = Tk()
    vatWin.geometry("325x150")
    vatWin.title("VAT Calculator")

    Label(vatWin, text = "How much does your product/service cost?", font = 12, fg = "green").grid(column = 1)
    Label(vatWin, text ="£", font = 15).grid(column =0, row = 1, pady = 20)
    price = Entry(vatWin, width = 50)
    price.grid(column = 1, row = 1)

    Button(vatWin, text = "CALCULATE", command = calculate).grid(column = 1, row = 2)

    vatWin.mainloop()

def tax():
    def calculate():
        try:
            s = int(salary.get())
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
                
        except ValueError:
            pass
        
    taxWin = Tk()
    taxWin.geometry("325x150")
    taxWin.title("TAX Calculator")

    Label(taxWin, text = "What is your salary?", font = 12, fg = "green").grid(column = 1)
    Label(taxWin, text ="£", font = 15).grid(column =0, row = 1, pady = 20)
    salary = Entry(taxWin, width = 50)
    salary.grid(column = 1, row = 1)

    Button(taxWin, text = "CALCULATE", command = calculate).grid(column = 1, row = 2)

    taxWin.mainloop()

def tt():
        
    ttWin = Tk()
    ttWin.geometry("310x310")
    ttWin.title("Times table")

    for i in range(1,11):
        for j in range(1,11):
            Label(ttWin, text = str(i * j), font = 20).grid(column = i, row = j, padx = 3, pady = 3)


    ttWin.mainloop()

main()
