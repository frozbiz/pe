# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

N = 1000000
#import cProfile
#from timeit import Timer
from array import array
from time import time


def step(x):
    if (x & 1):
        return 3 * x + 1
    return x >> 1

class seq:
    def __init__(self):
#        self.valArray = array('i',(0 for i in range(N)))
        self.valArray = list(0 for i in range(N))
        self._fill_spot(1,0)

    def _fill_spot(self,n,count):
        while n <= N and self.valArray[n-1] == 0:
            count += 1
            self.valArray[n-1] = count
            n *= 2

    def sequence(self, x):
        if (x > N):
            return 1 + self.sequence(step(x))
        if (self.valArray[x-1] == 0):
#            self._fill_spot(x,self.sequence(step(x)))
            self.valArray[x-1] = 1 + self.sequence(step(x))
        return self.valArray[x-1]

#Old global way
##
###valArray = list(0 for i in range(N))
##valArray = array('H',(0 for i in range(N)))
##
##valArray[0] = 1
##
##uncachedVals = set()
##nCacheMisses = 0
##
##def sequence(x):
##    global valArray, uncachedVals, nCacheMisses
##    if (x > N):
##        # add code to instrument the misses to figure out whether or not
##        # it makes sense to put them in a dictionary
##        # since it only accounts for 186425 saved calculations
##        # I'm not going to bother
##        if (x in uncachedVals):
##            nCacheMisses += 1
##        else:
##            uncachedVals.add(x)
##        return 1 + sequence(step(x))
##    if (valArray[x-1] == 0):
##        valArray[x-1] = 1 + sequence(step(x))
##    return valArray[x-1]
##
def main():
    nMax = 0
    nStartNum = 0
    cSeq = seq()
    for i in range(1,N+1):
        nHops = cSeq.sequence(i)
        if (nMax < nHops):
            nMax = nHops
            nStartNum = i
    return nStartNum, nMax
start = time()
out = main()
stop = time()
print out, stop - start

def foo():
    print "Foo!"
##
##timer = Timer("main()")
##
##print timer.timeit(1)
##
##cProfile.run("foo()")
##cProfile.run("main()")
##
