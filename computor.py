#!/usr/bin/python
import sys
import re

def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: #threshold
            return guess
        last_guess= guess

if (len(sys.argv) != 2):
    print 'Wrong number of arguments. Exit\n'
    sys.exit()
elif sys.argv[1] == '':
    print 'Please verify your input. Exit\n'
    sys.exit()
else:
    eq = str(sys.argv[1])
    #print '\nthe equation is the following: ' + eq

c0 = 0;
c1 = 0;
c2 = 0;

eqtest = re.findall(r'([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+.\d+)', eq)

#print 'EQTEST ------->', eqtest
if eqtest:
    print 'Please verify your input: It seems you power have coma). Exit\n'
    sys.exit()


def check_power(eq1):
    for key in eq1:
        #print 'KEY-------->',  float(key[0][len(key[0]) - 1])

        if float(key[0][len(key[0]) - 1]) > 2:
            print 'The polynomial degree is stricly greater than 2, I can\'t solve.'
            sys.exit()

def check_consistency(eq1, av):
    i = 0
    for letter in av:
        if letter == '^':
            i += 1
    #print 'eq1 LEN == ', len(eq1)
    if len(eq1) != i:
        print 'Please verify your input(2). Exit\n'
        sys.exit()
eq1 = re.findall(r'([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+)', eq)

#print '\neq1 =>', eq1, '\n'
check_power(eq1)
check_consistency(eq1, sys.argv[1])


if not eq1:
    print 'Please verify your input. Exit\n'
    sys.exit();

#print '\neq1 =>', eq1, '\n'

def search_equal(eq):
    i = 0
    while (i < len(eq)):
        if eq[i] == '=':
            return i
        i+=1
    return 0

def get_deg(member):
    l = len(member)
    return member[l - 1]

def push_deg(member_full, deg, pos, neg):
    global c0
    global c1
    global c2
    re = member_full[1].strip(' ')
    #print 'After strip ... ->' + re
    re = float(re)
    #print 'After re ... ->' , re
    #print 'POS ->>>', pos
    #print 'NEG ->>>', neg
    if deg == '0':
        if pos == 1:
            c0 = c0 + re
        else:
            c0 = c0 - re
    elif deg == '1':
        if pos:
            c1 = c1 + re
        else:
            c1 = c1 - re
    elif deg == '2':
        if pos:
            c2 = c2 + re
        else:
            c2 = c2 - re

def print_reduced(c0, c1, c2):
    if c0 > 0:
        print '+', c0, ' * X^0',
    elif c0 < 0:
        print ' ', c0, ' * X^0',
    if c1 > 0:
        print '+', c1, ' * X^1',
    elif c1 < 0:
        print ' ', c1, ' * X^1',
    if c2 > 0:
        print '+', c2, ' * X^2',
    elif c2 < 0:
        print ' ', c2, ' * X^2',
    elif c0 == 0 and c1 == 0 and c2 == 0:
        print c0, ' * X^0',
    print ' = 0'

def print_polynomial_degree(c0, c1, c2):
    degree = 0
    if c2 != 0:
        degree = 2
    elif c1 != 0:
        degree = 1
    elif c0 != 0:
        degree = 0
    else:
        degree = 3
    return degree

def get_delta(c0, c1, c2):
    #delta = b^2 - 4 * ac = c1^2 - 4 * c2 * c0
    #print c0
    #print c1
    #print c2
    return c1**2 - (4 * c2 * c0)

equal = search_equal(eq)

eq2 = []
equal_pos = 0
i = 0
while (i < len(eq1)):
    pos = 0
    neg = 0
    deg = 0
    equal_pos += len(eq1[i][0])
    #print 'LEN =', len(eq1[i][0])
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
    #print 'deg = ', deg
    #print 'i =', i
    #print 'equal =', equal
    #print 'equal_pos = ', equal_pos
    if equal_pos < equal:
        push_deg(eq1[i], deg, pos, neg)
    else:
        if pos == 1:
            pos = 0
            neg = 1
        else:
            neg = 0
            pos = 1
        push_deg(eq1[i], deg, pos, neg)

    pos = 0
    neg = 0
    i += 1

#print '\n', eq2

print 'Reduced form:',
print_reduced(c0, c1, c2)
if print_polynomial_degree(c0, c1, c2) != 3:
    print 'Polynomial degree: ', print_polynomial_degree(c0, c1, c2)
delta = get_delta(c0, c1, c2)
#print 'Delta =>', delta
if delta > 0 and print_polynomial_degree(c0, c1, c2) == 2:
    print 'Discriminant is strictly positive, the two solutions are: '
    print (-c1 + (sqrt(delta)))/(2 * c2)
    print (-c1 - (sqrt(delta)))/(2 * c2)
elif delta == 0 and print_polynomial_degree(c0, c1, c2) == 2:
    print 'Discriminant is equal to zero, the double real solution is: '
    print -c1/(2*c2)
elif delta < 0 and print_polynomial_degree(c0, c1, c2) == 2:
    print 'There are two complex solutions which are:'
    print -c1, ' + i *', sqrt(-delta), '/',(2 * c2)
    print -c1, ' - i *', sqrt(-delta), '/',(2 * c2)
elif print_polynomial_degree(c0, c1, c2) == 1:
    print 'The solution is: '
    print -c0/c1
elif print_polynomial_degree(c0, c1, c2) == 0 and c0 != 0:
    print 'There is no solution to this equation'
elif print_polynomial_degree(c0, c1, c2) == 3 or (print_polynomial_degree(c0, c1, c2) == 0 and c0 == 0):
    print 'There an infinite number of solutions to this equation'

#print '\nC0 => ', c0
#print 'C1 => ', c1
#print 'C2 => ', c2
