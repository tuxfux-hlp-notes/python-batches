#!/usr/bin/python
name = raw_input("please enter the student name:")
if name in my_students:
    print "{} is going to give exam {}".format(name,my_exams[my_students.index(name)])
    
