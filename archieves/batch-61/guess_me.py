#!/usr/bin/python
# break : you are abruptly taken out of a loop.
# sys.exit: a quick way to exit out of a program.

import sys

play_or_not = input("do you want to play the game: y/n ->")

if play_or_not == 'n':
	sys.exit()

number = 7 # numbe in my palm
#test = True

# max number of tries is 3.
#while test:
while True:
	num = input("please enter the number:")
	if num > number:
		print "the number you guessed is sligthly larger."
	if num < number:
		print "the number you guessed is slightly smaller"
	if num == number:
		print "Congo!! you guessed the right number"
		break
		#test=False

print "Thanks for playing the game."
