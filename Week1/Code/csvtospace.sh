#!/bin/bash
# Author: Valentina Marconi valentina.marconi@imperial.ac.uk
# Script: csvtospace.sh
# Desc: converts a csv file to a space separated values file
# Arguments: csv file
# Date: Oct 2018

echo "Creating a space separated version of $1 ..."
#cd ../Data/Temperatures
#find . -maxdepth 1 -name "*.csv"
cat $1|tr -s ","  "\t" >> $1.txt
echo "Done!"
#exit
#for file in *.csv; do cat $file | tr -s "," " "  >> $1.csv; done
#echo "Done!"
#exit
#echo "Creating a space separated version of $1..."
