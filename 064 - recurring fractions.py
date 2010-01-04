from time import time
from math import sqrt

def isSquare(n):
    sqrt_n = sqrt(n)
    return (sqrt_n == int(sqrt_n))

def count_recurrence(n):
    if isSquare(n):
        return 0
    start = gen_next_term_iter((n, (n, 0)))
    (first, goal) = start
    count = 1
    (out, test) = gen_next_term_iter(goal)
    while (test != goal):
        count += 1
        (out, test) = gen_next_term_iter(test)

    return count

def gen_next_term_iter((top, (n, rem))):
    new_top = (n - rem ** 2) / top
    out = int((sqrt(n) - rem) / new_top)
    new_rem = ((-rem) - out * new_top)
    return (out, (new_top, (n, new_rem)))

start_time = time()

count_odd = 0
for i in xrange(10**4):
    count_odd += count_recurrence(i) & 0x01

end_time = time()

print count_odd

print "Took", end_time-start_time, "seconds."
