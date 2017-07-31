#!/usr/bin/python
import MySQLdb as mdb
#con = mdb.connect('servername','username','password','databasename')
con = mdb.connect('localhost','user63','user63','batch63')
cur = con.cursor()
cur.execute("select user()")
output = cur.fetchone()
print output[0].split('@')[0]
con.close()
