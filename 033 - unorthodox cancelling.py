from time import time

start_time = time()

for i in range(1,10):
    for j in range(1,10):
        if (i == j):
            continue
        for k in range(1,10):
            num = float(i) * 10.0 + j
            denom = float(j) * 10.0 + k
            alt_num = float(i)
            alt_denom = float(k)
            if (num/denom == alt_num/alt_denom):
                print "%d%d/%d%d = %d/%d" % (i,j,j,k,i,k)

end_time = time()

print "Took", end_time-start_time, "seconds."
