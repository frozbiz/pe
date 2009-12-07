from time import time

start_time = time()

# Only works for odd numbers
def add_spiral_corners(n):
    assert(n & 1)
    num = 1
    tot = 1
    for i in xrange(3,n+1, 2):
        leap = i-1
        for j in xrange(4):
            num += leap
            tot += num
    return tot

ans = add_spiral_corners(1001)

end_time = time()

print ans
print "Took", end_time-start_time, "seconds."
