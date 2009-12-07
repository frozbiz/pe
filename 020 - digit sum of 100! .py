# What is the sum of the digits of 100!?

def digitsum(x):
    return sum(int(c) for c in str(x))

def fact(x):
    return reduce((lambda x,y:x*y),range(2,x+1), 1)

print digitsum(fact(100))
