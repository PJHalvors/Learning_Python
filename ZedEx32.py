#!/bin/env/python
#Exercise 33

#Set list name the_count to equal numeric values 1,2,3,4,5
the_count = [1, 2, 3, 4, 5]

#Set list name fruits to equal numeric values 'apples', 'oranges', 'pears', 'apricots'
fruits = ['apples', 'oranges', 'pears', 'apricots']

#Set list name change to numeric and character values 1, 'pennies', 2, 'dimes', 3, 'quarters'
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This is the first kind of for-loop that goies through a list
#print a statement that includes a formatter for each number in the_count list
for number in the_count:
	print "This is count %d" % number

#same as above
#print a statement that includes a formatter for each character-term in the fruit list
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
# we can also build lists, first start with an empty one
	elements = []
# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Element was: %d" % i
#Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?

NewList = [range(2,5)]
print "Adding %r to the list." % range
NewList.append(range)
print NewList	
