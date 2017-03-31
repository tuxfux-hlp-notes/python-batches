#!/usr/bin/python
# break : it breaks you out of the loop.
# sys.exit : take you out of the program.

import sys

yes_no = raw_input("do you want to play the game: y/n - ")
if yes_no == 'n':
    sys.exit()

number = 7
#test = True

#while test:  # LOOKS FOR THE TRUTH OF A CONDITION
count=1
while count <=3:
    answer = input("please enter your number:")
    count = count + 1
    if answer > number:
        print "buddy !! the number you guessed is slightly larger"
    elif answer < number:
        print "buddy !! the number you guessed is slightly smaller"
    else:
        print "you guessed the right number"
        break
        #test = False
        
print "thank you for playing the game"

'''
Task:
please make sure your friend can only enter number 3 times.
if he failed 3rd time say - thank you buddy !!! better luck next time
'''
