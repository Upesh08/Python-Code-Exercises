# Binary to Decimal & back Converter.
# In this program, user will be giving a number as an input and converts it to bindary/decimal equivalent based on the user's choice. 
# Developer: Upesh Maharana 
# Dated: 2021/02/12

import math
def convertBinDec(n,ch):
    """
    This function takes users choice and Number as input and converts the number into Binary/Decimal. 
    Parameters:
    n -- Number to be converted.
    ch -- User's choice. 
    """
    if ch==1:
        Sum = 0
        num = n[::-1]  # using slicing to reverse the string for accurate results. 
        for i in range(len(num)):
            g = int(math.pow(2,i) * int(num[i]))
            Sum += g

        return Sum
    
    if ch==2:
        digits = []
        d = int(n)
        while(True):
            if d>=1:
               q = d//2   # for finding quotient
               r = d%2    # for fining remainder
               d = q
               digits.append(r)
            else:
                break
        
        digits.reverse() # for reversing the list to get the right binary digit 
        return "".join(str(i) for i in digits)
   
    

def Main():
    """
    This method creates a menu for the user to select and input his/her choice. 
    """
    print("""
    Welcome to the Binary Decimal Converter Tool.

    Please select from our below options:
    1. Convert Binary to Decmal
    2. Convert Decimal to Binary
    
    """)

    while(True):
        choice = input("Please enter your choice")
        if choice.isdigit() == True and int(choice) in range(1,3):
            if  choice == '1':
                binary = input("Please enter the Binary Number")
                ConvNum = convertBinDec(binary,int(choice))
                print("Value after conversion is :",ConvNum)
            if  choice == '2':
                decimal = input("Please enter the Decimal Number")
                ConvNum = convertBinDec(decimal,int(choice))
                print("Value after conversion is :",ConvNum)
        else:
            print("Data entered is not in the correct format.")
         
if __name__ == "__main__":
    Main()