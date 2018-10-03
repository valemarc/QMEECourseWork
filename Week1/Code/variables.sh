#!/bin/bash
# Author: Valentina Marconi valentina.marconi@imperial.ac.uk
# Script: variables.sh
# Desc: shows the use of variables
# Arguments: 1 string of carachters, 2 numbers separated by a space
# Date: Oct 2018
MyVar='some string'
echo 'the current value of the variable is' $MyVar
echo 'Please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar
##Reading multiple values
echo 'Enter two numbers separated by space(s)'
read a b
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum

