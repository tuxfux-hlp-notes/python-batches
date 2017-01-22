#!/usr/bin/env python
import cgi
import MySQLdb as mdb
print "Content-type: text/html"
print 
con = mdb.connect('localhost','user34','user34','batch34')
cur = con.cursor()
form=cgi.FieldStorage()
name=form['name'].value
gender=form['gender'].value
print "going to fill the following details into database - %s,%s" %(name,gender)
cur.executemany("insert into students(name,gender) values (%s,%s)",[(name,gender)])
con.commit()
con.close()

