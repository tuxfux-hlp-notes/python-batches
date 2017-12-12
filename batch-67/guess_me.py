#!/usr/bin/python
# break: break is a keyword which will take you out of the loop.
# sys.exit : take you out of the program.
# stop after 3 iterations max.

import sys
y_n = raw_input("do you want to play game - y/n ?")
if y_n == 'n':
	sys.exit()

number = 7  # randomize this number.. hint ? rand
#test = True

#while test:  # while works on truth of a condition
while True:
	answer = int(raw_input("please guess your number:"))
	if answer > number:
		print "the number you guessed is slightly larger."
	elif answer < number:
		print "the number you guessed is slightly smaller."
	elif answer == number:
		print "Congo!! you won the game."
#		test=False
		break

print "Thanks for playing the game."


'''
outer loop
 inner loop
 	break

'''