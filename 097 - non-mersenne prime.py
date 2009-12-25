from time import time

start_time = time()
ans = 28433
N = 10 ** 10
for ignore in xrange(78304):
    ans = (ans << 100)
    if (ans > N):
        ans %= N

ans = (ans << 57)
ans %= N

end_time = time()

print ans + 1
print "Took", end_time-start_time, "seconds."
