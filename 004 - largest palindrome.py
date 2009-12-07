# Find the largest palindrome made from the product of two 3-digit numbers.
from time import time

def isPalindrome(nNum):
    s = str(nNum)
    nLen = len(s)
    for i in xrange(nLen/2):
        if (s[i] != s[nLen - 1 - i]):
            return False

    return True

start_time = time()

nLeft = 999
nRight = nLeft

nLargestPalindrome = 0

nProduct = nLeft * nRight

while (nProduct > nLargestPalindrome):
    # should be a do-while if they had such a structure :)
    while (nProduct > nLargestPalindrome and nRight >= 100):
        if (isPalindrome(nProduct)):
            nLargestPalindrome = nProduct
            break
        else:
            nRight -= 1
            nProduct = nRight * nLeft

    nLeft -= 1
    nRight = nLeft
    nProduct = nRight * nLeft

end_time = time()

print nLargestPalindrome
print "Took", end_time-start_time, "seconds."
