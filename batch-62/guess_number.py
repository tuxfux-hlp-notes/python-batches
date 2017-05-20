#!/usr/bin/python
# break : take you out of the loop.
# sys.exit : to take you out of the program.
# hw:
# task1: reduce the number of chances/guesses to 3.
# task2: rand function to generate random numbers for number variable.

import sys

yn = raw_input("do you want to play the game:")
if yn == 'n':
    sys.exit()

number = 7
#test = True

# while test:
while True:
    answer = int(raw_input("please guess your number:"))
    if answer > number:
        print "buddy!!! you guessed a number slightly larger"
    elif answer < number:
        print "buddy!!! you guessed a number sligthly smaller"
    elif answer == number:
        print "congo!! you guessed the right number"
        #test = False
        break
        
print "Please come back to play again !!!"
