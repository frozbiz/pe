# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# observations:
# - The words "one" through "nine" are written out 9 times in every 100 numbers
#   and 1 in every 10 numbers over 100 (180 out of 1000)
# - The words "ten" through "nineteen" happen once every 100 numbers
# - The word "and" happens 99 times out of a 100 above 100 (891 out of 1000)
# - The word "hundred" happens 900 times out of every 1000
# - The word "ten" happens once out of every 100 numbers
# - The words "twenty" through "ninety" happen 10 times in every 100 numbers
# - The words "one" and "thousand" happen once (more) in this sequence

listOneNine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
wordsOneNine = "".join(listOneNine)
listTenTwelve = ["ten", "eleven", "twelve"]
listTeenPrefix = ["thir", "four", "fif", "six", "seven", "eigh", "nine"]
listTenNineteen = listTenTwelve + [pfx + "teen" for pfx in listTeenPrefix]
wordsTenNineteen = "".join(listTenNineteen)
listTyPrefix = ["twen"] + listTeenPrefix
listTyPrefix[2] = "for"
listTwentyNinety = [pfx + "ty" for pfx in listTyPrefix]
wordsTwentyNinety = "".join(listTwentyNinety)

lenOneNine = len(wordsOneNine)
lenTenNineteen = len(wordsTenNineteen)
lenHundred = len("hundred")
lenTwentyNinety = len(wordsTwentyNinety)
lenAnd = len("and")
lenThousand = len("one" "thousand")
lenTen = len("ten")

answer =    180 * lenOneNine + 10 * lenTenNineteen + 891 * lenAnd + 900 * lenHundred
answer +=   100 * lenTwentyNinety + lenThousand

print answer

def numberAsWord(x):
    if not (0 < x <= 1000):
        return "bad input"
    if x >= 1000:
        return "one thousand"
    if x >= 100:
        hund = x/100
        tens = x%100
        if tens:
            tail = " hundred and " + numberAsWord(tens)
        else:
            tail = " hundred"
        return listOneNine[hund - 1] + tail
    if x >= 20:
        tens = x/10
        ones = x % 10
        tail = ""
        if (ones):
            tail = " " + numberAsWord(ones)
        return listTwentyNinety[tens - 2] + tail
    if x >= 10:
        return listTenNineteen[x - 10]
    if 0 < x < 10:
        return listOneNine[x-1]
    return "not yet"

def stripSpaces(x):
    return "".join(x.split())


print sum(len(stripSpaces(numberAsWord(x))) for x in xrange(1,1001))
    
