#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user62','user62','batch62')
cur = conn.cursor()
cur.execute("select version()")
output = cur.fetchone()
print output[0].split('-')[0]