# Finding e value to the Nth power and upto Nth Decimal Places. 
# In this program, user will be giving a number as an input to find the value of e POWER n. 
# Developer: Upesh Maharana 
# Dated: 2021/01/23

import sys,decimal,math

def calculate_E(n):
    """
    This function calculates the value of e raised to the power of x and returns the value of e upto x decimal places. 
    Parameter(s):
      'x' - The number(Power value) given as the input by the User. 
    """
    
    VALUE_OF_E = 2.718281828 
    EpowerX = pow(VALUE_OF_E,n)
    return round(EpowerX,n)

def Main():
    """
    This is the Main method which takes value of x as an input from the User 

    """
    while True:
        evalue = input("Please enter the value of X to calculate E. Type \"exit\" to terminate the program.")
        result = None 
        if evalue == "exit":
           sys.exit()
        elif evalue.isdigit() == False:
           print("Entered value is not a digit.Please try again")
        else:
           result = calculate_E(int(evalue))
           print("E power",evalue,"upto",evalue,"th decimal point is:",result)
           break

if __name__=='__main__':
    Main()
