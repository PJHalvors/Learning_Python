#!/bin/env/python

#Set your definition for adding two variables
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

#Set your definition for subtracting two variables
def subtract(a, b):
        print "SUBTRACTING  %d - %d" % (a, b)
        return a - b

#Set your definition for MULTIPLYING two variables
def multiply(a, b):
        print "MULTIPLYING %d * %d" % (a, b)
        return a * b
#Set your definition for DIVIDING two variables
def divide(a, b):
        print "DIVIDING %d / %d" % (a, b)
        return a / b

print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(78, 4)
htft = height / 12
weight = multiply (65, 2)
iq = divide (100, 2)

print "Age: %d, Height %d, Weight: %d, IQ: %d" % (age, htft, weight, iq)

# A puzzle for extra credit, type it in anyway.

print "Here is a puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "Can you do it by hand?"
