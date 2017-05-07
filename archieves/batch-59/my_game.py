#!/usr/bin/python
# while
# break: break will take you out of the loop.
# sys.exit : take you out of the program.
# task: make sure the maximum chances you give to your friend should be 3.

import sys

game = raw_input("do you want to play the game ? y/n :")

if game == 'n':
	sys.exit()

number = 7
#test = True

print "welcome to the game"

# you can go into a while block only if the condition is True.
while True:
	guess_num = int(raw_input("please enter your number:"))
	if guess_num > number:
		print "Buddy!!! The number you guessed is larger"
	elif guess_num < number:
		print "Buddy!!! The number you guessed is smaller"
	elif guess_num == number:
		print "Buddy !!! Congratulation."
		#test = False
		break

print "Thanks for playing the game"