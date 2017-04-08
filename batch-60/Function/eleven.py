#!/usr/bin/python
# map,filter,lambda
# when even your get a return value for a function.. Its called the truth of the function.
# if you are not getting the return value or getting None. The function is said to return False or function
# is false.

# map

def square(a):
	return a * a

print square(2)
print square(4)
print square(21)


'''
In [1]: map?
Docstring:
map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).
Type:      builtin_function_or_method
'''

print map(square,(11,21,31,41,51,61,71)) # [121, 441, 961, 1681, 2601, 3721, 5041]

# filter

def even(a):
	if a % 2 == 0:
		return 'even'

print even(2) 
print even(3)

'''
In [1]: filter?
Docstring:
filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list.
Type:      builtin_function_or_method
'''

print filter(even,(11,22,33,44,55,66,77,88,99,100)) # (22, 44, 66, 88, 100)


# 
print map(square,(11,21,31,41,51,61,71))    # [121, 441, 961, 1681, 2601, 3721, 5041]
print filter(square,(11,21,31,41,51,61,71)) # (11,21,31,41,51,61,71

# 
print filter(even,(11,22,33,44,55,66,77,88,99,100)) # (22, 44, 66, 88, 100)
print map(even,(11,22,33,44,55,66,77,88,99,100)) 
# [None, 'even', None, 'even', None, 'even', None, 'even', None, 'even']

# lambda - creation nameless function on fly.
print map(square,(11,21,31,41,51,61,71))    # [121, 441, 961, 1681, 2601, 3721, 5041]
print map(lambda a:a*a,(11,21,31,41,51,61,71))
print filter(even,(11,22,33,44,55,66,77,88,99,100)) # (22, 44, 66, 88, 100)
print filter(lambda a:a % 2 == 0,(11,22,33,44,55,66,77,88,99,100))



