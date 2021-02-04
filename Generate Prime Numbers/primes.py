# Generating prime number series upto the Nth Digit 
# In this program, user will be entering a number as an input and have the program generate the Fibonacci sequence to that number.
# Developer: Upesh Maharana 
# Dated: 2021/02/03

def generatePrimes(limit):
    """
    This method generates the list of Prime numbers within the range of (1,limit)
    Parameter(s):
    limit - A number given by the user as a range to find all the prime numbers. 
    """
    
    primes = []
    for i in range(1,limit+1):
        counter=0
        for j in range(1,i+1):
               if i%j==0:
                  counter += 1
        
        #checking if the number or factors are only 2 i.e '1' and the number itself.
        if counter == 2:
            primes.append(i)
        
    return primes


def Main():
    """
    Main method of the program where user is asked to give the value of N as an input.
    """
    try: 
        t = int(input("Please enter the valid number upto which Prime Number series will be generated."))
        if t > 0:
           print("Your Prime Number Series: ",generatePrimes(t))
        else:
           print("Given number is of incorrect format. Please enter a positive number next time.")
    except:
        print("Please enter a positive integer")

if __name__=="__main__":
    Main()


    
