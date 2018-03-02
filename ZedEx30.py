#!/bin/env/python
#Exercise 30

#Set numeric values to three variables; people, cars, and buses
people = 30
cars = 40
buses = 15

#If there are more cars than people, print a statement to take the cars.
#elif indicates that if the above term is not true but another statement is, print the accompanying statement.
#Else indicates that if all above terms are false, to print the accompanying statement.

if cars > people:
	print "We should take the cars."
elif cars < people: 
	print "We should not take the cars." 
else:
	print "We can't decide."


if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
