"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

import sys


END = 1000

words = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred",
    1000: "one thousand"
}

def num2words(n):
    numstr = str(n)
    if n in words:
        return words[n]
    else:
        if len(numstr) == 2:
            tens = int(numstr[0])
            units = int(numstr[1])
            return words[tens * 10] + '-' + words[units]
        elif len(numstr) == 3:
            hundreds = int(numstr[0])
            remainder = n - hundreds * 100
            if remainder == 0:
                return words[hundreds] + " hundred"
            else:
                return words[hundreds] + " hundred and " + num2words(remainder)
        else:
            sys.exit(">1000 not supported yet!")


numlist = []
for i in range(1, END + 1):
    numlist.append(num2words(i))

filtered = ' '.join(numlist)
filtered = filtered.replace('-', '')
filtered = filtered.replace(' ', '')
print len(filtered)
