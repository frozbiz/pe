from time import time
from primes import PrimeSieve


# Only works for odd numbers
def spiral_corner_gen(bYieldTrivial = False):
    num = 1
    if (bYieldTrivial):
        yield (1, (1,0,0,0))
    side = 3
    while 1:
        leap = side - 1
        yield (side, [num + leap * i for i in xrange(1,5)])
        num += leap * 4
        side += 2

start_time = time()
N = 10 ** 5
sieve = PrimeSieve(N)
isPrime = sieve.isPrimeExt
base = 1
count_prime = 0

ans = 0
for (side, corners) in spiral_corner_gen():
    count_prime += sum(isPrime(i) for i in corners)
    base += 4
    if (count_prime * 10) / base == 0:
        ans = side
        break

end_time = time()

print ans
print "Took", end_time-start_time, "seconds."
