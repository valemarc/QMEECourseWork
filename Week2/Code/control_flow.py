#!/usr/bin/env python3

"""Some functions exemplifying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.

#__appname__ = 'Boilerplate python script'
__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'
__version__ = '0.0.1'
#__license__ = "License for this code/program"

## imports ##
import sys # module to interface our program with the operating system

## constants ##


## functions ##
def even_or_odd(x=0): #if not specified, x should take value 0 (default value). If we wrote the function with just x (no defined value), then we would need to provide a value for x when running the function as there is no default value.
    """Find whether a number x is even or odd."""
    if x % 2 == 0: #The conditional if # here % is the modulo
        return "%d is Even!" % x #similar to x + "is even"
    return "%d is Odd!" %x

def largest_divisor_five(x=120):
    """Find which is the largest divisor of x among 2,3,4,5"""
    largest = 0
    if x % 5 == 0:
        largest = 5
    elif x % 4 == 0: #means "else, if"
        largest = 4
    elif x % 3 == 0:
        largest = 3
    elif x % 2 == 2:
        largest = 2
    else: # When all other (if, elif) conditions are not met
        return "No divisor found for %d!" %x #Each function can return a value or a variable.
        return "The largest divisor of %d is %d" % (x,largest)

def is_prime (x=70):
    """Find whether an integer is prime."""
    for i in range(2,x): #"range" returns a sequence of integers
        if x % i == 0:
            print("%d is not a prime: %d is a divisor" % (x,i)) #Print formatted text "%d %s %f %e" % (20,"30",0.0003,0.00003)

            return False
    print("%d is a prime!" % x)
    return True

def find_all_primes(x=22):
    """Find all the primes up to x"""
    allprimes = []
    for i in range(2,x+1):
        if is_prime(i):
            allprimes.append(i)
    print("There are %d primes between 2 and %d" % (len(allprimes),x))
    return allprimes

def main(argv): #this can be modified to do anything you need
    """ Main entry point of the program """
    print(even_or_odd(22))
    print(even_or_odd(33))
    print(largest_divisor_five(120))
    print(largest_divisor_five(121))
    print(is_prime(60))
    print(is_prime(59))
    print(find_all_primes(100))
    return 0

if __name__ == "__main__": #this is what the interpreter looks for first
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv) #catch all arguments fed into the def
    sys.exit(status) #pass the arguments to the main function (above)