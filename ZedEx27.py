#!/bin/env/python

#Exercise 27: Memorizing Logic
#In addition to printing cards, I wanted to practice integrating logical terms into code we're already using.

print "Not indicates the opposite of logical terms True and False."
Boolean_Not1 = not False
Boolean_Not2 = not True
print "Here's an example; not False is %s and not True is %s." % (Boolean_Not1, Boolean_Not2)
print""

print "Or will take a combination of True and False, preferentially returning true with one exception of False and False."
Boolean_Or1 = True or True
Boolean_Or2 = True or False
Boolean_Or3 = False or True
Boolean_Or4 = False or False
print "Here's an example; True or True, False or True, True or False return %s,%s, %s but False and False return %s." % (Boolean_Or1, Boolean_Or2, Boolean_Or3, Boolean_Or4)
print""

print "And will take a combination of True and False, returning False because at least one must return True."
Boolean_A1 = True and True
Boolean_A2 = True and False
Boolean_A3 = False and True
Boolean_A4 = False and False
print "Here's an example; True/True returns %s, but True/False, False/True and False/False return %s, %s, and %s." % (Boolean_A1, Boolean_A2, Boolean_A3, Boolean_A4)
print""

print "What happens if we add a not before each boolean phrase?"
nBO1 = not(True or True)
nBO2 = not(True or False)
nBO3 = not(False or True)
nBO4 = not(False or False)
nBA1 = not(True and True)
nBA2 = not(True and False)
nBA3 = not(False and True)
nBA4 = not(False and False)

print "Not with and takes True/True and returns %s, but True/False, False/True and False/False return %s, %s, and %s." % (nBA1, nBA2, nBA3, nBA4)

print "Not with or takes True/True and returns %s, but True/False, False/True and False/False return %s, %s, and %s." % (nBO1, nBO2, nBO3, nBO4)
print""
print "Let's try these: 1 != 0, 1 != 1, 0 != 1, 0 != 0"
print 1 != 0
print 1 != 1
print 0 != 1
print 0 != 0
print""
print "How about these: 1==0,1==1,0==1,0==0"
print 1 == 0
print 1 == 1
print 0 == 1
print 0 == 0

