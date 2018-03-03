#!/bin/env/python

#Exercise 36

from sys import exit
import webbrowser

def piled_high_deep():
  print "Welcome to the Grad School Gauntlet! Let's begin. Do you want to take classes or skip to setting up a committee?"
  while True:
      next = raw_input("> ")
      if "classes" in next:
          print "How many classes do you want to take?"
          course = int(raw_input())
          if course >= 2:
            webbrowser.open ('http://whatshouldwecallgradschool.tumblr.com/post/28776049736/going-back-to-classes-in-the-fall')
            dead("Dear lord, why so many? You can't do lab work with that much homework!")
      else:
            print "Smart choice. Now go put your committee together."
            print ""
            print ""
            quals()
  else:
      dead("Dude. You're getting paid. Just take the classes.")

def quals():
    print "It's QE Time!"
    print "You could write your own. Or pick two topics."
    print "But if you pick two, your committee picks their fave one."
    print "Do you want your own topic or two new topics?"
    Topic = raw_input("> ")
for Topic in quals():
	if "my own" in Topic:
		print "Great! You're an expert on this, right?"
	    expert = raw_input("> ")
	if "wrong" in expert:
			webbrowser.open ('http://whatshouldwecallgradschool.tumblr.com/post/147210406637/questions-during-my-qual')
			dead("Nope? Well, womp wah, you failed.")
	elif "right" in expert:
			webbrowser.open ('http://whatshouldwecallgradschool.tumblr.com/post/103078228013/after-finishing-my-qual-exam')
			print "Woot! You survived!!"
			defense()	
	elif "two new topics" in Topic:
		print "Well, you can do that too. Good luck with the written and defense tests!! Bahahahahahahaha"
		defense()
	else:
		print "You didn't answer the question. Dude. Start Over."
		piled_high_deep()
"""        
def defense():
    print "Are you ready to rumble?"
    if "Yes" in next:
        dead("P0WNED IT!")
        jobs()
    elif "Maybe" in next:
        dead("Stop being so wishy washy.")
    elif "No" in next:
        dead(" Crying? there's no crying in baseball...err...grad school!")
        jobs()
    else:
        dead("Dude.")

def jobs():
    print "You've graduated! Where are you going? (Postdoc/Not)"
    if "Postdoc" in next:
        dead("You won't be in prison forever. But your career just died. Good Job!")
    else:
        dead("Congrats on spending a few millenia, blood sweat and tears on... on...well, what, exactly?")

def dead(why):
    print why, "Ok. Bye now!"
    exit(0)

def start():
    print "You've given blood, sweat, and tears to college classes. Stupid paper cuts."
    print "You've given blood, sweat and more tears to the GRE. Dang paper cuts."
    print "You've poured blood, sweat, and tears into your Apps...why do we get so many paper cuts?!"
    print "Are you ready? (Yep/Nope)"

    next = raw_input("> ")

    if next == "Yep":
        piled_high_deep()
    elif next == "Nope":
        print "Well, ya shouldnadidthat."
    else:
        print "I don't get what you're saying. Try again tomorrow!"
start()
