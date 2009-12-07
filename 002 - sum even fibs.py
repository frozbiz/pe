# Sum the even Fibonacci numbers less than 1000000

fib = [1,2]
nOnOdd = 0
nSum = 0
nWhich = 1
while (fib[nWhich] <= 1000000):
    if (not nOnOdd):
        nSum += fib[nWhich]
        nOnOdd += 1
    elif (nOnOdd == 2):
        nOnOdd = 0
    else:
        nOnOdd += 1

    fib[not nWhich] += fib[nWhich]
    nWhich ^= 1

print nSum
