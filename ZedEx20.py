#!/bin/env/python

#Import modules
from sys import argv

#List the two file types you'll use for argv
script, input_file = argv

#Define your print function
def print_all(f):
	print f.read()

#Define your find function
def rewind(f):
	f.seek(0)

#Define how you'll calculate the number of lines in your file
def print_a_line(line_count, f):
	print line_count, f.readline()

#Name your current file you'll use as a variable
current_file = open(input_file)

#Print string to open entire file (I think the cat command in UNIX does this)
print "First let's print the whole file:\n"

#As the previous string tells you, display the whole file
print_all(current_file)

#Print string to begin at start of file, e.g. rewind
print "Now let's rewind, kind of like a tape."

rewind(current_file)

#Let user know that you will display the first three lines in your terminal
#Then do that.

print "Let's print three lines."

current_line = 1
print_a_line(current_line, current_file)

current_line =  current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
