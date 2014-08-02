"""
Project Euler Problem #10
==========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils import isprime

MAX = 2000000

def sieve(n):
    """Return all numbers less than or equal to 'n' that are prime."""
    allnums = range(3, n + 1, 2)
    for mindex, number in enumerate(xrange(3, n + 1, 2)):
        if allnums[mindex] == 0:
            continue
        # Set all multiples to 0.
        for index in xrange(mindex+number, (n - 3) / 2 + 1, number):
            allnums[index] = 0
    return [2] + filter(lambda n: n != 0, allnums)

print sum(sieve(MAX))
