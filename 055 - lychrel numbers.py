from time import time

def num_rev(n):
    assert(isinstance(n, (int,long)))
    n_rev = 0
    while (n):
        n_rev *= 10
        n_rev += n % 10
        n /= 10
    return n_rev

def rev(n):
    assert(isinstance(n, (int,long)))
    return int(str(n)[::-1])

def isPalindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def isLychrel(n):
    # The problem states that if it doesn't happen in 50 iterations,
    # it's not going to
    for i in range(50):
        n += rev(n)
        if isPalindrome(n):
            return False

    return True

    
start_time = time()

count = 0
for i in xrange(5,10000):
    count += isLychrel(i)

end_time = time()

print "Got", count
print "Took", end_time-start_time, "seconds."
