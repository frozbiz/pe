from time import time
from primes import PrimeSieve

start_time = time()
N = 10 ** 6
sieve = PrimeSieve(N)
isPrime = sieve.isPrime

longest = 0
ans = 2

length = len(sieve.primes)
for start in xrange(length):
    first_test = start + 1 + longest
    tot = sum(sieve.primes[start:first_test])
    for i in xrange(first_test, length):
        tot += sieve.primes[i]
        if (tot > N):
            break
        if (isPrime(tot)):
            longest = i - start
            ans = tot

end_time = time()

print "Took", end_time-start_time, "seconds."
