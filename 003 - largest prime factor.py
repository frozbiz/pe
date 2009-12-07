# Find the largest prime factor of 317584931803

nTarget = 317584931803
nCurrent = nTarget

i = 2
nLargestFactor = 1

while (i < nCurrent and i*i < nTarget):
    while (nCurrent > i and nCurrent % i == 0):
        nCurrent /= i
        nLargestFactor = i
        print i

    i += 1 # Make this increment better

if (nLargestFactor < nCurrent):
    nLargestFactor = nCurrent
    print nCurrent

print nLargestFactor
