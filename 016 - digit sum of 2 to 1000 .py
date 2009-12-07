# What is the sum of the digits of the number 2^1000?

def digitsum(x):
    return sum(int(c) for c in str(x))

print digitsum(2**1000)
