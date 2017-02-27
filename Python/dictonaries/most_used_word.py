#!/usr/bin/python
count = dict()
line = raw_input("")
words = line.split()
for word in words:
    count[word] = count.get(word,0)+1
print count
listkey = list(count)
print listkey
listvalue = count.values()
print listvalue
mostfrequentvalue = 0
mostfrequentword = ''
for word in words:
    if count[word] > mostfrequentvalue:
        mostfrequentvalue = count[word]
        mostfrequentword = word
print mostfrequentword
