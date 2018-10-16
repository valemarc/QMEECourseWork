#!/usr/bin/env python3

"""Align DNA sequences and calculate alignment scores"""

__appname__ = 'Align DNA'
__author__ = 'Valentina Marconi (valentina.marconi@ioz.ac.uk)'
__version__ = '0.0.1'

# Read in csv file from the data folder
import csv
f = open('../Data/seqs.csv','r')
lines = [row for row in f]
seq1 = lines[0].strip('\n')
seq2 = lines[1].strip('\n')

# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest
l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    #import ipdb; ipdb.set_trace()
    for i in range(l2):
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # build some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print("")

    return score


#calculate_score(s1, s2, l1, l2, 0)
#calculate_score(s1, s2, l1, l2, 1)
#calculate_score(s1, s2, l1, l2, 2)

# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1

for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2
        my_best_score = z

print(my_best_align)
print(s1)
print("Best score:", my_best_score)

# write a file containing results of best score
list_to_save = (str(my_best_align), str(my_best_score))
f = open('../Results/best_score.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') ## Add a new line at the end

f.close()

