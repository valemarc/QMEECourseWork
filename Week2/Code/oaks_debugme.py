#!/usr/bin/env python3

"""Function to find oak species in a list"""

__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'
__version__ = '0.0.1'


import csv
import sys
import doctest # Import the doctest module

def is_an_oak(name):
    """Find out is a species is an oak.

    >>> is_an_oak("Fagus sylvatica")
    False

    >>> is_an_oak("Quercus robur")
    True

    >>> is_an_oak("Quercusstart")
    False
    """
    name = name.lower()
    name = name.split()[0]
    if len(name) != 7:
        return False
    #Genus, species = name.split(' ')
    return name.startswith("quercus")

def main(argv): 
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    next(taxa, None)
    csvwrite = csv.writer(g)
    csvwrite.writerow(["Genus","species"])
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0])
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0],row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()