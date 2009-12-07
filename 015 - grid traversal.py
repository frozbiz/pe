# How many routes are there through a 20x20 grid?

#brain dead way

def numRoutes(x,y):
    if (x == 0 or y == 0):
        return 1
    return (numRoutes(x-1,y) + numRoutes(x,y-1))

# Okay, so that doesn't scale, but perhaps we can smarten it up ...
# first, realize that reflection allows us to claim that
# numRoutes(1,2) == numRoutes(2,1)

def numRoutes(x,y):
    if (x == 0 or y == 0):
        return 1
    if (x == y):
        return (2 * numRoutes(x-1,y))
    return (numRoutes(x-1,y) + numRoutes(x,y-1))

# now use dynamic programming to do it even better
N = 20
#nodeVals = [[0 for y in xrange(x)] for x in xrange(1,N+1)]

def numRoutes(x,y):
    nodeVals = []
    if (y > x):
        x,y = y,x

    for currX in xrange(x):
        col = []
        nodeVals.append(col)
        right = 1
        for currY in xrange(currX):
            left = nodeVals[currX-1][currY]
            right += left
            col.append(right)
        col.append(2 * right)

    return nodeVals[x][y]


