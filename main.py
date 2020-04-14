import tkinter
import math as M

expression = ""        #definice matematickeho vyrazu

def addToExpression(addition):        #fce pridani znaku do vyrazu
    global expression
    if expression == "0":
        expression = str(addition)
    else:
        expression = str(expression) + str(addition)
    
    app.result.set(expression)        #zobrazeni vyrazu

def clear():        #fce pro mazani celeho vyrazu
    global expression
    expression = "0"
    app.result.set(expression)

def solve():        #fce pro vyresenni vyrazu
    global expression
    if "^" in expression:
        expression=str(expression).replace("^", "**")        #prepsani mocniny
    if "√" in expression:
        expression=str(expression).replace("√", "M.sqrt")        #prepsani odmocniny
    try:        #zjisteni problemu
        app.result.set(eval(expression))        #reseni
        expression = eval(expression)
    except:
        app.result.set("Error")
        expression="0"
    
def delete():        #fce mazani jednoho znaku
    global expression
    if len(str(expression)) > 1:
        expression = str(expression)[:-1]
    else:
        expression = "0"
    app.result.set(eval(expression))

class window(tkinter.Tk):        #trida aplikace
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.title("Calculator")        #zakladni nastaveni aplikace
        self.result=tkinter.StringVar()
        self.result.set("0")
        
        self.output=tkinter.Label(textvariable=self.result, borderwidth=2, relief="sunken")        #pridani tlacitek
        self.output.grid(row=0, column=0, columnspan=4, sticky="NSEW")

        self.buttonClear=tkinter.Button(text="C", width=4, height=2, command=clear, bg="lightGrey")
        self.buttonDel=tkinter.Button(text="Del", width=4, height=2, command=delete, bg="lightGrey")
        self.buttonPower=tkinter.Button(text="^", width=4, height=2, command= lambda: addToExpression("^"), bg="lightGrey")
        self.buttonSqRt=tkinter.Button(text="√", width=4, height=2, command= lambda: addToExpression("√("), bg="lightGrey")
        self.buttonOB=tkinter.Button(text="(", width=2, height=2, command= lambda: addToExpression("("), bg="lightGrey")
        self.buttonCB=tkinter.Button(text=")", width=2, height=2, command= lambda: addToExpression(")"), bg="lightGrey")
        
        self.buttonClear.grid(row=1, column=0, sticky="NSEW", rowspan=1)
        self.buttonDel.grid(row=2, column=0, sticky="NSEW", rowspan=1)
        self.buttonPower.grid(row=1, column=1, sticky="NSEW", rowspan=2)
        self.buttonSqRt.grid(row=1, column=2, sticky="NSEW", rowspan=2)
        self.buttonOB.grid(row=1, column=3, sticky="NSEW", rowspan=1)
        self.buttonCB.grid(row=2, column=3, sticky="NSEW", rowspan=1)

        self.button1=tkinter.Button(text="1", width=4, height=4, command= lambda: addToExpression("1"), bg="grey")
        self.button2=tkinter.Button(text="2", width=4, height=4, command= lambda: addToExpression("2"), bg="grey")
        self.button3=tkinter.Button(text="3", width=4, height=4, command= lambda: addToExpression("3"), bg="grey")
        self.button4=tkinter.Button(text="4", width=4, height=4, command= lambda: addToExpression("4"), bg="grey")
        self.button5=tkinter.Button(text="5", width=4, height=4, command= lambda: addToExpression("5"), bg="grey")
        self.button6=tkinter.Button(text="6", width=4, height=4, command= lambda: addToExpression("6"), bg="grey")
        self.button7=tkinter.Button(text="7", width=4, height=4, command= lambda: addToExpression("7"), bg="grey")
        self.button8=tkinter.Button(text="8", width=4, height=4, command= lambda: addToExpression("8"), bg="grey")
        self.button9=tkinter.Button(text="9", width=4, height=4, command= lambda: addToExpression("9"), bg="grey")
        self.button0=tkinter.Button(text="0", width=4, height=4, command= lambda: addToExpression("0"), bg="grey")

        self.button1.grid(row=3, column=0, sticky="NSEW")
        self.button2.grid(row=3, column=1, sticky="NSEW")
        self.button3.grid(row=3, column=2, sticky="NSEW")
        self.button4.grid(row=4, column=0, sticky="NSEW")
        self.button5.grid(row=4, column=1, sticky="NSEW")
        self.button6.grid(row=4, column=2, sticky="NSEW")
        self.button7.grid(row=5, column=0, sticky="NSEW")
        self.button8.grid(row=5, column=1, sticky="NSEW")
        self.button9.grid(row=5, column=2, sticky="NSEW")
        self.button0.grid(row=6, column=0, sticky="NSEW")

        self.buttonDivide=tkinter.Button(text="/", width=4, height=4, command= lambda: addToExpression("/"), bg="lightGrey")
        self.buttonMultiply=tkinter.Button(text="*", width=4, height=4, command= lambda: addToExpression("*"), bg="lightGrey")
        self.buttonMinus=tkinter.Button(text="-", width=4, height=4, command= lambda: addToExpression("-"), bg="lightGrey")
        self.buttonPlus=tkinter.Button(text="+", width=4, height=4, command= lambda: addToExpression("+"), bg="lightGrey")
        self.buttonPeriod=tkinter.Button(text=".", width=4, height=4, command= lambda: addToExpression("."), bg="lightGrey")
        
        self.buttonDivide.grid(row=3, column=3, sticky="NSEW")
        self.buttonMultiply.grid(row=4, column=3, sticky="NSEW")
        self.buttonMinus.grid(row=5, column=3, sticky="NSEW")
        self.buttonPlus.grid(row=6, column=3, sticky="NSEW")
        self.buttonPeriod.grid(row=6, column=1, sticky="NSEW")
        
        self.buttonEquals=tkinter.Button(text="=", width=4, height=4, command=solve, bg="lightGrey")

        self.buttonEquals.grid(row=6, column=2, sticky="NSEW")

app = window()
app.mainloop()        #start aplikace