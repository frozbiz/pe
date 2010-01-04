from time import time

ds = lambda x: sum(int(n) for n in (str(x)))

expand = lambda x,y,n: x * n + y

def seq_gen():
    yield 2
    x = 2
    while 1:
        yield 1
        yield x
        yield 1
        x += 2

def rev_seq_gen(N):
    (revs, over) = divmod(N - 1, 3)
    for rev in xrange(revs + 1, 0, -1):
        for i in xrange(over,0,-1):
            if i & 0x01:
                yield 1
            else:
                yield rev * 2
        over = 3
    yield 2
    
start_time = time()

N = 100

top = 1
bottom = 0
for n in rev_seq_gen(N):
    top, bottom = expand(top, bottom, n), top
    #print top, "/", bottom

end_time = time()

print "Got", top

print "Took", end_time-start_time, "seconds."
