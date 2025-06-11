#!/usr/bin/python3
"""print the alphabet in lowercase except for q and e"""

for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    print("{}".format(chr(letter)), end="")
