import tkinter

expression = ""

def addToExpression(addition):
    global expression
    if expression == "0":
        expression = addition
    else:
        expression = expression + addition
    
    app.result.set(expression)

def clear():
    global expression
    expression = "0"
    app.result.set(expression)

def solve():
    global expression
    app.result.set(eval(expression))
    expression = "0"

class window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.title("Calculator")
        self.result=tkinter.StringVar()
        self.result.set("0")
        self.output=tkinter.Label(textvariable=self.result, borderwidth=2, relief="sunken")
        self.output.grid(row=0, column=0, columnspan=4, sticky="NSEW")

        self.buttonClear=tkinter.Button(text="C", width=4, height=2, command=clear)
        self.buttonClear.grid(row=1, column=0, sticky="NSEW")

        self.button1=tkinter.Button(text="1", width=4, height=4, command= lambda: addToExpression("1"))
        self.button2=tkinter.Button(text="2", width=4, height=4, command= lambda: addToExpression("2"))
        self.button3=tkinter.Button(text="3", width=4, height=4, command= lambda: addToExpression("3"))
        self.button4=tkinter.Button(text="4", width=4, height=4, command= lambda: addToExpression("4"))
        self.button5=tkinter.Button(text="5", width=4, height=4, command= lambda: addToExpression("5"))
        self.button6=tkinter.Button(text="6", width=4, height=4, command= lambda: addToExpression("6"))
        self.button7=tkinter.Button(text="7", width=4, height=4, command= lambda: addToExpression("7"))
        self.button8=tkinter.Button(text="8", width=4, height=4, command= lambda: addToExpression("8"))
        self.button9=tkinter.Button(text="9", width=4, height=4, command= lambda: addToExpression("9"))
        self.button0=tkinter.Button(text="0", width=4, height=4, command= lambda: addToExpression("0"))

        self.button1.grid(row=2, column=0, sticky="NSEW")
        self.button2.grid(row=2, column=1, sticky="NSEW")
        self.button3.grid(row=2, column=2, sticky="NSEW")
        self.button4.grid(row=3, column=0, sticky="NSEW")
        self.button5.grid(row=3, column=1, sticky="NSEW")
        self.button6.grid(row=3, column=2, sticky="NSEW")
        self.button7.grid(row=4, column=0, sticky="NSEW")
        self.button8.grid(row=4, column=1, sticky="NSEW")
        self.button9.grid(row=4, column=2, sticky="NSEW")
        self.button0.grid(row=5, column=0, sticky="NSEW")

        self.buttonDivide=tkinter.Button(text="/", width=4, height=4, command= lambda: addToExpression("/"))
        self.buttonMultiply=tkinter.Button(text="*", width=4, height=4, command= lambda: addToExpression("*"))
        self.buttonMinus=tkinter.Button(text="-", width=4, height=4, command= lambda: addToExpression("-"))
        self.buttonPlus=tkinter.Button(text="+", width=4, height=4, command= lambda: addToExpression("+"))
        self.buttonPeriod=tkinter.Button(text=".", width=4, height=4, command= lambda: addToExpression("."))
        
        self.buttonDivide.grid(row=2, column=3, sticky="NSEW")
        self.buttonMultiply.grid(row=3, column=3, sticky="NSEW")
        self.buttonMinus.grid(row=4, column=3, sticky="NSEW")
        self.buttonPlus.grid(row=5, column=3, sticky="NSEW")
        self.buttonPeriod.grid(row=5, column=1, sticky="NSEW")
        
        self.buttonEquals=tkinter.Button(text="=", width=4, height=4, command=solve)

        self.buttonEquals.grid(row=5, column=2, sticky="NSEW")

app = window()
app.mainloop()