import tkinter

expression = ""

def addToExpression(addition):
    global expression
    expression = expression + addition


class window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Calculator")
        self.output=tkinter.Label(text="test")  
        self.output.grid(row=0, column=0, columnspan=4)
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

        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        self.button0.grid(row=4, column=1)

        self.buttonDivide=tkinter.Button(text="/", width=4, height=4)
        self.buttonMultiply=tkinter.Button(text=".", width=4, height=4)
        self.buttonMinus=tkinter.Button(text="-", width=4, height=4)
        self.buttonPlus=tkinter.Button(text="+", width=4, height=4)
        
        self.buttonDivide.grid(row=1, column=3)
        self.buttonMultiply.grid(row=2, column=3)
        self.buttonMinus.grid(row=3, column=3)
        self.buttonPlus.grid(row=4, column=3)
        
        self.buttonEquals=tkinter.Button(text="=", width=4, height=4)

        self.buttonEquals.grid(row=4, column=2)

app = window()
app.mainloop()
print(expression)