# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def isSquare(x):
    i = 2
    while i*i < x:
        i += 1
        
    if i*i == x:
        return i
    
    return 0

def FindPythagoreanTriplet():
    for a in range(1,333):
        b = a
        nSum = a + b + b
        while (nSum < 1000):
            c_sq = a*a + b*b
            c = isSquare(c_sq)
            if (c):
                print "Found %d^2 + %d^2 = %d^2" % (a,b,c)
                nSum = a + b + c
                if (nSum == 1000):
                    print "Eureka!"
                    print (a*b*c)
                    return (a,b,c)
            else:
                c = sqrt(c_sq)
                nSum = a + b + c
            b += 1

FindPythagoreanTriplet()


                
