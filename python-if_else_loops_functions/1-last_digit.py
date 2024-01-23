#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
string = 'Last digit of'

if number >= 0:
    last = number % 10
else:
    last = number % -10

if last > 5:
    print(f'{string} {number} is {last} and is greater than 5')
elif last == 0:
    print(f'{string} {number} is {last} and is 0')
else:
    print(f'{string} {number} is {last} and is less than 6 and not 0')
