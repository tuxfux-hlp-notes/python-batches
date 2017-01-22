#!/usr/bin/env python
import cgi
print "Content-type: text/html"
print 
form=cgi.FieldStorage()
print "value {} \n".format(form)
gender=form['gender'].value
name=form['name'].value
print "going to fill the following details into database - %s,%s" %(name,gender)

