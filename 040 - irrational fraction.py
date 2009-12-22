from time import time

def num_generator():
    n = 1
    while (1):
        strNum = str(n)
        for dig in strNum:
            yield int(dig)
        n+=1

start_time = time()

res = 1
i = 1
i_check = 10
for dig in num_generator():
    if (i == i_check):
        res *= dig
        i_check *= 10
        if (i_check > 1000000):
            break
    i += 1

end_time = time()

print res

print "Took", end_time-start_time, "seconds."
