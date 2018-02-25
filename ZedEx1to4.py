#!/bin/env/python
#This program contains exercises Num1 to Num4 from Zed's Book

#Excercise 1: Printing strings
#In this exercise using the print command, print seven strings
#The text in a few of the strings may have slightly been changed, only to test, break, and re-build code
#You can use a pair of single or double quotes for each string. 
#I prefer double quotes, personally.
#Several of these single lines with a number sign are comments. 
#They appear in code, but not on your terminal.

print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is much too fun."
print 'Woot! iPrint.'

#You can also place a pair of single quotes in a double quote string, like so:
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

#FYI even though i'm on Excercise 25 now, this is stil super helpful for me.
#Don't forget your basics!!!
#FYI to add space in between each exercise I'm inserting [print ""] to make four lines worth of space. Helps me see things a bit better.
print ""
print ""
print ""
print ""
#Exercise #2:Commenting. On. Everything. Is. IMPORTANT!
#Two sample comments, like this one and the one above, are listed below:
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

#You can add a comment within each string, which helps esp. if string is short
print "I could have code like this." # and the comment after is ignored
'''FYI # is a commenting symbol that helps you explain your code. you can insert at the beginning of any string to disable that string or piece of code.'''
#print "This won't run"
print "This will run."
print ""
print ""
print ""
print ""
#Exercise 3: Math in Python

#Display sentence in a string
print "I will count my chickens."

#In line list string followed by equation. I use more spaces that I probably should, but I like it that way.
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7 #This should show up FALSE. 5 is not less than -2
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print " Is it greater?", 5 > -2 #This should show up TRUE
print " Is it greater or equal?", 5 >= -2 #This should show up TRUE
print " Is it less or equal?", 5 <= -2 #This should show up FALSE

#So in Exercise#3, Python can be a calculator, the percent sign is a modulus and shows remainders from division, and python follows PEMDAS
print ""
print ""
print ""
print ""
#Exercise 4: Variables and Naming things
#Note: I changed the numbers to test/break and re-build the code. 

#Set variables to numbers or equations with those variables
cars = 125
space_in_a_car = 5.0 
drivers = 25
passengers = 75 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Write six strings that include one of the above variables in each string
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


