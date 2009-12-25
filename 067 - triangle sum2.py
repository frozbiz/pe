from time import time

start_time = time()
triFile = open("triangle.txt")
triList = [l for l in triFile if len(l.strip())]

triList = [map(int,row.split()) for row in triList]

triList.reverse()

BASE = len (triList)

for i in xrange(1,BASE):
    for j in xrange(len(triList[i])):
        triList[i][j] += max((triList[i-1][j], triList[i-1][j+1]))

end_time = time()

print triList[-1][0]

print "Took", end_time-start_time, "seconds."
