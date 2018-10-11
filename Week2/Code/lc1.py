#!/usr/bin/env python3

"""Create list of latin names, common names and mean body mass for all species in the list provided."""

__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'


birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )


#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 
#Create a list of scientific names
sci_names = [x[0] for x in birds]
print(sci_names)
#Create a list of common names
common_names = [x[1] for x in birds]
print(common_names)
#Create a list of mean body masses
mean_bm = [x[2] for x in birds]
print(mean_bm)

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 
##Using for loops
##Print scientific names
for species in birds:
    print(species[0])
    
##Print common names
for species in birds:
    print(species[1])

##Print mean body mass
for species in birds:
    print(species[2])


