#!/usr/bin/python
'''
my_days = ['yesterday','today','tomorrow','dayafter']

output:1

yesterday 9
today     5
tomorrow  8
dayafter  8

output:2

Yesterday
TOday
TOMorrow 
DAYAfter 


#output1
my_days = ['yesterday','today','tomorrow','dayafter']

for value in my_days:
	print value,len(value)



#output2
my_days = ['yesterday','today','tomorrow','dayafter']
for value in my_days:
	#print value,my_days.index(value),value[0:my_days.index(value) + 1]
	print value[:my_days.index(value) + 1].upper() + value[my_days.index(value) + 1:]
'''
