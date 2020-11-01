########Fibbing
from tkinter import *

def main():
    def generate():
        fib = [0, 1]
        try:
            x = []
            y = int(num.get())
            for i in range(1, y+1):
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x.append(first)
            Label(win, text = str(x)).grid(row = 5, column = 0)
            
        except ValueError:
            pass
        
    def total():
        fib = [0, 1]
        try:
            x = 0
            y = int(num.get())
            for i in range(1, y+1):
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x += first
            Label(win, text = x).grid(row = 6, column = 0)
            
        except ValueError:
            pass
        
    def reverse():
        fib = [0, 1]
        try:
            x = []
            y = int(num.get())
            for i in range(1, y+1):
                first = fib[0]
                second = fib[1]
                fib[0] = second
                fib[1] = first + second
                x.append(first)
            Label(win, text = str(x[::-1])).grid(row = 7, column = 0)
            
        except ValueError:
            pass
        
    win = Tk()
    win.geometry("319x250")
    win.title("Fibbing")


    Label(win, text = "How many places do you want be generated?", font = 12).grid(pady = 10)
    num = Entry(win, width = 30)
    num.grid()

    Button(win, text = "Generate", command = generate, width = 12).grid(pady = 10)
    Button(win, text = "Sum", command = total, width = 12).grid()
    Button(win, text = "Reverse", command = reverse, width = 12).grid(pady = 10)

    win.mainloop()

main()
