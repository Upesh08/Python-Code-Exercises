# Money Change Back Calculator.
# This calculator takes the amount and price as an input from the user and returns the balance amount in terms of quarters,dimes,nikels and pennies.  
# Developer: Upesh Maharana 
# Dated: 2021/02/10

def calculateChange(amt,price):
    """
    This function calculates the change in terms of quarters, dimes, nickels, and pennies which is required to be given back to the user.
    """
    change = amt-price
    denominations = {'quarter':25,'dime':10,'nickel':5,'pennie':1}
    msg = ""
    for key,value in denominations.items():
        num = int(change/value)
        key = "penny" if key == "pennie" and num<=1 else key
        plural = "s" if num > 1 else ""
        msg += " " +str(int(num)) + " " + key + plural
        change = change%value
    return msg

def Main():
    """
    This method takes amount and price as an input from the user and returns the balance amount in denominations by calling a method internally. 
    """
    try:
        prodPrice = int(input("Please enter the price of the product."))
        amount = int(input("Please enter the amount to be payed."))
        if amount >= 0 and prodPrice >= 0:
            if amount >= prodPrice:
               print("Your Balance amount is :",amount - prodPrice,"$ which is",calculateChange(amount,prodPrice))
            else:
               print("Insufficient amount entered.")
        else: 
            print("Invalid Amount entered. Please enter positive amount.")
    except:
        print("Invalid Input format.")
   
 
if __name__ == "__main__":
    Main()
