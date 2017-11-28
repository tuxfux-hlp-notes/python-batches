#!/usr/bin/python
import MySQLdb as mdb
con = mdb.connect('localhost','user66','user66','batch66')
cur = con.cursor()
cur.execute('select version()')
output = cur.fetchone()
print output[0].split('-')[0]
