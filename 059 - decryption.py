from time import time

# This told me that there were characters other than lowercase letters in the
# output, which led me to believe that the cyphertext wasn't cleaned, which means
# There are probably spaces
def getCandidates(arr):
    for code_seq in arr:
        trial = range(ord('a'), ord('z') + 1)
        poss = []
        for c in trial:
            for (code,freq) in code_seq:
                ans = c ^ code
                if not (ord('a') <= ans <= ord('z')):
                    break
            else:
                poss.append(c)
        yield poss

def sort_key((x,y)):
    return (y,x)

def decipher(arr, key):
    i = 0
    for code in arr:
        yield (code ^ key[i])
        i += 1
        i %= len(key)

start_time = time()

infile = open("cipher1.txt")
codes = eval("["+infile.readline()+"]")

# split the message into N (three) key groups, one corresponding to each
# character of the cipher text and put them in dictionaries with their frequency
# then sort them back out into lists by freq
codes_deinterleaved = []
freq_dict = []
code_freq = []
for i in xrange(3):
    codes_deinterleaved.append(codes[i::3])
    freq_dict.append({})
    for code in codes_deinterleaved[i]:
        if code in freq_dict[i]:
            freq_dict[i][code] += 1
        else:
            freq_dict[i][code] = 1
    code_freq.append(sorted(freq_dict[i].items(), key=sort_key, reverse=True))

# since there are spaces in the output, this just got a whole lot easier:
ans = [i for i in decipher(codes, [cf[0][0] ^ ord(' ') for cf in code_freq])]

ans_str = reduce(lambda x,y: x + y, (chr(i) for i in ans))

end_time = time()

print ans_str
print sum(ans)
print "Took", end_time-start_time, "seconds."
