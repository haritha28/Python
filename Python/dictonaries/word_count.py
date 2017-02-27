#!/usr/bin/python
count=dict()
print "Enter the sentence:"
line=raw_input("")

Words=line.split()
print "Words:",Words

for Word in Words:
    count[Word]=count.get(Word,0)+1
print 'Counts', count
