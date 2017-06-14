#!/usr/bin/python
#import pdb

def first():
  second()
  return "hey i am first"

def second():
  third()
  return "hey i am second"

def third():
  fourth()
  return "hey i am third"

def fourth():
  fifth()
  return "hey i am fourth"

def fifth():
  return "hey i am fifth"

# MAIN
#pdb.set_trace()
first()
