from time import time

start_time = time()

results = set()
for a in xrange(2,101):
    for b in xrange(2,101):
        results.add(a**b)

end_time = time()

print len(results)

print "Took", end_time-start_time, "seconds."
