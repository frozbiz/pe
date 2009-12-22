from time import time

def eval_word(word):
    sub = ord('A') - 1
    return reduce(lambda tot,c: tot + ord(c) - sub, word.upper(), 0)

start_time = time()

word_file = open("words.txt")
words = eval("[%s]" % word_file.readline())
word_vals = map(eval_word,words)
longest_word_val = max(word_vals)

# now generate the triangle numbers
t_nums = set()
num = 1
inc = 2
while (num <= longest_word_val):
    t_nums.add(num)
    num += inc
    inc += 1

def isTNum(n):
    return n in t_nums

ans = reduce(lambda tot,n: tot + isTNum(n), word_vals, 0)

end_time = time()

print ans

print "Took", end_time-start_time, "seconds."
