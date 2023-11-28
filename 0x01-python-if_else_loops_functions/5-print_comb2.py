#!/usr/bin/python3
for number in range(100):
    separator = ", " if number < 99 else "\n"
    print("{:02d}".format(number), end=separator)
