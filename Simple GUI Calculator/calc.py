# GUI Arithmetic Calculator.
# In this program, the user will be able to do basic arithmetic operations
# Developer: Upesh Maharana 
# Dated: 2021/04/26


from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.iconbitmap("Calc_icon.ico")

box = Entry(root,width=35,borderwidth=5)
box.grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 10)

def func(n):
    #box.delete(0,END)
    expr = box.get()
    box.delete(0,END)
    box.insert(0,expr+str(n))
    
def clear_func():
    box.delete(0,END)

def oprFunc(type):
    """ This method will first store the value present in the Entry widget in a global variable and 
    then it will clear the Entry widget"""
    global operation
    operation = type.lower()
    first_num = box.get()
    global operand
    operand = int(first_num)
    box.delete(0,END)

def equal_func():
    """ This method is responsible for showing the output of the arithmetic operation"""
    second_num = box.get()
    box.delete(0,END)
    if operation == "subtraction":
       result = operand - int(second_num) 
    elif operation == "addition":
       result = operand + int(second_num) 
    if operation == "multiplication":
       result = operand * int(second_num) 
    if operation == "division":
       if int(second_num) != 0:
          result = operand / int(second_num) 
       else:
          result = "Cannot be divided by zero"
    box.insert(0,result)


# defining Buttons
btn_1 = Button(root,text = '1',padx = 30,pady= 10,command=lambda:func(1))
btn_2 = Button(root,text = '2',padx = 30,pady= 10,command=lambda:func(2))
btn_3 = Button(root,text = '3',padx = 30,pady= 10,command=lambda:func(3))

btn_4 = Button(root,text = '4',padx = 30,pady= 10,command=lambda:func(4))
btn_5 = Button(root,text = '5',padx = 30,pady= 10,command=lambda:func(5))
btn_6 = Button(root,text = '6',padx = 30,pady= 10,command=lambda:func(6))

btn_7 = Button(root,text = '7',padx = 30,pady= 10,command=lambda:func(7))
btn_8 = Button(root,text = '8',padx = 30,pady= 10,command=lambda:func(8))
btn_9 = Button(root,text = '9',padx = 30,pady= 10,command=lambda:func(9))

btn_0 = Button(root,text = '0',padx = 30,pady= 10,command=lambda:func(0))
btn_clear = Button(root,text = 'Clear',padx = 60,pady= 10,command=clear_func)
btn_sub = Button(root,text = '-',padx = 30,pady= 10,command=lambda:oprFunc("Subtraction"))
btn_div = Button(root,text = '/',padx = 30,pady= 10,command=lambda:oprFunc("Division"))
btn_mul = Button(root,text = '*',padx = 30,pady= 10,command=lambda:oprFunc("Multiplication"))
btn_add = Button(root,text = '+',padx = 30,pady= 10,command=lambda:oprFunc("Addition"))
btn_equals = Button(root,text = '=',padx = 70,pady= 10,command=equal_func)

# Positioning Buttons
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1) 
btn_3.grid(row=3,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_0.grid(row=4,column=0)
btn_clear.grid(row=4,column=1,columnspan=2)

btn_sub.grid(row=5,column=0)
btn_div.grid(row=5,column=1)
btn_mul.grid(row=5,column=2)

btn_add.grid(row=6,column=0)
btn_equals.grid(row=6,column=1,columnspan=2)

root.mainloop()


