from time import time

start_time = time()

def digit_cycle(n):
    remainders = {}
    numer = 1
    ix = 0
    while 1:
        remainders[numer] = ix
        numer *= 10
        numer %= n
        ix += 1
        if (numer == 0):
            return 0
        if (numer in remainders):
            return ix - remainders[numer]

nMax = 6
index = 7
for i in xrange(10,1000):
    n = digit_cycle(i)
    if (n > nMax):
        nMax = n
        index = i

end_time = time()

print index, ":", nMax

print "Took", end_time-start_time, "seconds."
