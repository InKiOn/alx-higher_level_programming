#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif number % 10 > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
else if n < 6 && n != 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
