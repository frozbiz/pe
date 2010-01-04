from time import time

ans = 0
start_time = time()

count = 0
for n in xrange(1,22):
    limit = (10 ** (n-1))
    for i in xrange(9,0,-1):
        if (i ** n) < limit:
            break
        count += 1

ans = count

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
