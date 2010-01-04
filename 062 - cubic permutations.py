from time import time

def countUniqueDigs(n):
    digs = [0 for i in xrange(10)]
    while n:
        (n,dig) = divmod(n, 10)
        digs[dig] += 1
    
    return tuple(digs)

start_time = time()

cubes = []

cud_dict = {}
N = 10000
TARGET = 5
NUM, COUNT = range(2)
ans = 0
for cube in (n ** 3 for n in xrange(345, N)):
    cud = countUniqueDigs(cube)
    if cud in cud_dict:
        cud_dict[cud][COUNT] += 1
        if (cud_dict[cud][COUNT] >= TARGET):
            ans = cud_dict[cud][NUM]
            break
    else:
        cud_dict[cud] = [cube, 1]

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
