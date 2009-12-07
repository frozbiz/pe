# Find the difference between the sum of the squares and the square of the sum of the first one hundred natural numbers.

def square(x): return (x*x)

# First lets get some arrays to handle the numbers

aSumSquares = range(1,101)
aSquareSum = aSumSquares

nSquareSum = square(sum(aSquareSum))

nSumSquares = sum(map(square,aSumSquares))

print nSquareSum - nSumSquares
