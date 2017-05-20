#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user61','user61','batch61')  # connection
# connection datails : server,username,password,database
cursor = conn.cursor()  # Curson is for running queiries on your database.
cursor.execute('select version()') # executes a query for us.
output = cursor.fetchone() # we are fetcching one record.
print "output:{}".format(output[0].split('-')[0])