# Modern Calculator.
# This program is a form of a calculator which helps in calculating the result by taking numbers as input from the User. 
# Developer: Upesh Maharana 
# Dated: 2021/02/15

import math

def calculate(a,b,op):
    """
    This method helps in calculating the result.
    Parameters:
    a - Operand 1
    b - Operand 2
    op - Operator
    """
    a = int(a)
    b = int(b)
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '*':
        return a*b
    if op == '/':
        return a/b

def Main():
    """
    This is the Main method which takes the operands as an input from the User and shows the result.
    """
    choice = True
    while(choice):
            print("""
            Welcome to our Calculator.
            Operations that can be performed by the calculator are as follows:
            a) Addition
            b) Subtraction
            c) Multiplication
            d) Division
            e) Exit
         
            """)
        
            option = True
            result = None
            while option:
                ch = input("Enter the operation you want to perform:").lower()
                
                if ch == 'a':
                    op1 = input("Enter your first operand:")
                    op2 = input("Enter your second operand:")
                    result = calculate(op1,op2,'+')   
                    option = False 
                elif ch == 'b':
                    op1 = input("Enter your first operand:")
                    op2 = input("Enter your second operand:")
                    result = calculate(op1,op2,'-') 
                    option = False   
                elif ch == 'c':
                    op1 = input("Enter your first operand:")
                    op2 = input("Enter your second operand:")
                    result = calculate(op1,op2,'*')
                    option = False    
                elif ch == 'd':
                    op1 = input("Enter your first operand:")
                    op2 = input("Enter your second operand:")
                    result = calculate(op1,op2,'/')
                    option = False 
                elif ch == 'e':
                    break 
                else:
                   print("Invalid option entered") 
            if result != None:
               print("Result:{}".format(result))
            
            choice = input("Would you like to perform more operations? (y/n)")  
            if choice.lower() == 'y':
                choice = True
            elif choice.lower() == 'n':
                choice = False
            else:
                print("Invalid data entered.Please re-enter your preference")
                choice = True            

if __name__ == "__main__":
    Main()