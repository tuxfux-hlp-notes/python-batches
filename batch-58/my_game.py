#!/usr/bin/python
# break : break is a keyword which takes you out of a loop.
# sys.exit: takes you out of the program.
# Task : make sure you give your friend only 3 chances.

import sys

my_answer = raw_input("do you want to play the game? y/n :")
if my_answer == 'n':
	sys.exit()


my_num = 7 # hidden in my palm
#test = True

# you get into the while block only if your condition satisfies as True
while True:
	guess_num = int(raw_input("please guess the number:"))
	if guess_num > my_num:
		print "Buddy you guessed a slightly larger number"
	elif guess_num < my_num:
		print "Buddy you guessed a slightly smaller number"
	elif guess_num == my_num:
		print "congo!! you guessed the right number"
		#test=False
		break

print "Thanks for playing.Please visit us again."