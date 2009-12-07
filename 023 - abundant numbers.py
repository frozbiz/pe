# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.

from math import sqrt

def divisorsNoSelf(x):
    rt = sqrt(x)
    limit = int(rt)
    if (rt == limit):
        yield limit
    else:
        limit += 1
    for i in xrange(2,limit):
        if ((x % i) == 0):
            yield i
            yield x/i

def sumOfDivisors(x):
    return sum(divisorsNoSelf(x)) + 1

abundants = [i for i in xrange(12, 28124) if (sumOfDivisors(i) > i)]

answers = []

dictAbundant = dict.fromkeys(abundants,True)

# write a binary search to replace 'in' operator
def isAbundant(x):
    return dictAbundant.get(x,False)

def isSum(x):
    for i in abundants:
        if ((i + i) > x):
            return False
        if isAbundant(x - i):
            return (i, x-i)
    return False

answers = (i for i in xrange(1,28124) if not isSum(i))

print sum(answers)
