#!/usr/bin/python
# usage: learning modules in depth

version=2.0

def my_add(a,b):
  ''' this function is for addition of numbers and strings '''
  return a + b
  
def my_sub(a,b):
  ''' This function is for the substraction of two numbers '''
  if a > b:
    return a - b
  else:
    return b - a
    
def my_div(a,b=1):  
   # b is a default value. Just to make sure that no one makes it zero and we hit on an exception.
   ''' This function is for division of numbers '''
   return a/b
   
def my_multi(a,b):
   ''' This function is for the multiplication of the numbers '''
   return a * b 
   

# Main
if __name__ == '__main__':
  print "i am launchng a missile."
