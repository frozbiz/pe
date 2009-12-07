from time import time

start_time = time()
fib = [1,2]
nWhich = 1
limit = 10**999
term = 3
while (fib[nWhich] < limit):
    term += 1
    fib[not nWhich] += fib[nWhich]
    nWhich ^= 1

end_time = time()

print term, ":", fib[nWhich]

print "Took", end_time-start_time, "seconds."
