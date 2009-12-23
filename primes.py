from math import sqrt, floor

class PrimeSieve:
    def __init__(self, N):
        self.N = N
        self.sqrt_N = int(floor(sqrt(N)))
        self.__sieve = set(xrange(2,N))

        for i in xrange(2, self.sqrt_N + 1):
            if (not self.isPrime(i)):
                continue
            self.__sieve.difference_update(xrange(i*i, N, i))

    def isPrime(self, x):
        assert(x <= self.N)
        return x in self.__sieve

    def __getattr__(self, attr):
        if (attr == "primes"):
            # since this is only called if the attribute is not found, we can
            # just set this and return it.
            self.primes = sorted(self.__sieve)
            return self.primes
        raise AttributeError("'PrimeSieve' object has no attribute '%s'" % (attr))

