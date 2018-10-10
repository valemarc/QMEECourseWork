#!/usr/bin/env python3

"""Boilerplate python script"""

__appname__ = 'Boilerplate python script'
__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import sys # module to interface our program with the operating system

## constants ##


## functions ##
def main(argv): #this can be modified to do anything you need
    """ Main entry point of the program """
    print('This is a boilerplate') # NOTE: indented using two tabs or 4 spaces
    return 0

if __name__ == "__main__": #this is what the interpreter looks for first
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv) #catch all arguments fed into the def
    sys.exit(status) #pass the arguments to the main function (above)