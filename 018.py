"""
Project Euler Problem 18
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                    75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""

from utils import pairwise, print_triangle


triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
#print_triangle(triangle)
#print
dimension = len(triangle[-1])
dim_weights = 2 * dimension - 2

#triangle = [
#    [75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
#    [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67],
#    [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33],
#    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
#]

rev_triangle = triangle[::-1]
print_triangle(rev_triangle)
print

weights = []
for index, row in enumerate(rev_triangle[:-1]):
    print index, row
    row_weights = []
    prev_row = []
    for rindex, element in enumerate(row):
        if rindex == 0:
            row_weights.append(element + rev_triangle[index + 1][0])
        elif rindex == len(row) - 1:
            row_weights.append(element + rev_triangle[index + 1][-1])
        else:
            row_weights.extend([element + rev_triangle[index + 1][rindex - 1],
                                element + rev_triangle[index + 1][rindex]])
    weights.append(row_weights)

print_triangle(weights)

#rev_sums = []
#for index, row in enumerate(rev_triangle[:-1]):
#    print "index=%d row=%s" % (index, row)
#    pairs = pairwise(row)
#    print "pairs:", pairs
#    parent = rev_triangle[index+1]
#    print "parent:", parent
#    if index == 0:
#        new_row = [max(x) for x in pairs]
#    else:
#        row_sums = [x + y for x, y in zip(parent, rev_sums[index-1])]
#        print "row_sums:", row_sums
#        new_row = [max(x) for x in pairwise(row_sums)]
#    print "new_row:", new_row
#    rev_sums.append(new_row)
#    #print
#    #print_triangle(rev_sums)
#    #print

#print
#print_triangle(rev_sums)
#print

#rev_sums = rev_sums[:-1]
#sums = rev_sums
#sums.reverse()

#print
#print_triangle(sums)
#print

#path = [triangle[0][0]]
#for row in triangle[1:]:
#    path.append(row[row.index(max(row))])
#print path
#print sum(path)
