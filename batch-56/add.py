#!/usr/bin/python
# positional parameters/positional arguments
import sys
if len(sys.argv) != 3:
    print """
            syntax: {} <arg1> <arg2>
            please use the above syntax """.format(sys.argv[0])
else:
    print int(sys.argv[1]) + int(sys.argv[2])
