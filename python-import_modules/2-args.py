#!/usr/bin/python3

import sys

j = 0
k = 0
for i in sys.argv[1:]:
    j += 1

if j == 1:
    print("1 argument:")
elif j == 0:
    print("0 argument.")
else:
    print("{} arguments:".format(j))

for i in sys.argv[1:]:
    k += 1
    print("{}: {}".format(k, i))
