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
max_used = most_frequent(count)

def most_frequent(count):
    most_frequent_value = 0
    most_frequent_word = ''
    for word in words:
        if count[word] > most_frequent_value:
            most_frequent_value = count[word]
            most_frequent_word = word
    return most_frequent_word
