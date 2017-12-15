#!/usr/bin/python
absentees = ['sridhar','chetan','yaseen','balu','kumar']
for student in ['sridhar','komala','chetan','kumar','rajesh','balu','ravi','yaseen']:
	if student in absentees:
		continue
		#break
		#pass
	print "results of {}.".format(student)