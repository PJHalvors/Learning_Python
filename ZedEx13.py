#!/bin/python

#Import argument parameters when passed from the sys module
from sys import argv

#List your arguments
script, first, second, third = argv

#Print string while listing off each argument
#Each argument can be replaced (THere are 3) when you run the program
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

