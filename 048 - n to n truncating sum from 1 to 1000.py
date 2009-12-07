from time import time

start_time = time()

def pow_trunc(n,m,trunc):
    trunc_mod = 10 ** trunc
    nPow = 1
    for i in xrange(m):
        nPow *= n
        nPow %= trunc_mod
    return nPow

def sum_trunc(aVals,trunc):
    trunc_mod = 10 ** trunc
    return reduce(lambda x,y: (x+y) % trunc_mod, aVals, 0)

trunc = 10
N = 1000
ans = sum_trunc((pow_trunc(i,i,trunc) for i in xrange(1,N+1)), trunc)
end_time = time()

trunc_mod = 10**10
#ans2 = str(sum([i**i for i in xrange(1,N+1)]))[-10:]
ans2 = sum([i**i for i in xrange(1,N+1)]) % trunc_mod
second_time = time()

print ans

print "Took", end_time-start_time, "seconds."
print ans2
print "Took", second_time-end_time, "seconds."
