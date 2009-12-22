from time import time

from math import sqrt, ceil

def isPandigital(n):
    str_n = str(n)
    num_digs = len(str_n)
    return (set(int(x) for x in str_n) == set(xrange(1,num_digs + 1)))


primes = [2,3,5,7,11,13,17]

def permute_iter(str_n):
    l = len(str_n)
    if l <= 1:
        yield str_n
    else:
        permute_func = permute_iter
        if (3 < l <= 10):
            permute_func = lambda x : permute_iter_test(x,primes[10-l])
        for i in xrange(0,l):
            for perm in permute_func(str_n[:i] + str_n[i+1:]):
                yield str_n[i] + perm

def permute_iter_test(str_n, nTest):
    l = len(str_n)
    if (l < 1):
        yield ""
        return

    permute_func = permute_iter
    if (3 < l <= 10):
        permute_func = lambda x : permute_iter_test(x,primes[10-l])
    for i in xrange(0,l):
        for perm in permute_func(str_n[:i] + str_n[i+1:]):
            str_test = str_n[i] + perm
            if (int(str_test[:3]) % nTest == 0):
                yield str_test

def permute(n):
    return permute_iter(str(n))

start_time = time()

answers = []

for ans in permute(reduce(lambda x,y: str(x) + str(y), xrange(10))):
    answers.append(ans)

end_time = time()

print answers
print sum(map(int,answers))

print "Took", end_time-start_time, "seconds."
