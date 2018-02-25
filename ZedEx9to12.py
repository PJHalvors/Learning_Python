#!/bin/env/python

#Learn Python the Hard way, Zed Shaw with Python 2.7

#Exercise#9:Printing with new lines
# Forward slash followed by n indicates a new line
#Set variable days to a string listing the days of the week
days = "Mon Tue Wed Thu Fri Sat Sun"

#Set variable months also to a string, with a new line for each month.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#The next two lines each print a string(indicated variable) after a string
print "Here are the days: ", days
print "Here are the months: ", months

#The final string uses triple quotes to insert a LARGE CHUNK OF TEXT
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print"";print"";print"";print"";

#Exercise#10:Escaping the double quotes
#Set variable tabbyMEW to include a tab with the string
tabbyMEW= "\tI'm tabbed in."

#Set variable persian_cat to split the string into two lines using fwdslash-n
persian_cat = "I'm split\non a line."

#Set variable backslash cat to include a backslash(2) by using two backslashes
backslash_cat = "I'm \\ a \\ cat."

#Set variable FATCAT to be multiple lines with triple quote, and tabs with backslash-t
FATCAT = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabbyMEW
print persian_cat
print backslash_cat
print FATCAT

print"";print"";print"";print"";

#Exercise#11:Raw_Inputs to asnwer asked questions
#List string that asks a question about your age (rude, I know...)
print "How old are you?",
#Set variable to prompt a person to answer the question.
#With raw input you can enter whatever character answer you want
age = raw_input()

#List string that asks a question about your height
print "How tall are you?",
#Set variable to prompt a person to answer the question.                      
ht = raw_input()

#List string that asks a question about your weight (rude, I know...)
print "How much do you weigh?",
#Set variable to prompt a person to answer the question.                      
wt = raw_input()

#List a string that formats variables no matter what
print "So, you're %r old, %r tall and %r heavy." % (
	age, ht, wt)

#I changed the code slightly to build|break|re-build. It's a great learning experience.
print"";print"";print"";print"";

#Exercise#12:
#Set variable age to prompt user to answer using the raw input statement

#In this case, make two lines one by placing prompt inside the raw input statement
age = raw_input("How old are you? ")

#Set variable ht for height to prompt user to answer using the raw input statement 
ht = raw_input("How tall are you? ")

#Set variable wt for weight to prompt user to answer using the raw input statement 
wt= raw_input("How much do you weigh? ")

#List a string to include the formatted variables
print "So, you're %r old, %r tall and %r heavy." % (
	age, ht, wt)
