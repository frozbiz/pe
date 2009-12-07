# Find the smallest number that is evenly divisible by all of the numbers from 1 to 20?

# Perhaps this is easier done without a program ...

# First, factorize all numbers

# 1: 1
# 2:   2
# 3:     3
# 4:   2   2
# 5:         5
# 6:   2 3
# 7:           7
# 8:   2   2     2
# 9:     3         3
#10:   2     5
#11:                 11
#12:   2 3 2
#13:                    13
#14:   2       7
#15:     3   5
#16:   2   2     2         2
#17:                         17
#18:   2 3         3
#19:                            19
#20:   2   2 5

# Now take the diagonal:
a = [1,2,3,2,5,7,2,3,11,13,2,17,19]

# and multiply it
nProd = 1
for n in a:
    nProd *= n

print nProd
