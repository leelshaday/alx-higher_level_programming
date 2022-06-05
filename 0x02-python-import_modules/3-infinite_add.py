#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 0
    for i in range(len(argv) - 1):
        n += int(argv[i + 1])
    print("{:d}".format(n))
