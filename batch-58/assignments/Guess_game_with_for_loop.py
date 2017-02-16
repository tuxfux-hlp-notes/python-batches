#!/usr/bin/python3

import sys

def_num = 5
i = 1 

print("Hi buudy... Welcome to the guess game.")
choice = input("Do you want to play the game. Press Y/N: ")

if choice == 'N' or choice == 'n':
	print("Sorry to see u exit.... Have a nice time. \n")
	sys.exit()
for i in range(3):
	guess_num = int(input("Guess any no. from 1 to 10: "))
	if guess_num<def_num :
		print("Noo buddy... u have chosen a slightly smaller no.\n")
	if guess_num>def_num :
		print("Noo buddy... u have chosen a slightly larger no.\n")
	if guess_num==def_num :
		print("Suuper... what a guess yaar.\n ***Congos***")
		sys.exit()
	
print("Sorry buddy... your 3 attempts got completed. Better luck next time. ")
