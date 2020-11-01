########Fibbing
from tkinter import * #Importing tkinter

def main():
    def generate():
        fib = [0, 1] #Stating the first numbers of the sequence.
        try:
            x = [] #Initialising an empty list.
            y = int(num.get()) #Gets the input from the user.
            
            #This loop generates the numbers in the sequence.
            for i in range(1, y+1): 
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x.append(first) #All the numbers generated are added into the empty list.
            Label(win, text = str(x)).grid(row = 5, column = 0) #The sequence with the specified lenght is outputted to the user.
            
        #If the user does not enter a value or if they enter a string, nothing will happen and no error will be shown.
        except ValueError:
            pass
        
    def total():
        fib = [0, 1] #Stating the first numbers of the sequence.
        try:
            x = 0 #Initalising x as 0 to later output the sum of the whole sequence.
            y = int(num.get()) #Gets the input from the user.
            
            #This loop generates the numbers in the sequence.
            for i in range(1, y+1): 
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x += first #All the values are being added to x.
            Label(win, text = x).grid(row = 6, column = 0) #The sum of the sequence is ooutputted.
            
        #If the user does not enter a value or if they enter a string, nothing will happen and no error will be shown.
        except ValueError:
            pass
        
    def reverse():
        fib = [0, 1] #Stating the first numbers of the sequence.
        try:
            x = []#Initialising an empty list
            y = int(num.get())
            for i in range(1, y+1):
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x.append(first) #All the numbers generated are added into the empty list.
            Label(win, text = str(x[::-1])).grid(row = 7, column = 0) # "x[::-1]" will output the sequence in reverse.
            
        #If the user does not enter a value or if they enter a string, nothing will happen and no error will be shown.    
        except ValueError:
            pass
        
    win = Tk() #Creating the surface
    win.geometry("306x250") #This specifies the size of the surface
    win.title("Fibbing") #Title of the window


    Label(win, text = "How many places do you want to generate?", font = 12).grid(pady = 10) 
    num = Entry(win, width = 30) # "Entry(surface, width)" allows the user to enter a value
    num.grid() # Place the widget on the surface

    #Buttons giving the user options
    #Button(surface, text = "message", command = function, width).grid(row, column, padx, pady)
    #NOTE: when you place a function in "command", you don't need have to your brackrackets.
    Button(win, text = "Generate", command = generate, width = 12).grid(pady = 10) #This will output the sequence
    Button(win, text = "Sum", command = total, width = 12).grid() #This will output the sum of the sequence.
    Button(win, text = "Reverse", command = reverse, width = 12).grid(pady = 10) #This will output the sequence in reverse.

    win.mainloop()

main() #Initialises the program
