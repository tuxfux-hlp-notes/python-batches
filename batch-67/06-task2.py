#!/usr/bin/python3
'''
my_fruits = ['apple','banana','apple','banana','cherry','apple']

output:
my_dupli = ['apple','banana']
my_fruits = ['apple','banana','cherry'] 

'''
my_fruits = ['apple','banana','apple','banana','cherry','apple']
#my_fruits = ['apple','banana','apple','banana','cherry']
my_dupli = []
for value in my_fruits[:]:
	if my_fruits.count(value) > 1:
		if value not in my_dupli:
			my_dupli.append(value)
		my_fruits.remove(value)

print (my_dupli)
print (my_fruits)