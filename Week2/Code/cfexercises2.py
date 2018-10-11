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
def elevate(x):
    """Elevate a number to the power of 0.5."""
    return x ** 0.5

def greatest(x,y):
    """Return the greater number between the two."""
    if x>y:
        return x
    return y

def swap(x,y,z):
    """Order numbers."""
    if x > y:
        tmp = y
        y = xq
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x,y,z]

def multiply(x):
    """Multiply 1 by the number you provide plus 1."""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def recurs(x): # a recursive function
    """Recursive multiplication."""
    if x == 1:
        return 1
    return x * recurs(x - 1)

def main(argv): #this can be modified to do anything you need
    """ Main entry point of the program """
    print(elevate(22))
    print(greatest(33,35))
    print(swap(120,130,140))
    print(multiply(60))
    print(recurs(59))
    return 0

if __name__ == "__main__": #this is what the interpreter looks for first
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv) #catch all arguments fed into the def
    sys.exit(status) #pass the arguments to the main function (above)