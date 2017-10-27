#!/usr/bin/python
# break: break is used for taking us out of the loop.
# sys.exit : exit out of the program.
# task1 : i want the maximum number of attempts to 3.
# task2 : http://www.pythonchallenge.com/pc/def/map.html

import sys

my_number = 7
#test = True

y_n = raw_input("do you want to play the game? y/n:")
if y_n == 'n':
	sys.exit()



#while test:  # truth of a condition
while True:
	guess = int(raw_input("please enter your number:"))
	if guess > my_number:
		print "you guessed a slightly larger number"
	elif guess < my_number:
		print "you guessed a slightly smaller number"
	elif guess == my_number:
		print "Congo,you guessed the right number."
		#test=False
		break


print "Thanks for playing the game."