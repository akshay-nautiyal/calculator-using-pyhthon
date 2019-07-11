import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")
heading_label = tk.Label(mainWindow, text='enter the first number')
heading_label.pack()

num_field = tk.Entry(mainWindow)
num_field.pack()

def takevalueInput():
    num1 = int(num_field.get())
    print(num1)

heading_labe2 = tk.Label(mainWindow, text='enter the second number')
heading_labe2.pack()

num_field1 = tk.Entry(mainWindow)
num_field1.pack()

def takevalue2Input():
    num2 = int(num_field1.get())
    print(num2)

def functionInput(text):
    num1 = int(num_field.get())
    num2 = int(num_field1.get())

    if( text == '+'):
        result = num1 + num2
        print(result)
    elif(text == '-'):
        result = num1 - num2
        print(result)
    elif(text == '*'):
        result = num1 * num2
        print(result)
    elif( text == '/'):
        if(num2 == 0):
            result = 0
            print(result)
        else:
            result = num1/num2
            print(result)

heading_labe3 = tk.Label(mainWindow, text='opration')
heading_labe3.pack()

button = tk.Button(mainWindow, text='+', command=lambda:functionInput('+'))
button.pack()

button = tk.Button(mainWindow, text='-', command=lambda:functionInput('-'))
button.pack()

button = tk.Button(mainWindow, text='*', command=lambda:functionInput('*'))
button.pack()

button = tk.Button(mainWindow, text='/', command=lambda:functionInput('/'))
button.pack()
mainWindow.mainloop()
