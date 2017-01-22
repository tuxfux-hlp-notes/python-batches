#!/usr/bin/python
import MySQLdb as mdb
con = mdb.connect('localhost','user57','user57','batch57')
# con - handle - variable name
# mdb.connect(server,username,password,database)
cur = con.cursor()
cur.execute("select user()")
output = cur.fetchone()
con.close()
print output[0].split('@')[0]
