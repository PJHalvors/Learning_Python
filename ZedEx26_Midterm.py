#!/bin/env/python
print """I copied the code from https://learnpythonthehardway.org/book/exercise26.txt as per exercise26 instructions.
I pasted/edited this code using the Atom text editor to read through it a little better.
nano in terminal has a zoom-in option through [command shift +] but there's a bit to go through.
One big fix is the lack of comments, which will help anyone running the code, so I added those in here.
A lot of comments will repeat.Here we go."""
#Note and new comment after sixth run: added space between description of midterm and start of midterm
print"";print"";print"";print"";

#Comment added: Set up a function to isolate each word in a sentence.
def break_words(stuff):
    #Comment added:Describe the function.
    """This function will break up words for us."""
    #Comment added: Set variable to equal function, and activate with the return command.
    words = stuff.split(' ')
    return words

#Comment added: Set up a function to sort each word in a sentence by alphabetical order.
def sort_words(words):
    #Comment added:Describe the function.
    """Sorts the words."""
    #Comment added. Set variable to equal function, and activate with the return command.
    return sorted(words)

#Comment added: Set up a function to print the first word in a sentence.
#After first run. There was a colon missing at the end of line 16. I added it in.
def print_first_word(words):
    #Comment added:Describe the function.
    """Prints the first word after popping it off."""
    #Comment added. Set variable to equal function, and activate with the print command.
    #After eighth run. words.poop is misspelled here.
    word = words.pop(0)
    print word

#Comment added: Set up a function to print the last word in a sentence.
#After second run. There was a parentheses missing at the end of line 34. I added it in.
def print_last_word(words):
    #Comment added:Describe the function.
    """Prints the last word after popping it off."""
    #Comment added. Set variable to equal function, and activate with the print command.
    word = words.pop(-1)
    print word

#Comment added: Set up a function to sort and print all but first and last words in a sentence.
def sort_sentence(sentence):
    #Comment added:Describe the function.
    """Takes in a full sentence and returns the sorted words."""
    #Comment added. Set variable to equal function, and activate with the return command.
    words = break_words(sentence)
    return sort_words(words)

#Comment added: Set up a function to sort and print first and last word in a sentence.
#Comment added: use two previous functions to print first and last word in a given sentence.
def print_first_and_last(sentence):
    #Comment added:Describe the function.
    """Prints the first and last words of the sentence."""
    #Comment added. Set variable to equal function, and activate with the return command.
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#Comment added: Set up a function to sort and print all but first and last words in a sentence.
def print_first_and_last_sorted(sentence):
    #Comment added:Describe the function.
    """Sorts the words then prints the first and last one."""
    #Comment added. Set variable to equal function, and activate using two previously defined functions.
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Comment added: print the string saying let's practice everything.
print "Let's practice everything."

#Comment added: print string using escapes to include ' (\'), backslashes, \n for new line, \t to tab in
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#Comment added: set variable poem to a chunk of text containing new line and tab escapes
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

#Comment added: print new line to set a top border above the poem
print "--------------"

#Comment added: print the contents of the variable poem
print poem

#Comment added: print new line to set a top border above the poem
print "--------------"

#Comment added: set a variable to a numeric equation
#Noticed after fourth run. This is 6 not 5. corrected operators.
#Numeric value does not equal 5!
#To Correct numeric values: original was 10+2-3+5
#Can use: 10 + 2 - 2 + 5 but i don't think that's it. Its a multiple of 10...
#10-2 = 8; 8+3 = 11; 11-6 = five.
#I think weirdly enough, this was the tricky part for me.
five = 10 - 2 + 3 - 6

#Comment added: print a string containing the numeric variable
print "This should be five: %s" % five

#Comment added: create a new function for jelly_beans
def secret_formula(started):
    jelly_beans = started * 500
    #After third run. backslash in line 103 (previously line 80) where forward slash needed
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#Comment added: set numeric value for variable start_point
start_point = 10000
#Comment added: input three variables from above function to get values using start_point
#After sixth run line 112 has two = . (originally line 110).
#corrected to one =
#After seventh run. line 115 (originally line 114): corrected start-point to start_point
beans, jars, crates = secret_formula(start_point)

#Comment added: print string to display start_point variable using numeric formatter %d
print "With a starting point of: %d" % start_point

#Comment added: print string containing three numeric formatters for the three variables beans, jars, crates
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

#Comment added: set new value for start_point variable
start_point = start_point / 10

#Comment added: Print string with a sentence
print "We can also do that this way:"
#Comment added: print string containing three numeric formatters for the three variables beans, jars, crates
#After fourth run. This wasn't shown, but start_point was originally written as start_pont
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

#After fourth run. The error was shown here in line 128 (originally line 120)
#After fourth run. Spell checking. And Grammar. Holy Moly.
sentence = "All good\tthings come to those who wait."

#Comment added: Removed ex25 in the two lines below (line 132, 133). It is not needed for this exercise.
#Comment added: Set variable words to equal a function in the above variable sentence.
words = break_words(sentence)

#Comment added: Set variable sorted_words to equal or return output of function sort_words.
#Comment added: Return a function within a function
sorted_words = sort_words(words)

#Comment added: Return functions containing the variable words.
#Comment added: Print the first word of all returned words in a sentence.
print_first_word(words)

#Comment added: Print the last word of all returned words in a sentence.
print_last_word(words)

#Comment added: Print the first word of all returned sorted words in a sentence.
#After fifth run. remove the [.] at the beginning of line 146 (originally line 136)
print_first_word(sorted_words)

#Comment added: Print the last word of all returned sorted words in a sentence.
print_last_word(sorted_words)

#Comment added: set the variable sorted_words to display in alphabetical order
sorted_words = sort_sentence(sentence)

#After fifth run. noticed that print is mis-typed as prin. That has been corrected here.
#Comment added: Print the contents of variable sorted_words
print sorted_words

#After fifth run. noticed that print_first_and_last is mis-typed as print_irst_and_last.
#That has been corrected here.
#Comment added: Print the first and last word of the sentence
print_first_and_last(sentence)

#After fifth run. noticed that print_first_and_last_sorted is mis-typed as print_first_a_last_sorted.
#After fifth run. noticed that print_first_and_last is tabbed in.
#variable sentence is misspelled as senence.
#That has been corrected here.
#Comment added: Print the first and last words in the list of sorted words from sentence.
print_first_and_last_sorted(sentence)
