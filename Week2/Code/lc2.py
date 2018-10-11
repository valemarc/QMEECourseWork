#!/usr/bin/env python3

"""Create list of months with more than 100mm rainfall and less than 50mm rainfall in 1910."""

__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
months_over_100 = tuple([x for x in rainfall if x[1]>100])
print(months_over_100)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 
months_under_50 = [x[0] for x in rainfall if x[1]<50]
print(months_under_50)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 
#create a list of month,rainfall tuples where the amount of rain was greater than 100 mm
for month in rainfall:
    if month[1]>100:
        print(tuple(month))

###Creating a list of months where the amount of rain was less than 50 mm
##Using for loops
for month in rainfall:
    if month[1]<50:
        print(month[0])


