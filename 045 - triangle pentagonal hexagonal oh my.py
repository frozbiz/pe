from time import time
from math import sqrt

def quad(a,b,c):
    return ((-b + sqrt(b*b - 4*a*c)) / (2*a), (-b - sqrt(b*b - 4*a*c)) / (2*a))

def half_quad(a,b,c):
    return ((-b + sqrt(b*b - 4*a*c)) / (2*a))

def isPentNum(i):
    ix = half_quad(3, -1, -2*i)
    return ix == int(ix)

def isHexNum(i):
    ix = half_quad(2, -1, -i)
    return ix == int(ix)

start_time = time()

start_ix = 285
start_val = 40755

ix = start_ix
val = start_val

while 1:
    ix += 2
    val += ix + ix - 1
    if (isPentNum(val)):
        break

end_time = time()

print ix, val

print "Took", end_time-start_time, "seconds."
