#!/usr/bin/python
# continue - skips the iteration for you.
absent = ['kumar','sameer','shashank']
students = ('mahesh','nikhil','pavani','kumar','sameer','shashank','lawrence','koushi')
for value in students:
	if value in absent:
		continue
		#break
		#pass
	print "following is the results of {}".format(value)
