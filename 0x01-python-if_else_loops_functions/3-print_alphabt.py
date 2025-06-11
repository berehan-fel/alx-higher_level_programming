#!/usr/bin/python3
# Author - Berehan Felegehewot

"""print alphabet except for q and e """

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
