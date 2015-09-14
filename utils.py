import operator


def fibonacci(n):
    """Return the nth term of the Fibonacci sequence."""
    if n < 2:
         return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def simple_factors(n):
    """Return the factors of a positive integer."""
    return [x for x in range(1, n+1) if n % x == 0]

def factors(n):
    """Return the factors of a positive integer."""
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def primefactors(n):
    """Return the prime factors of a positive integer."""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors


def palindromic(n):
    """Check if an integer is palindromic."""
    nstr = "%d" % int(n)
    if len(nstr) % 2 != 0:
        return False
    nstr1 = nstr[:len(nstr)/2]
    nstr2 = nstr[len(nstr)/2:][::-1]
    if nstr1 == nstr2:
        return True
    return False


def sumsquares(n):
    """Return the sum of the squares of the integers in the range 1..n."""
    result = 0
    for i in range(1, n+1):
        result += i ** 2
    return result


def isprime(n):
    """Check if an integer is prime."""
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


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


def product(factors):
    """Return the product of the supplied list of integers."""
    return reduce(operator.mul, factors, 1)


def ispythagorean(a, b, c):
    """Check if a triplet of integers is Pythagorean, i.e.
    consists of three natural numbers, a < b < c, for
    which a^2 + b^2 = c^2."""
    if (a ** 2 + b ** 2) == (c ** 2):
        return True
    return False


def factorial(n):
    """Return the factorial product of the supplied integer."""
    seq = range(1, n + 1)
    return product(seq)


def pairwise(iterable):
    pairs = []
    for index, item in enumerate(iterable):
        pairs.append(iterable[index:index+2])
        if index == len(iterable) - 2:
            break
    return pairs


def max_digits(iterable):
    """Return the maximum number of digits in any element of a list."""
    digits = 0
    for elem in iterable:
        if len("%d" % elem) > digits:
            digits = len("%d" % elem)
    return digits


def print_triangle(triangle):
    """Pretty-prints a triangle of integers."""
    maxrowlen = 0
    for row in triangle:
        if len(row) > maxrowlen:
            maxrowlen = len(row)
    maxdigits = max([max_digits(row) for row in triangle])
    maxlen = maxdigits * maxrowlen
    for row in triangle:
        rowstrlist = ["{num:0{width}}".format(num=x, width=maxdigits) for x in row]
        pad = maxlen - len(row) * maxdigits
        print (' ') * pad, '  '.join(rowstrlist)

