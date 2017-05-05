#!/usr/bin/python
# break: take your out of the loop .
# sys.exit : take you out of the program.
# task: come up with a logic to close the program after 3 attempts.

import sys
answer = raw_input("do you want to play the game - y/n ?")
if answer == 'n':
    sys.exit()

number = 7   # hiding it in my palm
count = 0
#test=True

#while test:
while count<3:
    guess_number = int(raw_input("please guess the number:"))
    if guess_number > number:
        print "buddy!! you guessed the number slighly larger"
        count=count+1
    elif guess_number < number:
        print "buddy!! you guessed the number slighly smaller"
        count = count+1
    elif guess_number == number:
        print "congo!! you guessed the right number"
        #test=False
        break
        
print "thanks for playing the game"
