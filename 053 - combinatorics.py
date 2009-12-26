from time import time

def fact(n):
    return reduce(lambda x,y: x * y, xrange(2,n+1), 1)

def c(n, r):
    return fact(n) / (fact(r) * fact(n - r))

start_time = time()
count = 0
for n in xrange(23,101):
    for r in xrange(1,n):
        if (c(n,r) > 1000000):
            count += 1

end_time = time()

print "Took", end_time-start_time, "seconds."
