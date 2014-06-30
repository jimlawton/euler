"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""

from utils import isprime


INDEX = 10001
nprimes = 0
i = 1
while True:
    if isprime(i):
        nprimes += 1
    if nprimes == INDEX + 1:
        break
    i += 1

print i

