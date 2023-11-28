#!/usr/bin/python3

def islower(c):
    """Check if character c is lowercase."""
    # Let's check if the ASCII value of c is in the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')


# Testing the function
print(islower('a'))  # Returns True
print(islower('A'))  # Returns False
print(islower('1'))  # Returns False
