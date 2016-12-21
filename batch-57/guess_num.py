#!/usr/bin/python
# break: break will take you out of the loop.
# sys.exit : take you out of the program.

import sys
whatsup = raw_input("do you want to play the game - y/n ?")
if whatsup == 'n':
	sys.exit()

number = 7  # palm
#test = True  



# only when your condition is True, you can go into the block for a while or a for loop.

#while test:
while True:
	answer = input("please enter your number:")
	if answer > number:
		print "buddy!!! you gave a answer slightly larger"
	elif answer < number:
		print "buddy!!! you gave a number slightly smaller"
	elif answer == number:
		print "congo!!! you gave the right answer"
		#test=False
		break

print "thank you for playing the game"

# task
# I want the above program to give max 3 chances and not more than that.
