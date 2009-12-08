from time import time

def find_best_candidate(x,rem):
    x_sq = x ** 2
    lo = x + 1
    hi = (rem+1)/2
    inc = (hi - lo) / 2

    while inc:
        y = lo + inc
        z = rem - y
        test = cmp(x_sq + y**2, z**2)
        if (test < 0):
            lo = y + 1
        elif (test > 0):
            hi = y
        else:
            lo = y
            break
        inc = (hi - lo) / 2
    return (x,lo,rem-lo)

def permute(x):
    for i in xrange(1,x-1):
        for j in xrange(i+1,(x-i+1)/2):
            k = x - i - j
            if (i**2 + j**2 > k**2):
                break
            yield (i,j,k)

def permute_smarter(x):
    for i in xrange(1, x/3):
        yield find_best_candidate(i, x-i)

def isTriangle(tSides):
    return ((tSides[0] ** 2 + tSides[1] ** 2) == (tSides[2] ** 2))

start_time = time()

N = 1000
best = []
best_ix = -1
for i in xrange(6, N+1):
    triangles = []
    for candidate in permute_smarter(i):
        if (isTriangle(candidate)):
            triangles.append(candidate)
    if len(triangles) > len(best):
        best = triangles
        best_ix = i

end_time = time()

print best_ix, ":", best

print "Took", end_time-start_time, "seconds."
