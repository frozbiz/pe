from time import time
from bisect import bisect
from math import sqrt, ceil

def isPrime(x):
    global sieve
    return x in sieve

def candidate_iter(start, length):
    if length < 1:
        yield ""
        return

    for n in xrange(start,10):
        for tail in candidate_iter(n,length - 1):
            yield str(n) + tail
    
def candidateGenerator(length):
    return candidate_iter(0,length)

def permutation_iter(aVals):
    l = len(aVals)
    if l <= 1:
        yield aVals
    else:
        for i in xrange(l):
            aNewVals = aVals[:i] + aVals[i+1:]
            for aPerm in permutation_iter(aNewVals):
                yield aVals[i:i+1] + aPerm

def unique_permutation_iter(aVals):
    collapsed = [p for p in set(aVals)]
    l = len(collapsed)
    if l <= 1:
        yield aVals
    else:
        for ix in xrange(l):
            c = collapsed[ix]
            i = aVals.index(c)
            aNewVals = aVals[:i] + aVals[i+1:]
            for aPerm in unique_permutation_iter(aNewVals):
                yield aVals[i:i+1] + aPerm

def countUniqueDigs(s):
    digs = {}
    for n in s:
        digs[n] = digs.get(n,0) + 1
    return digs

def isPermutation(x,y):
    return countUniqueDigs(x) == countUniqueDigs(y)

start_time = time()

# find a bunch of primes (up to 4 digits)
N = 10 ** 4
sqrt_N = int(ceil(sqrt(N)))
sieve = set(xrange(2,N))

for i in xrange(2,sqrt_N + 1):
    if (not isPrime(i)):
        continue
    sieve.difference_update(xrange(i*i, N, i))

ans = []

for s in candidateGenerator(4):
    perms = sorted(set(int(p) for p in permutation_iter(s) if isPrime(int(p))))
    for i in xrange(len(perms) - 2):
        val1 = perms[i]
        for j in xrange(i+1, len(perms) - 1):
            val2 = perms[j]
            inc = val2 - val1
            test = val2+inc
            if (test in perms[j+1:]):
                ans.append((val1, val2, test, inc))

end_time = time()

print ans
for sol in ans:
    print "%04d%04d%04d" % sol[:3]

print "Took", end_time-start_time, "seconds."
