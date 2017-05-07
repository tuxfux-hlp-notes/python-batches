#!/usr/bin/python
# ./add.py 11 12  # 23
# sys.argv
# https://docs.python.org/2/library/argparse.html

import sys

if len(sys.argv) != 3:
	print "syntax:./{} {} {}".format(sys.argv[0],"arg1","arg2")
else:
	result = int(sys.argv[1]) + int(sys.argv[2])
	print result