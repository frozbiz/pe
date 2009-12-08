from time import time

target = frozenset(chr(i + ord('0')) for i in xrange(1,10))
best = "000000000"
best_mult = -1
best_n = 0
def numDigits(x):
    return len(str(x))

def hasDups(aVals):
    return (len (aVals) > len(frozenset(aVals)))

def test(x):
    global best, best_mult, best_n
    start = 0
    # wish I had a do-while
    val = x # * 1
    str_val = str(val)
    end = start + len(str_val)
    n = 2
    while ((not hasDups(str_val)) and
           (best[start:end] <= str_val) and
           (len(str_val) < 9)):
        str_val += str(x * n)
        n += 1

    if (len(str_val) == 9 and
        frozenset(str_val) == target and
        best < str_val):
        best = str_val
        best_mult = x
        best_n = n - 1

start_time = time()

# we can't get fewer than 9 characters out of str(10000 * 1) + str(10000 * 2)
STOP = 10000
for x in xrange(1,STOP):
    test(x)

end_time = time()

print best
print best_mult
print best_n

print "Took", end_time-start_time, "seconds."
