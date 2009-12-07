# Sum the natural numbers below 1000 that are multiples of 3 or 5

nThree = 3
nFive = 5
i = 0
nSum = 0
while (i < 1000):
    nSum += i
    if (nThree < nFive):
        i = nThree
        nThree += 3
    elif (nThree > nFive):
        i = nFive
        nFive += 5
    else:
        i = nThree
        nThree += 3
        nFive += 5
#    print i

print nSum
