"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

# The number of "North-East" paths through a lattice from (0,0) to (x,y) is
# [https://en.wikipedia.org/wiki/Lattice_path]
# the number of combinations of 'a' objects out of a set of 'a + b' objects,
# i.e.
#   / x + y \   (x + y)!
#   |       | = -------
#   \   x   /    (x!)^2
#
# In the case of a square grid:
#
#   /  2x  \   (2x)!
#   |      | = -------
#   \   x  /    2 * x!

from utils import factorial

GRIDSIZE = 20

routes = factorial(2 * GRIDSIZE) / ((factorial(GRIDSIZE)) ** 2)
print routes
