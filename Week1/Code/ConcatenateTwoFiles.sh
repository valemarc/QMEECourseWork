#!/bin/bash
# Author: Valentina Marconi valentina.marconi@imperial.ac.uk
# Script: ConcatenateTwoFiles.sh
# Desc: concatenate two files
# Arguments: 2 txt files, name and path of output file
# Date: Oct 2018
cat $1 > $3
cat $2 >> $3
echo "Merged File is"
cat $3
