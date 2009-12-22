from time import time
from bisect import bisect
from math import sqrt, ceil

def isPrime(x):
    global sieve
    return x in sieve

def isSquare(x):
    rt = sqrt(x)
    return rt == int(rt)

def isAnomoly(x):
    global primes
    ix = 0
    while(primes[ix] < x):
        if isSquare((x - primes[ix])/2):
            return False
        ix += 1

    return True

start_time = time()

# find a bunch of primes (up to 6 digits)
N = 10 ** 6
sqrt_N = int(ceil(sqrt(N)))
sieve = set(xrange(2,N))

for i in xrange(2,sqrt_N + 1):
    if (not isPrime(i)):
        continue
    sieve.difference_update(xrange(i*i, N, i))

# create a list of odd composite numbers
odd_composites = (i for i in xrange(3,N,2) if not isPrime(i))
primes = sorted(sieve)
ans = 0
for comp in odd_composites:
    if isAnomoly(comp):
        ans = comp
        break

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
