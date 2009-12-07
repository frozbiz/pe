# What is the 10001st prime number?

def decAndCheck(a):
    if (a[1] == 1):
        a[1] = a[0]
        return 1

    a[1] -= 1
    return 0
        

aPrimeList = [[2,2]]
nCurrPrime = 2
def getNextPrime():
    global nCurrPrime
    nCurrPrime += 1
    while(sum(map(decAndCheck,aPrimeList))):
        nCurrPrime += 1

    aPrimeList.append([nCurrPrime,nCurrPrime])
    return nCurrPrime

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

for i in range(10000):
    n = getNextPrimeBetter()

print n
