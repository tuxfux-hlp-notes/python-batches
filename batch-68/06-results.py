#!/usr/bin/python
# continue: skip an interation
absentee = ['kumar','madhu']
for student in ('navya','mukunda','vinay','kumar','naresh','raja','bala','madhu'):
	#if student == 'kumar':
	if student in absentee:
		continue
		#break
		#pass
	print "results for - {}".format(student)
