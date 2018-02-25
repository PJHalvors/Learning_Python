#!/bin/env/python

#This program contains exercises Num5 to Num8 from Zed's Book

#Exercise5:Printing with variables

#Set variables to numeric or characters
name = "PJ"
age = 25 #arbitrary number
ht = 68.125 #also arbitrary
wt = 125 #also also arbitrary
eyes = 'Almond'
teeth = 'White'
hair = 'Purple-Undercut' #I totally wish! This would be so cool!!

#Write six strings inserting character or numeric variables
print "Let's talk about %s." % name
print "She's %d inches tall." % ht
print "She's %d pounds heavy." % wt
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Those teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d."%(
	age, ht, wt, age + ht + wt)

print"";print"";print"";print"";

#Exercise6:Strings and text

#Set variable x to a string containing a numeric insert, variable to character values, and var y to another string
x = "There are %d types of people." % 10
binary = "binary"; do_not = "don't";
y = "Those who know %s and those who %s." % (binary, do_not)

#Display two strings, which contain variables. String within a string. Twice. 
print x
print y

#Display a string within a string. Twice.
print "I said: %r." % x
print "I also said: '%s'." % y

#Set variables to alphanumeric values
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Display string with the above two variables. String in a string here. 
print joke_evaluation % hilarious

#Set variables w and e to strings
w = "This is the left side of..."
e = "a string with a right side."

#Write out both strings. 3 things: 2 strings in a string, and a string in a string twice.
print w + e

#Need Spaces!
print"";print"";print"";print"";

#Exercise7:
#The first three lines each print a string.
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."

#Print ten punctuation marks in a row
print "." * 10 

#Set twelve variables to twelve character values
#To save space, I'm using a semicolon to place more than one line in the same line. 
#This results in two lines with six variables to a character value per variable
end1 = "C";end2 = "h";end3 = "e";end4 = "e";end5 = "s";end6 = "e"
end7 = "B";end8 = "u";end9 = "r";end10 = "g";end11 = "e";end12 = "r";

#Print one whole string with all twelve character values
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#Removing the comma at the end of end6 variable yields two lines with six variables each
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

print"";print"";print"";print"";

#Exercise8:Printing with formatters
#Set a variable formatter to print for values no matter what
#Percent r means values can be alphanumeric or even strings
formatter = "%r %r %r %r"

#Print string where there are numbers inserted in a formatter
print formatter % (1, 2, 3, 4)

#Print string with characters (words as string) inserted
print formatter % ("one", "two", "three", "four")

#Print variable formatter with True or False inserted in
print formatter % (True, False, False, True)

#Print content in the string for formatter times four
print formatter % (formatter, formatter, formatter, formatter)

#Print four strings in the next string
print formatter % (
	"I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
