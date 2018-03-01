#!/bin/env/python
#Exercise 29 What if

#Set numbers to variables people, cats and dogs
people = 20 
cats = 30
dogs = 15

#Set an if statement with a string dependent on it. 
#if a string returns TRUE, do function

#This statement is TRUE, so it should show up
if people < cats:
	print "Too many cats! The world is doomed!"

#This statement is FALSE, so it should not show up
if people > cats:
        print "Not many cats! The world is saved!"

#This statement is FALSE, so it should not show up
if people < dogs:
        print "The world is drooled on!"

#This statement is TRUE, so it should show up
if people > dogs:
        print "The world is dry!"

#Set variable dogs within a range of 5 more or 5 less than its original value
dogs += 5

#This statement is TRUE, so it should show up
if people >= dogs:
	print "People are greater than or equal to dogs."

#This statement is TRUE, so it should show up
if people <= dogs:
	print "People are less than or equal to dogs."

#This statement is TRUE, so it should show up
if people == dogs:
	print "People are dogs."
