#!/usr/bin/python
# break: break will take you out of the loop in a sane way.
# sys.exit: take you out of the program
# task: maximum number of chances - 3
# generate the number randomly between 1,20


import sys

play = raw_input("Do you want to play the game y/n :")
if play == 'n':
	sys.exit()


number = 7 # number in palm
#test=True

# while loop always works on truth of a condition
while True:
	answer = input("please enter your number:")
	if answer > number:
		print "your answer is slightly larger than the number"
	elif answer < number:
		print "your answer is slightly smaller than the number"
	elif answer == number:
		print "Congo!! you guessed the right number"
		#test=False
		break

print "Thank you for playing the game."