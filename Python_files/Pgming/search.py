#!/usr/bin/python
f = open("file.txt")
for line in f:
    line = line.rstrip()
    if line.startswith('From'):
         print line
