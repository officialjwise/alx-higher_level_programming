#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print(upper_char, end="")
    print()
