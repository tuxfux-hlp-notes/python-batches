#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user67','user67','batch67')
#conn = mdb.connect('db servername','username','password','database')
cur = conn.cursor()
cur.execute('select version()')
output=cur.fetchone()
print output[0].split('-')[0]
