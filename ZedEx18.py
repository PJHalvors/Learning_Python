#!/bin/env/python

"""Zed Shaw Learn Python the hard way. Lesson # 18"""

#This one is like your scripts with argv
# Tell python, using def for define, to make a function called printtwo
# we want *args (asterisk args), like  argv parameter but for functions.
# This has to go inside () parentheses to work.

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#This one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
