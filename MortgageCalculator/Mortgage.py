# Mortgage Monthly Payment Calculator
# In this program, we will be calculating Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. 
# Developer: Upesh Maharana 
# Dated: 2021/02/07

import math 
import decimal
def calculatePayment(p,r,t):
    """
    This method calculates the mortgage payment to be paid monthly by the user. 
    """
    nume = p*r/100/12
    deno = 1-math.pow((1+r/100/12),-t)
    payment = nume/deno
    return payment

def calculateYears(p,r,amt):
    """
    This method calculates the tenure in years require to clear the loan. 
    """
    nume = 1-(p*r/(100*amt*12))
    deno = pow(1 + (r/(100*12)),-12)
    no_of_years = math.log(nume)/math.log(deno)
    return no_of_years

def Main():
    """
    This method takes inputs from the user and calls methods to calculate the result.
    """
    choice = True
    while(choice): 
        print ("""
        
        ***********Welcome to the Mortgage Calculator **************

        Using this calculator, you can 
        
        1) Calculate the monthly Mortgage Payment to be made. 
        2) Calculate the time duration in months to clear the loan 
        
        """)
        ch = int(input("Enter the option you want to select:"))
        if ch == 1:
           choiceOption1 = True
           while(choiceOption1 == True): 
                loan = input("Enter loan value: ")
                term = input("Enter Mortgage term (in months): ")
                rate = input("Enter interest rate:")
                if loan.isnumeric() == True and term.isnumeric() == True and rate.isnumeric() == True:
                   payAmount = calculatePayment(float(loan),float(rate),int(term))
                   print("Monthly payment :", round(payAmount))
                   choiceOption1 = False
                else:
                   print("Data entered is not in the correct format. Please re-enter.")
        elif ch == 2:
            choiceOption2 = True
            while(choiceOption2 == True): 
                loan = input("Enter loan value: ")
                pay_per_month = input("Enter the payment you can afford to make monthly:")
                rate = input("Enter interest rate:")
                if loan.isnumeric() == True and pay_per_month.replace('.','',1).isdigit() == True and rate.replace('.','',1).isdigit():
                   years = calculateYears(float(loan),float(rate),float(pay_per_month))
                   print("Total Years required :", years)
                   choiceOption2 = False

                else:
                   print("Data entered is not in the correct format. Please re-enter.")
        
        mainChoice = input("Would you like to continue (y/n).? ")
        if mainChoice.lower() == 'y':
           pass
        else:
           choice = False
        
            
if __name__=="__main__":
    Main()
