#!/usr/bin/python3

output_str = ""
for char_code in range(ord('a'), ord('z') + 1):
    output_str += chr(char_code)
print("{}".format(output_str), end="")
