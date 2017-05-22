#!/usr/bin/env python
print "Content-type: text/html"
print 
print "<html><head><title>students data</title></head>"
print "<body>"
print "<h1>students details</h1>"
print "<ul>"
import MySQLdb as mdb
con = mdb.connect('localhost','user58','user58','batch58')
cur = con.cursor()
cur.execute("select * from student")
for i in range(cur.rowcount):
  row = cur.fetchone()
  print "<li>Name:%s  Gender:%s</li>" %(row[0],row[1])
print "</ul>"
print "</body></html>"
con.close()

