#!usr/bin/python
demolist = ["Hello", 23, "Ram", 2324, "tia"]
for index in demolist:
    print (index)
for item in range(10):
    print item

list = [1 , 21, 2 , 23, 31, 45, 45]
list.sort()
i = 0
for index in list:
    cur = index
    if (cur == index + i):
        print "Duplicate exists"
    i = i + 1

for i in xrange(1,10000):
    print i
