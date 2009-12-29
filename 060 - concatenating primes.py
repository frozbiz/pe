from time import time
from primes import PrimeSieve
from bisect import bisect

def concatenateAndTest(primes):
    for i in xrange(len(primes)-1):
        str_i = str(primes[i])
        for j in xrange(i+1, len(primes)):
            str_j = str(primes[j])
##            print str_i + str_j
##            print str_j + str_i
            if not (isPrime(int(str_i + str_j)) and isPrime(int(str_j + str_i))):
                return False
    return True

def ds(n):
    dsum = 0
    while n:
        dsum += n % 10
        n /= 10

    return dsum

def selector_iter(sCurrent, sWorking, nTest, count):
    if (len(sWorking) < count):
        return

    if (len(sCurrent) == count):
        yield sCurrent
        return

    for n in sorted(sWorking):
        if n <= nTest:
            continue
        if (sCurrent <= compat[n]):
            for ans in selector_iter(sCurrent.union([n]), sWorking & compat[n].union([n]), n, count):
                yield ans

start_time = time()
N = 10 ** 4
sieve = PrimeSieve(N)
isPrime = sieve.isPrimeExt
primes = sieve.primes

ans = 0
prime_list = range(5)
l = len(primes)
# Create a dictionary for each prime that lists the 'compatible' primes

compat = {}
ix = bisect(primes, 10 ** 4)
primes1 = [3] + [prime for prime in primes[:ix] if ds(prime) % 3 == 1]
primes2 = [3] + [prime for prime in primes[:ix] if ds(prime) % 3 == 2]

l = len(primes1)

for i in xrange(l-1):
    pi = primes1[i]
    str_pi = str(pi)
    for j in xrange(i+1, l):
        pj = primes1[j]
        str_pj = str(pj)
        if isPrime(int(str_pi + str_pj)) and isPrime(int(str_pj + str_pi)):
            if (pi in compat):
                compat[pi].add(pj)
            else:
                compat[pi] = set([pj])

            if (pj in compat):
                compat[pj].add(pi)
            else:
                compat[pj] = set([pi])

l = len(primes2)
for i in xrange(l-1):
    pi = primes2[i]
    for j in xrange(i+1, l):
        pj = primes2[j]
        if concatenateAndTest((pi,pj)):
            if (pi in compat):
                compat[pi].add(pj)
            else:
                compat[pi] = set([pj])
            
            if (pj in compat):
                compat[pj].add(pi)
            else:
                compat[pj] = set([pi])

ans_sum = None
all_ans = []
for i in sorted(compat):
    sWorking = compat[i].union([i])
    sCurrent = set([i])
    for ans in selector_iter(sCurrent.union([i]), sWorking, i, 5):
        if (not ans_sum or ans_sum > sum(ans)):
            ans_sum = sum(ans)
        # print ans
        all_ans.append(ans)
                                 
end_time = time()

print ans_sum

print "Took", end_time-start_time, "seconds."
