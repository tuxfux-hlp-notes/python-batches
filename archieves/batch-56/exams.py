#!/usr/bin/python
# continue: skip the iteration
for student in ('shiva','srikant','sunil','kumar','tarun','swapnil','anunash'):
    if student == 'kumar':
        continue # print all except kumar
        #break    # print shiva,srikant,sunil
        #pass     # print everything
    print "results for the student:{}".format(student)
    
