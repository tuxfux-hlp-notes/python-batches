#!/usr/bin/python
# while always work on truth of a condition.
# break - break is a sane way of coming out of a loop.
# sys.exit - take you out of the program.
# task I: make sure the maximum attempt is only 3. 
# if its more than 3,please try another time.
# task II: you can generate random number for number variable.
# rand

import sys

number = 7
#test = True

play = raw_input("do you want to play the game: y/n -")
if play == 'n':
	sys.exit()

#while test:
while True:
	answer = input("please enter your number:")
	if answer > number:
		print "buddy you answer is slightly larger."
	elif answer < number:
		print "buddy your answer is slightly smaller."
	elif answer == number:
		print "Congo!!! buddy you guessed the right number"
		#test=False
		break

print "Thanks for playing our game !!"