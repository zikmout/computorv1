#!/usr/bin/python
import sys
import re
#print 'Number of arguments', len(sys.argv), 'arguments.'
#print 'Argument list:', str(sys.argv)
if (len(sys.argv) != 2):
    print 'Wrong number of arguments. Exit\n'
    sys.exit()
else:
    eq = str(sys.argv[1])
    print '\nthe equation is the following: ' + eq

c0 = 0;
c1 = 0;
c2 = 0;

#(([\-\+]?[0-9]*(\.[0-9]+)?)\ \*)
#full ([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+)
eq1 = re.findall(r'([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+)', eq)
print '\neq1 =>', eq1, '\n'

def get_deg(member):
    l = len(member)
    return member[l - 1]

def push_deg(member_full, deg):
    if deg == 0:
        c0 = c0 + member_full[1]
    elif deg == 1:
        c1 = c1 + member_full[1]
    elif deg == 2:
        c2 = c2 + member_full[1]

eq2 = []
i = 0
while (i <= len(eq1[0])):
    pos = 0
    neg = 0
    deg = 0
    print eq1[i]
    if eq1[i][0][0] == '+':
        pos = 1
        eq2.append('pos')
    elif eq1[i][0][0] == '-':
        neg = 1
        eq2.append('neg')
    else:
        pos = 1
        eq2.append('pos')
    deg = get_deg(eq1[i][0])
    print 'deg => ', deg
    push_deg(eq1[i], deg)



    pos = 0
    neg = 0
    i += 1


print eq2

'''
proper = []
for digit in eq1:
    proper.append(digit[0]);
print '\npropper =>', proper

for eq1 in proper:
    print eq1[0]
'''

print '\nC0 => ', c0
print 'C1 => ', c1
print 'C2 => ', c2
