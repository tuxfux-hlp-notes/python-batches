#!/usr/bin/python

balance = 0

def deposit():
    global balance
    balance = balance + 1000
    return balance

def withdraw():
	global balance
	balance = balance - 200
	return balance

## saleem

print "balance of saleem before deposit {}".format(balance)
deposit()
print "balance of saleem after deposit {}".format(balance)
withdraw()
print "balance of saleem after withdraw {}".format(balance)

# navya
print "balance of navya before deposit {}".format(balance)



