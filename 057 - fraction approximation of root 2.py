from time import time

num_digs = lambda x: len(str(x))

expand_top = lambda x,y: x + y
    
start_time = time()

top = 2
bottom = 1

count = 0
for i in xrange(1000):
    final_top = expand_top(top,bottom)
    final_bottom = top
    #print final_top, "/", final_bottom
    count += (num_digs(final_top) > num_digs(final_bottom))
    (top, bottom) = (top * 2 + bottom, top)

end_time = time()

print "Got", count

print "Took", end_time-start_time, "seconds."
