"""
Project Euler Problem #2
=========================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

from utils import fibonacci


sum = 0
i = 2
while True:
    term = fibonacci(i)
    if term % 2 == 0:
        if term > 4000000:
            break
        sum += term
    i += 1
print sum
