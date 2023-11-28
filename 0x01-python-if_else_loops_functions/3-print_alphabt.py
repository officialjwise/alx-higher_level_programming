#!/usr/bin/python3
for chars in range(97, 123):
    if chars != 113 and chars != 101:
        print("{:c}".format(chars), end="")
