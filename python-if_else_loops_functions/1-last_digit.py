#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
der = number % 10
if der > 5:
    print(f"Last digit of {number} is {der} and is greater than 5")
elif der < 5 and der != 0:
    if der > 0:
    print(f"Last digit of {number} is {der} and is less than 6 and not 0")
    else
    print(f"Last digit of -{number} is {der} and is less than 6 and not 0")
elif der == 0:
    print(f"Last digit of {number} is {der} and is 0")
