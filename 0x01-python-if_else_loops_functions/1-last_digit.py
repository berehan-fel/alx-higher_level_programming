#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
print("Last digit of {:d} is {:d} and".format(number, last_digit), end=" ")
if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
