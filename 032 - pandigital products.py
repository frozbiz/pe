from time import time

start_time = time()

def permutation_iter(aVals):
    l = len(aVals)
    if l <= 1:
        yield aVals
    else:
        for i in xrange(l):
            aNewVals = aVals[:i] + aVals[i+1:]
            for aPerm in permutation_iter(aNewVals):
                yield aVals[i:i+1] + aPerm

def allPanDigitalProds(s):
    for times in xrange(1,len(s)-1):
        for equals in xrange(times + 1, len(s)):
            multiplier = long(s[:times])
            multiplicand = long(s[times:equals])
            result = long(s[equals:])
            if (multiplier * multiplicand == result):
                yield result


prods = set()
for perm in permutation_iter("123456789"):
    for prod in allPanDigitalProds(perm):
        prods.add(prod)

end_time = time()

print sum(prods)

print "Took", end_time-start_time, "seconds."
