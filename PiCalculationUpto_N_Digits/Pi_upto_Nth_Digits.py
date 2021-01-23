# Finding PI value upto the Nth Digit 
# In this program, user will be giving a number as an input to find the value of Pi(π) upto the given number of decimal places using the famous Chudnovsky Algorithm. 
# Developer: Upesh Maharana 
# Dated: 2021/01/20

import math 
import decimal

def factorial(x):
    """ 
    Calculates the factorial of a given number
    Parameter(s): 
        'n'- The number given to find the factorial of.  
    """
    
    if x == 0:
        return 1
    else:
       return x * factorial(x-1)

def calc_pi_chudnovsky(q):
    """
    It calculates the RHS part of the famous Chudnovsky Algorithm i.e 'q' iterations in order to find the decimal places. To get 'q' decimal places, total iterations should be equal to "q+1".
   
    Parameter(s): 
        'q'- The number of decimal places which nees to be fetched.  
    """
    
    q = q + 1  #To get actual decimal places
    decimal.getcontext().prec = q    # To set precision only upto 'q' number of decimal point.  
    summation = 0
    C = 426880 * math.sqrt(10005)
    for i in range(q):
        numerator = factorial(6*i)*(545140134*i + 13591409)   
        denominator = (factorial(3*i)) * ((factorial(i))**3) *(640320**(i*3))
        summation += numerator/denominator
    piValue =  decimal.Decimal(C)/ decimal.Decimal(summation)
    return piValue

def Main():
    #Taking input from the user
    print("Enter the value of Nth digit Pi needs to be calculated..")
    num =input()
    if num.isdigit()==False:
        print("Entered value is not a digit. Please provide the value in correct format")
    else:
        result = calc_pi_chudnovsky(int(num))
        print("Value of Pi upto ",num,"th digit is:",result)

if __name__=='__main__':
	Main()
 
