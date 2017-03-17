#!/usr/bin/python
import MySQLdb as mq
con = mq.connect('localhost','user58','user58','batch58')
cur = con.cursor()
cur.execute("select version()")
output = cur.fetchone()[0]
print output
cur.execute("select user()")
user = cur.fetchone()[0].split('@')[0]
print user
con.close()


'''
In [1]: import MySQLdb as mq

In [2]: mq.connect?
Signature: mq.connect(*args, **kwargs)
Docstring: Factory function for connections.Connection.
File:      /usr/lib/python2.7/dist-packages/MySQLdb/__init__.py
Type:      function

In [3]: con = mq.connect('localhost','user58','user58','batch58')

In [4]: con.cursor?
Signature: con.cursor(cursorclass=None)
Docstring:
Create a cursor on which queries may be performed. The
optional cursorclass parameter is used to create the
Cursor. By default, self.cursorclass=cursors.Cursor is
used.
File:      /usr/lib/python2.7/dist-packages/MySQLdb/connections.py
Type:      instancemethod

In [5]: cur = con.cursor()

In [6]: cur.execute?
Signature: cur.execute(query, args=None)
Docstring:
Execute a query.

query -- string, query to execute on server
args -- optional sequence or mapping, parameters to use with query.

Note: If args is a sequence, then %s must be used as the
parameter placeholder in the query. If a mapping is used,
%(key)s must be used as the placeholder.

Returns long integer rows affected, if any
File:      /usr/lib/python2.7/dist-packages/MySQLdb/cursors.py
Type:      instancemethod

In [7]: cur.fetchone?
Signature: cur.fetchone()
Docstring:
Fetches a single row from the cursor. None indicates that
no more rows are available.
File:      /usr/lib/python2.7/dist-packages/MySQLdb/cursors.py
Type:      instancemethod

In [8]: 

'''