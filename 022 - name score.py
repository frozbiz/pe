# What is the total of all the name scores in the file?

namefile = open("names.txt")
a = [name.split(",") for name in namefile]
namefile.close()

a = reduce((lambda x,y:x+y),a)
a = map((lambda x: x[1:-1]),a)
a.sort()

def wordSum(word):
    return sum((ord(c)-ord('A')+1) for c in word)

def genScores(a):
    for i in xrange(len(a)):
        yield (i+1) * wordSum(a[i])

print sum(genScores(a))
