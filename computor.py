#!/usr/bin/python
import sys
print 'Number of arguments', len(sys.argv), 'arguments.'
print 'Argument list:', str(sys.argv)
if (len(sys.argv) != 2):
    print 'Wrong number of arguments. Exit'
    sys.exit()
else:
    print 'Ok, lets start de solver'


