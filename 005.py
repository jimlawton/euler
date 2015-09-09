"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

MAX = 20

i = 1
while True:
    alldiv = True
    for j in range(2, MAX+1):
        if i % j != 0:
            alldiv = False
            break
    if alldiv:
        break
    i += 1
print i
