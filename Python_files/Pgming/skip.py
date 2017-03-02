#!/usr/bin/python
f = open("file.txt")
for line in f:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print line
