#!/usr/bin/python
# break: take you out the loop .
# sys.exit: take you out of the program. 

import sys

answer = raw_input("do you want to play the game - y/n:")
if answer == 'n':
	sys.exit()



my_num = 7 # number written on palm
#test= True

# while loop always works on truth of a condition.
#while test:
while True:
	num = int(raw_input("please enter your number:"))
	if num == my_num:
		print "congo!! you guessed the right number"
		break
		#test=False
	elif num > my_num:
		print "you guessed a number slightly larger"
	elif num < my_num:
		print "you guessed a number slightly smaller"

print "Please visit us again!!"