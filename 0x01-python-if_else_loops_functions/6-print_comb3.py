#!/usr/bin/python3
"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical."""

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        separator = ", "

        if first_digit < 8 or (first_digit == 8 and second_digit < 9):
            print(f"{first_digit}{second_digit}", end=separator)
        else:
            print(f"{first_digit}{second_digit}")
