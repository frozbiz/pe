# Find the sum of all the primes below two million.

nCurrPrime = 2

def isPrime(x):
    # slight speed-up, although starting at 2 and going by one works fine as well
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    i = 3
    while (i*i <= x):
        if (x % i == 0):
            return False
        i += 2
    return True

def getNextPrimeBetter():
    global nCurrPrime
    nCurrPrime += 1
    while (not isPrime(nCurrPrime)):
        nCurrPrime += 1

    return nCurrPrime

n = nCurrPrime
nSum = 0
while n < 2000000:
    nSum += n
    n = getNextPrimeBetter()

print n
print nSum
