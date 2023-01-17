#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    der = number % 10
else:
    der = number % -10
if der > 5:
    print(f"Last digit of {number} is {der} and is greater than 5")
elif der < 6 and der != 0:
        print(f"Last digit of {number} is {der} and is less than 6 and not 0")
elif der == 0:
    print(f"Last digit of {number} is {der} and is 0")
