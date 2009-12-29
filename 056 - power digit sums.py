from time import time

def ds(n):
    dsum = 0
    while n:
        dsum += n % 10
        n /= 10

    return dsum

start_time = time()

max_sum = 0
for i in xrange(2,100):
    for j in xrange(2,100):
        s = ds(i ** j)
        if s > max_sum:
            max_sum = s


end_time = time()

print "Got", max_sum

print "Took", end_time-start_time, "seconds."
