from time import time
from math import sqrt
from bisect import bisect

def genPentNum(i):
    return (i * ((3 * i) - 1) / 2)

def quad(a,b,c):
    return ((-b + sqrt(b*b - 4*a*c)) / (2*a), (-b - sqrt(b*b - 4*a*c)) / (2*a))

def half_quad(a,b,c):
    return ((-b + sqrt(b*b - 4*a*c)) / (2*a))

def isPentNum(i):
    global pent_num_set
    if (i > pent_nums[999999]):
        ix = half_quad(3, -1, -2*i)
        return ix == int(ix)
    return i in pent_num_set

start_time = time()

pent_nums = [genPentNum(i) for i in xrange(1,1000001)]
pent_num_set = set(pent_nums)
pent_num_components = {}

candidates = 0
i = 0
##while (candidates == 0):
##    break
##    i += 1
##    pent_num = genPentNum(i)
##    pent_num_components[pent_num] = set()
##    ix_last = bisect(pent_nums, pent_num/2)
##    for n in pent_nums[:ix_last]:
##        x = pent_num - n
##        if isPentNum(x):
##            pent_num_components[pent_num].update((n,x))
##            assert(x >= n)
##            if isPentNum(x - n):
##                ix_x = int(half_quad(3, -1, -2*x))
##                ix_n = int(half_quad(3, -1, -2*n))
##                print "Found candidates %d:%d, %d:%d" % (ix_x, x, ix_n, n)
##                if (candidates == 0 or
##                    ((ix_x - ix_n) < (candidates[1] - candidates[0]))):
##                    candidates = (ix_n, ix_x)
##    pent_nums.append(pent_num)

ans = 0
best = 1150
for i in xrange(1000,1000000):
    num1 = pent_nums[i]
    for j in xrange(i-100, i-best, -1):
        num2 = pent_nums[j]
        if isPentNum(num1 + num2) and isPentNum(num1 - num2):
            ans = (j,i)
            break
    if ans:
        break

print ans, ans[1]-ans[0], pent_nums[ans[1]]-pent_nums[ans[0]]
        
end_time = time()

print "Took", end_time-start_time, "seconds."
