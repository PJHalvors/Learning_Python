#!/bin/env/python
#This is exercise 25 from Zeds book. I comment everything, so that's added in too.


#Make a function to break words in a sentence
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

#Each of these functions has a description, a variable and its function.There are seven of these here.

#Make a function to sort through words in a sentence
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

#Isolate and print the first word from a sentence
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

#Isolate and print the last word from a sentence
def print_last_word(words):
        """Prints the last word after popping it off."""
        word = words.pop(-1)
        print word

#Return sorted words in a sentence
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)


#Display the first and last word of a sentence
def print_first_and_last(sentence):
        """Sorts the words then prints the first and last one."""
        words = sort_sentence(sentence)
        print_first_word(words)
        print_last_word(words)

#Display the first and last word of a sentence
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
