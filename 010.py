"""
Project Euler Problem #10
==========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils import isprime

#MAX = 2000000
MAX = 10

sum = 0
for i in xrange(2, MAX):
    if isprime(i):
        sum += i
print sum
