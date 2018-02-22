#!/bin/env/python
"""This is Zed's Learn Python the Hard Way: Exercise 17."""

#Import the class(or function, I dunno which yet) argv from module named sys
from sys import argv

#Import the function exists from class path within module os
from os.path import exists

print argv


#Set variables for argv function
script, from_file, to_file = argv

#Write a string indicating that you'll be copying something from file to new file
print "Copying from %s to %s" % (from_file, to_file)

#How can this be done in one line? 
#Set variables for your input file and the input data from your file
in_file = open(from_file)
indata = in_file.read()

#Use indata variable to print file size in a string
print "The input file is %d bytes long" % len(indata)
print "Ready, hit RETURN to continue, CTRL-C to abort."

#Create a new file to write this info to
out_file = open(to_file, 'w')
out_file.write(indata)
print "Alright, all done!"

out_file.close()
in_file.close()
