"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindromic(n):
    nstr = "%d" % int(n)
    if len(nstr) % 2 != 0:
        return False
    nstr1 = nstr[:len(nstr)/2]
    nstr2 = nstr[len(nstr)/2:][::-1]
    if nstr1 == nstr2:
        return True
    return False


maxp = 0
for i in range(1000):
    for j in range(1000):
        if palindromic(i * j):
            if i * j > maxp:
                maxp = i * j

print maxp
