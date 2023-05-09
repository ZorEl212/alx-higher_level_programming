#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dig = str(number)[-1]
if (number < 0):
    l_dig = int(l_dig) * -1

if (int(l_dig) < 6 and int(l_dig) != 0):
    print(f"Last digit of {number:d} is {l_dig} and is less than 6 and not 0")

elif (int(l_dig) > 5):
    print(f"Last digit of {number:d} is {l_dig} and is greater than 5")

elif (int(l_dig) == 0):
    print(f"Last digit of {number:d} is {l_dig} and is 0")
