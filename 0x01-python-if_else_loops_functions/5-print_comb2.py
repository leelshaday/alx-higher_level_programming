#!/usr/bin/python3
for i in range(100):
    print("{:0>2}".format(i), end=", " if i < 99 else "\n")
