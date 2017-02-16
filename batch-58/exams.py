#!/usr/bin/python
# continue : its skips an iteration.

for student in ['rajni','madhuri','priya','kumar','sunil','raj','praveen']:
	if student == 'kumar':
		continue
		#break
		#pass
	print "results for the student - {}".format(student)