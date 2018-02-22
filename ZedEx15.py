#!/bin/python

#from sys module import interpreter argv
from sys import argv

#list paramters for your argv: your script and the text file you want to read in
script, filename = argv

#set txt as variable for the file you want to open
txt = open(filename)

#Print a string stating your filename
print "Here's your file %r:" % filename

#Output string to read your text file. The screen will spit the contents out of your text.
print txt.read()

#Prompt reader to type the file name in again. Then spit out contents of text file onto screen. 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
