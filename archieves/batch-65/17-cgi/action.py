#!/usr/bin/env python
print "Content-type: text/html"
print 
import cgi
import MySQLdb as mdb
con = mdb.connect('localhost','user65','user65','batch65')
cur = con.cursor()
form=cgi.FieldStorage()
name=form['name'].value
gender=form['gender'].value
print "going to fill the following details into database - %s,%s" %(name,gender)
cur.executemany("insert into student (name,gender) values (%s,%s)",[(name,gender)])
con.commit()
con.close()


