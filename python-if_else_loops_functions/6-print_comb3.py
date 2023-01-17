#!/usr/bin/python3
for d in range(0, 10):
    for u in range(d + 1, 10):
        print("{}{}".format(d, u), end="\n" if d == 8 and u == 9 else ", ")
