#!/usr/bin/python
# usage: A debugging class
# pdb.set_trace
import pdb

version=2.0

def my_add(a,b):
  ''' This is the function for addition of numbers and strings '''
  print "value of a is {}".format(a)
  print "value of b is {}".format(b)
  return a+b
  
def my_div(a,b):
  ''' This is the function for division '''
  return a/b
  
def my_sub(a,b):
  ''' This is the function for substraction '''
  if a > b:
    return a - b
  elif b > a:
    return b - a
    
def my_mul(a,b):
  ''' This is the function for multiplication '''
  return a * b
  
# Application code

if __name__ == '__main__':
  print "This is a example on understading debugging"
  print "Congo, i learned to write a calculator"
  pdb.set_trace()
  print "summation of two numbers-> {}".format(my_add(1,2))
  print "multiplication of two numbers -> {}".format(my_mul(1,2))
  print "substartion of two numbers -> {}".format(my_sub(1,2))
  print "division of two numbers -> {}".format(my_div(4,2))

	
