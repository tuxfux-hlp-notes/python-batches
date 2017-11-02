#!/usr/bin/python
# continue - skip your iteration
absent = ['kumar','ram','navya']
for student in ('mayuri','sowji','priyanka','kumar','ravi','reddy','anand','ram','navya'):
	if student in absent:
		continue
		#break
		#pass
	print "results of student - {}".format(student)