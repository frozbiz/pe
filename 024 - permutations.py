from time import time

start_time = time()

def swap(aVals, i,j):
    tmp = aVals[i]
    aVals[i] = aVals[j]
    aVals[j] = tmp

def permutation_iter(aVals):
    l = len(aVals)
    if l <= 1:
        yield aVals
    else:
        for i in xrange(l):
            aNewVals = aVals[:i] + aVals[i+1:]
            for aPerm in permutation_iter(aNewVals):
                yield aVals[i:i+1] + aPerm

# this implementation of fact is valid for all positive integers
def fact(n):
    return reduce(lambda a,b: a*b, xrange(2,n+1), 1)

def specific_perm_iter(aVals, ixPerm, nCombs):
    assert(ixPerm < nCombs)
    if (ixPerm == 0):
        return aVals
    l = len(aVals)
    nCombs /= l
    ix = ixPerm / nCombs
    ixPerm %= nCombs
    item = aVals[ix]
    del aVals[ix]
    return [item] + specific_perm_iter(aVals, ixPerm, nCombs)

def specific_permutation(aVals, n):
    # the nth permutation can be found at the ith index where i = n-1
    ixPerm = n - 1
    nCombs = fact(len(aVals))
    if (ixPerm < 0 or ixPerm >= nCombs):
        raise ValueError("Permutation out of range")
    return specific_perm_iter(list(aVals), ixPerm, nCombs)

ans = specific_permutation("0123456789",1000000)

end_time = time()

# the slow way
count = 0
for perm in permutation_iter("0123456789"):
    count += 1
    if count == 1000000:
        ans2 = perm
        break
    
slow_time = time()

print "".join(ans)
print ans2

print "Fast took", end_time-start_time, "seconds."
print "Slow took", slow_time-end_time, "seconds."
