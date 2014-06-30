"""
Project Euler Problem #6
=========================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sumsq(n):
    result = 0
    for i in range(1, n+1):
        result += i ** 2
    return result

MAX = 100
ssq = sumsq(MAX)
sqs = sum([i for i in range(1, MAX+1)]) ** 2
diff = sqs - ssq
print diff
