from time import time
from bisect import bisect
from math import sqrt, ceil

def countUniqueDigs(s):
    digs = {}
    for n in s:
        digs[n] = digs.get(n,0) + 1
    return digs

def isPermutation(x,y):
    return countUniqueDigs(x) == countUniqueDigs(y)

def isListPermutation(lst):
    try:
        it = iter(lst)
        it.__init__()
        test = countUniqueDigs(it.next())
        while 1:
            if (test != countUniqueDigs(it.next())):
                return False
    except StopIteration:
        return True

start_time = time()

i = 1
ans = 0
while 1:
    if (isListPermutation(str(i * n) for n in xrange(1,7))):
        ans = i
        break
    i += 1

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
