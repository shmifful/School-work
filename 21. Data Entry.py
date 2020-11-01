######DATA ENTRY TABLE
from tkinter import *

def main():
    def inputData_and_destroy():
        menuWin.destroy()
        inputData()
        
    def inputData():
        def submit():
            f = open("Data entry file.txt", "a+")
            nValue = name.get()
            sValue= surname.get()
            eValue = email.get()
            pValue = password.get()
            cValue = city.get()
                
            data = "|"+nValue+"|"+sValue+"|"+eValue+"|"+pValue+"|"+cValue+"|"
            f.write(data)
            f.write("\n")
            f.close()
            inpWin.destroy()
            main()
                
        inpWin = Tk()
        inpWin.geometry("350x250")
        inpWin.title("INPUT YOU DATA")
        Label(inpWin, text="Name:").grid(column = 0, row = 0, pady = 15)
        name = Entry(inpWin, width = 35)
        name.grid(column = 1, row = 0, padx = 3)
        
        Label(inpWin, text="Surname:").grid(column = 0, row = 1)
        surname = Entry(inpWin, width = 35)
        surname.grid(column = 1, row = 1, padx = 3)
        
        Label(inpWin, text="Email:").grid(column = 0, row = 2, pady = 15)
        email = Entry(inpWin, width = 35)
        email.grid(column = 1, row = 2, padx = 3)
        
        Label(inpWin, text="Password:").grid(column = 0, row = 3)
        password = Entry(inpWin, width = 35, show = "*")
        password.grid(column = 1, row = 3, padx = 3)
        
        Label(inpWin, text="City:").grid(column = 0, row = 4, pady = 15)
        city = Entry(inpWin, width = 35)
        city.grid(column = 1, row = 4, padx = 3)

        Button(inpWin, text = "SUBMIT", command = submit).grid(column = 1, row = 5, padx = 30)
        
        inpWin.mainloop()

#################################################################################################################################################

    def getData_and_destroy():
        menuWin.destroy()
        getData()
        
    def getData():
        def detailWin(data):
            def mainAndDestroy():
                dWin.destroy()
                main()
                
            with open("Data entry file.txt", "r") as f:
                for line in f.readlines():
                    if data in line:
                        break
                details = line.split("|")
                name = details[1]
                surname = details[2]
                city = details[5]

                dWin = Tk()
                dWin.geometry("300x200")
                dWin.title("Your Details")

                Label(dWin, text = "Name: "+name).pack(pady=20)
                Label(dWin, text = "Surname: "+surname).pack()
                Label(dWin, text = "City: "+city).pack(pady=20)

                Button(dWin, text = "Return to menu", command = mainAndDestroy).pack()
                

                dWin.mainloop()
                
        def verify():
            f = open("Data entry file.txt", "r")
            eValue = email.get()
            pValue = password.get()
            data = "|"+eValue+"|"+pValue+"|"
            file = f.read()

            if data in file:
                getWin.destroy()
                detailWin(data)
            else:
                Label(getWin, text = "Your data was not found", fg = "red").grid(column = 1, row = 3)
            f.close()
            
        getWin = Tk()
        getWin.geometry("300x150")
        getWin.title("WHAT'S YOUR DATA")

        Label(getWin, text="Email:").grid(column = 0, row = 0, pady = 15)
        email = Entry(getWin, width = 35)
        email.grid(column = 1, row = 0, padx = 3)
        
        Label(getWin, text="Password:").grid(column = 0, row = 1)
        password = Entry(getWin, width = 35, show = "*")
        password.grid(column = 1, row = 1, padx = 3)

        Button(getWin, text = "SUBMIT", command = verify).grid(column = 1, row = 2, pady = 17)

        getWin.mainloop()

#################################################################################################################################################
    
    menuWin = Tk()
    menuWin.geometry("300x300")
    menuWin.title("Menu")
    Button(menuWin, text = "Input data", width = 25, command= inputData_and_destroy).pack(pady = 50)
    Button(menuWin, text = "Get data", width = 25, command= getData_and_destroy).pack()
    Button(menuWin, text = "EXIT", width = 25, command= quit).pack(pady = 50)


    menuWin.mainloop()

    
main()
