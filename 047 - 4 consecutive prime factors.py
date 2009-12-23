from time import time
from bisect import bisect
from math import sqrt, ceil

def isPrime(x):
    global sieve
    return x in sieve

def countFactors(x):
    global primes
    factors = set()
    for prime in primes:
        if isPrime(x) or x <= 1:
            break
        while (x % prime) == 0:
            x /= prime
            factors.add(prime)
    if (x > 1):
        factors.add(x)
    return len(factors)
    

start_time = time()

# find a bunch of primes (up to 6 digits)
N = 10 ** 6
sqrt_N = int(ceil(sqrt(N)))
sieve = set(xrange(2,N))

for i in xrange(2,sqrt_N + 1):
    if (not isPrime(i)):
        continue
    sieve.difference_update(xrange(i*i, N, i))

primes = sorted(sieve)
ans = 0

i = 10
count = 0
while count < 4:
    if (countFactors(i) == 4):
        count += 1
    else:
        count = 0
    i += 1

ans = i - 4


end_time = time()

print ans, i

print "Took", end_time-start_time, "seconds."
