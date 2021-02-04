# Generating Fibonacci series upto the Nth Digit 
# In this program, user will be entering a number as an input and have the program generate the Fibonacci sequence to that number.
# Developer: Upesh Maharana 
# Dated: 2021/02/03

def generateFibSeries(n):
    """
    This method will generate fibonacci series upto the parameter passed
    Parameter(s):
    'n' -- The number given by the user upto which the series needs to be generated
    """
    # Declaring Constants as 0 and 1 are always the starting numbers in Fibonacci series
    A=0
    B=1
    FibSeq = [A,B]
    for i in range(n):
        c = FibSeq[-1] + FibSeq[-2]
        FibSeq.append(c)
    return FibSeq

def Main():
    """
    Main method of the program where user is asked to give the value of N as an input.
    """
    try: 
        t = int(input("Please enter the valid term # upto which you want to see Fibonacci series."))
        if t > 0:
           print("Your Fibonacci Series: ",generateFibSeries(t))
        else:
           print("Given number is of incorrect format. Please enter a positive number next time.")
    except:
        print("Please enter a positive integer")

if __name__ == "__main__":
   Main() 
   
