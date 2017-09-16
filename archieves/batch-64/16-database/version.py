#!/usr/bin/python

import MySQLdb as mdb
con = mdb.connect('localhost','user64','user64','batch64')
cur = con.cursor()
cur.execute("select version()")
output = cur.fetchone()
print output[0].split('-')[0]