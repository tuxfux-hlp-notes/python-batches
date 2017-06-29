#!/usr/bin/python
# guess the number in the palm of your friend.
# break - break is way of coming out of the loop abruptly.
# sys.exit - take your out of the program.
# task: restrict the people to max tries for 3 times

import sys

number = 7
#test = True # boolean

answer = raw_input("Do you want to play the game: y/n ?")
if answer == 'n':
	sys.exit()



# while always works on truth of a statement/condtion
#while test:
while True:
	guess_num = int(raw_input("please enter your number:"))
	if guess_num > number:
		print "Buddy!! the number you guessed is slightly larger !!"
	elif guess_num < number:
		print "Buddy!! the number you guessed is slightly smaller !!"
	elif guess_num == number:
		print "congo!!! buddy you guessed the right number !!"
		#test=False # boolean
		break


print "Thanks for playing the game!! please visit us again!!"