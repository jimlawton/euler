"""
Project Euler Problem #9
=========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def ispythagorean(a, b, c):
    if (a ** 2 + b ** 2) == (c ** 2): 
        return True
    return False


SUM = 1000

stop = False
for i in range(1, SUM + 1):
    for j in range(i, SUM + 1):
        for k in range(j, SUM + 1):
            if i + j + k == SUM:
                if ispythagorean(i, j, k):
                    stop = True
                    break
        if stop:
            break
    if stop:
        break

print i * j * k

