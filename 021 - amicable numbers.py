# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def divisorsNoSelf(x):
    limit = int(sqrt(x))
    for i in xrange(2,limit + 1):
        if ((x % i) == 0):
            yield i
            yield x/i

def sumOfDivisors(x):
    return sum(divisorsNoSelf(x)) + 1

N = 10000
sums = [0 for i in xrange(N)]

answers = []
for i in xrange(N):
    if (sums[i] == 0):
        n = sumOfDivisors(i)
        sums[i] = n
    else:
        n = sums[i]

    if (n < N and n > i):
        if (sums[n] == 0):
            m = sumOfDivisors(n)
            sums[n] = m
        else:
            m = sums[n]

        if (m == i):
            answers.append(m)
            answers.append(n)

print sum(answers)
