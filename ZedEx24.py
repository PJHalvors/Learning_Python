#!/bin/env/python

#This is exercise number 24 from Zed Shaw's book Learn Python the Hard way
#Version of Python is 2.7

#This exercise is more of a review, and goes through what we've learned so far
#Mind you, I've commented on everything as I write so I know what's going on.

#Write a string using the print command
print "Let's practice everything."

#Write a string using the escapes with forward slash
#Using contractions with \'
#Writing a forward slash within a string with \\
#Making your one-liner string into two lines with \n
#Adding a tab indentation in your string with \t
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#Set a variable named poem to a long, visible chunk of text containing new lines and indents

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nore comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#Write a string to display several dashes on your terminal
#This is a top border to your poem
print "--------------"

#Write a string to display your poem
print poem

#Write a string as your bottom border displaying several dashes in your terminal
print "--------------"

#Set your variable 'five' to a numeric equation
five = 10 - 2 + 3 - 6

#Write a string containing a character variable
print "This should be five: %s" % five

#Create a definition with a numeric variable
#within the definiition, set a series of variables to values
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#Set variable start_point to numeric value
start_point = 10000

#Set the three variables from the definition in the secret forumla function
beans, jars, crates = secret_formula(start_point)

#Write two strings using a numeric variable
print "With a starting point of: %d" % start_point
print " We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#Overwrite variable with new equation
start_point = start_point / 10

#Write two strings using numeric variables a different way
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

