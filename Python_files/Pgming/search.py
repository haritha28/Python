#!/usr/bin/python
f = open("file.txt")
for line in f:
     if line startswith('From'):
         print line
