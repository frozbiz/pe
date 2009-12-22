from time import time

from math import sqrt, ceil

def isPandigital(n):
    str_n = str(n)
    num_digs = len(str_n)
    return (set(int(x) for x in str_n) == set(xrange(1,num_digs + 1)))

def permute_iter(str_n):
    l = len(str_n)
    if l <= 1:
        yield str_n
    else:
        for i in xrange(0,l):
            for perm in permute_iter(str_n[:i] + str_n[i+1:]):
                yield str_n[i] + perm

def permute(n):
    return permute_iter(str(n))

start_time = time()

# find a bunch of primes (up to 7 digita
N = 10 ** 7
sqrt_N = int(ceil(sqrt(N)))
sieve = set(xrange(2,N))

def isPrime(x):
    return x in sieve

for i in xrange(2,sqrt_N + 1):
    if (not isPrime(i)):
        continue
    sieve.difference_update(xrange(i*i, N, i))

ans = 0
for test in permute(7654321):
    if isPrime(int(test)):
        ans = test
        break

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
