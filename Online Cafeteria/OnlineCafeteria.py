# OnlineCafeteria.py
# This is a small online cafeteria program in which the user selects the product to eat/drink,pays the price and then this program will notify how much money the user will be getting back in terms of quarters,dimes,nickels and pennies.
# Developer: Upesh Maharana 
# Dated: 2021/02/09

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
    This function interacts with the user by displaying the lists of products to buy and takes user's choice and amount. After user pays , this method will return the change amount in terms of quarters,dimes,nickles and pennies.
    """
    
    print("""
    
    Welcome to our Cafeteria. Todays Menu !.

    1) Cotton Candy : 30 $
    2) Lays (Onion and Cream magic) : 40 $
    3) Bournville chocolate bar : 60 $ 
    4) Lemonade : 50 $ 
    5) Spl. Pizza : 150 $
    6) Spl. Coffee : 10 $
    7) Spl. Burger Meal : 145 $  
    """)
    option = input("Please, enter your choice (1-7):")
    prices = {'1':30,'2':40,'3':60,'4':50,'5':150,'6':10,'7':145}
    if  option.isdigit() == True and int(option) in range(1,8):
        prodPrice = prices.get(option)
        print("Excellent choice sir. That will be  ",prodPrice,"$")
        payChoice = True
        total = 0
        while(payChoice):
            try:
                amount  = input("Please pay by entering the amount.")
                total += int(amount)
                if amount.isdigit()==True and total >= prodPrice:
                   print("Your Balance amount is :",total - prodPrice,"$ which is",calculateChange(int(total),prodPrice))
                   payChoice = False
                elif amount.isdigit()==True and total < prodPrice:
                    print("Insufficient amount Sir. Please pay ",prodPrice-total," more.")
                else: 
                    print("Amount entered is not in the correct format.")
            except:
                print("Invalid Input format.")
    else:   
        print("Wrong input given. Please re-enter a valid option.")
 
if __name__ == "__main__":
    Main()
