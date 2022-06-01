#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number > 0 else int(repr(number)[-1]) * -1

print("Last digit of {} is {} ".format(number, lastDigit), end="")

if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
