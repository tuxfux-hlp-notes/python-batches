#!/usr/bin/python

'''
task1:

Input:
my_fruits = ['apple','banana','apple','banana','cherry']

Output:
my_fruits = ['apple','banana','cherry']
my_dupli = ['apple','banana']

'''

my_dupli = []
my_fruits = ['apple','banana','apple','banana','cherry','apple']
print "my initial fruits {}".format(my_fruits)
for value in my_fruits[:]:
	print "my value is {}:".format(value)
	if my_fruits.count(value) > 1:
		if value not in my_dupli:
			my_dupli.append(value)
		my_fruits.remove(value)
		#print my_fruits

print my_fruits
print my_dupli
