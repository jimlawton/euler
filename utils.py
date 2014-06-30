import operator


def fibonacci(n):
    """Return the nth term of the Fibonacci sequence."""
    if n < 2:
         return n
    return fibonacci(n - 2) + fibonacci(n - 1)


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

