from time import time
from math import sqrt

def dictsFromSet(s):
    beg = {}
    end = set()
    for n in s:
        beg.setdefault(n / 100, []).append(n)
        end.add(n % 100)
    return (beg, end)

def candidate_find_iter(cand, which, remainder, beg):
    end = cand % 100
    l = len(remainder)
    if l == 0:
        if end == beg:
            yield [(cand,which)]

    for i in xrange(l):
        poly = remainder[i]
        curr_set = poly[ID]
        new_rem = remainder[:i]+remainder[i+1:]
        for next_cand in poly[BEG].get(end,[]):
            for ans in candidate_find_iter(next_cand, curr_set, new_rem, beg):
                yield [(cand,which)] + ans

start_time = time()
tri_set = set()
tri_beg = {}
tri_end = set()
hex_set = set()
hex_beg = {}
hex_end = set()
for i in xrange(10**4):
    n = i * (i + 1) / 2
    if (n < 1000):
        continue
    if (n > 9999):
        break
    end = n % 100
    # we can't use anything that ends in 0X
    if (end < 10):
        continue
    beg = n / 100
    tri_set.add(n)
    tri_beg.setdefault(beg, []).append(n)
    tri_end.add(end)
    if (i & 0x01):
        hex_set.add(n)
        hex_beg.setdefault(beg, []).append(n)
        hex_end.add(end)

sq_set = set()
sq_beg = {}
sq_end = set()
for i in xrange(10**1, 10**2):
    n = i ** 2
    if (n < 1000):
        continue
    end = n % 100
    # we can't use anything that ends in 0X
    if (end < 10):
        continue
    beg = n / 100
    sq_set.add(n)
    sq_beg.setdefault(beg, []).append(n)
    sq_end.add(end)

pent_set = set()
pent_beg = {}
pent_end = set()
for i in xrange(10, 10**3):
    n = i * (3 * i - 1) / 2
    if (n < 1000):
        continue
    if (n > 9999):
        break
    end = n % 100
    # we can't use anything that ends in 0X
    if (end < 10):
        continue
    beg = n / 100
    pent_set.add(n)
    pent_beg.setdefault(beg, []).append(n)
    pent_end.add(end)

sept_set = set()
sept_beg = {}
sept_end = set()
for i in xrange(10, 10**3):
    n = i * (5 * i - 3) / 2
    if (n < 1000):
        continue
    if (n > 9999):
        break
    end = n % 100
    # we can't use anything that ends in 0X
    if (end < 10):
        continue
    beg = n / 100
    sept_set.add(n)
    sept_beg.setdefault(beg, []).append(n)
    sept_end.add(end)

oct_set = set()
oct_beg = {}
oct_end = set()
for i in xrange(10, 10**3):
    n = i * (3 * i - 2)
    if (n < 1000):
        continue
    if (n > 9999):
        break
    end = n % 100
    # we can't use anything that ends in 0X
    if (end < 10):
        continue
    beg = n / 100
    oct_set.add(n)
    oct_beg.setdefault(beg, []).append(n)
    oct_end.add(end)

SET, BEG, END, ID = range(4)

circ_buffer = [(tri_set, tri_beg, tri_end, 3),
               (sq_set, sq_beg, sq_end, 4),
               (pent_set, pent_beg, pent_end, 5),
               (hex_set, hex_beg, hex_end, 6),
               (sept_set, sept_beg, sept_end, 7),
               (oct_set, oct_beg, oct_end, 8)]
l = len(circ_buffer)
### as long as we're making progress removing things, keep going ... where's my do
### while??
##bChanged = True
##while bChanged:
##    bChanged = False
##    for i in xrange(l):
##        # Remove all the numbers that don't start with an end from any other set
##        all_ends = reduce(lambda x,y: x|y,
##                          (circ_buffer[n][END] for n in (range(i) +
##                                                         range(i+1,l))))
##        rejs = set(circ_buffer[i][BEG]) - all_ends
##        if not rejs:
##            continue
##        print "%d:" % i, rejs
##        for rej in rejs:
##            for n in circ_buffer[i][BEG][rej]:
##                circ_buffer[i][SET].discard(n)
##
##        # Rebuild the dictionaries
##        (beg, end) = dictsFromSet(circ_buffer[i][SET])
##        circ_buffer[i][BEG].clear()
##        circ_buffer[i][BEG].update(beg)
##        if (circ_buffer[i][END] != end):
##            if ((circ_buffer[i][END] - end) - all_ends):
##                print "Mark"
##                bChanged = True
##            circ_buffer[i][END].clear()
##            circ_buffer[i][END].update(end)
##
all_ans = []
for candidate in circ_buffer[0][SET]:
    beg = candidate / 100
    for ans in candidate_find_iter(candidate, 3, circ_buffer[1:], beg):
        all_ans.append(ans)

end_time = time()

print all_ans
print "Took", end_time-start_time, "seconds."
