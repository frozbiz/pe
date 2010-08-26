from time import time
from bisect import bisect
from math import sqrt, ceil

def rev_digit_gen(n):
    if n == 0:
        yield 0
    while n:
        (n, c) = divmod(n,10)
        yield c

def countUniqueDigs(s):
    digs = {}
    for n in s:
        digs[n] = digs.get(n,0) + 1
    return digs

def countUniqueDigsInt(n):
    digs = {}
    for i in rev_digit_gen(n):
        digs[i] = digs.get(i,0) + 1
    return digs

def isPermutation(x,y):
    return countUniqueDigs(x) == countUniqueDigs(y)

def isListPermutation(s, lst):
    test = countUniqueDigs(s)
    for i in lst:
        if (test != countUniqueDigs(i)):
            return False
    return True

start_time = time()

i = 1
ans = 0
while 1:
    str_i = str(i)
    if (isListPermutation(str_i, (str(i * n) for n in xrange(2,7)))):
        ans = i
        break
    i += 1

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
