#!/bin/python

#Import argv from sys module
from sys import argv

#list variables for argv parameters
script, filename = argv

#write three strings with the print command
print "We're going to erase %r." % filename
print "If you don't want that, hit, CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#Open your text file in current directory
print "Opening the file..."
target = open(filename, 'w')

#Erase previous lines in file
print "Truncating the file. GoodBye!"
target.truncate()

#Write three lines for text file
print "Now i'm going to ask you for three lines."

line1 = raw_input("line 1: ") 
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#Write each line to a file as seperate line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing Time"

target.close()
