from time import time

from array import array

start_time = time()

# find a bunch of primes
N = 1000000
sqrt_N = 1000
sieve = set(xrange(2,N))

def isPrime(x):
    return x in sieve

for i in xrange(2,sqrt_N + 1):
    if (not isPrime(i)):
        continue
    sieve.difference_update(xrange(i*2, N, i))

def isTruncatable_right(x):
    if not isPrime(x):
        return False
    if x < 10:
        return True
    return isTruncatable_right(x/10)

def isTruncatable_left(x, nFilter):
    if not isPrime(x):
        return False
    if x < 10:
        return True
    return isTruncatable_left(x % nFilter, nFilter/10)

def numDigits(x):
    return len(str(x))

def isTruncatable(x):
    if x < 10:
        return False
    return isTruncatable_right(x) and isTruncatable_left(x, 10 ** numDigits(x))

truncs = []
for prime in sieve:
    if (isTruncatable(prime)):
        truncs.append(prime)
        if (len(truncs) == 11):
            break

end_time = time()

print truncs
print sum(truncs)
print "Took", end_time-start_time, "seconds."
