#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number[-1:]
if number < 0:
    x = - 1 * (-number % 10)
else:
    x = number % 10

if x > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif x == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif x < 6 and x != 0:
    print(f"Last digit of {number} is {last}" end=" ")
    print("and is less than 6 and not 0")