from time import time
from primes import PrimeSieve

def countUniqueDigs(s):
    digs = {}
    for n in s:
        digs[n] = digs.get(n,0) + 1
    return digs

# it's a candiate for testing if it has more than 1 '0', '1', or '2' that we can rotate
def isCandidate(n):
    digs = countUniqueDigs(str(n))
    return (digs.get("0",0) > 1) or (digs.get("1",0) > 1) or (digs.get("2",0) > 1)

def permute_sub(str_n, n, c):
    inc = 0
    for ch in str_n:
        inc *= 10
        if ch == c:
            inc += 1

    for i in xrange(int(c),10):
        yield n
        n += inc

def permute(n):
    str_n = str(n)
    digs = countUniqueDigs(str_n)
    for c in "012":
        if (digs.get(c,0) > 1):
            yield permute_sub(str_n, n, c)

start_time = time()
N = 10 ** 6
sieve = PrimeSieve(N)
isPrime = sieve.isPrime

primes = (p for p in sieve.primes if isCandidate(p))
TARGET = 8
ans = []
for prime in primes:
    for perms in permute(prime):
        ans = [n for n in perms if isPrime(n)]
        if len(ans) >= TARGET:
            break
    if len(ans) >= TARGET:
        break

end_time = time()

print "Took", end_time-start_time, "seconds."
