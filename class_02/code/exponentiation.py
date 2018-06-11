#!/usr/bin/env python3

"""
Tomas Meszaros

Modulo exponentiation, comparing various methods.

For theory, see:
- https://en.wikipedia.org/wiki/Exponentiation_by_squaring
"""

import math
import sys

import timer


@timer.timeit("     python_pow:")
def python_pow(n, e, m):
    return pow(n, e, m)


@timer.timeit("      naive_pow:")
def naive_pow(n, e, m):
    r = 1
    for _ in range(e):
        r *= n
    return r % m

@timer.timeit("     binary_exp:")
def binary_exp(n, e, m):
    """ Not as fast as it could be.
    Could remove function calls and list operatios
    """

    def pow2(n, e):
        """ utility function
        pow if e is power of 2
        """
        if e == 1:
            return n
        assert(e % 2 == 0)

        i = 1
        prev = n
        r = n

        # O(log(e))
        while i < e:
            r = prev*prev
            prev = r
            i *= 2
        return r

    # e as binary string
    bin_e = str(bin(e))[2:]

    # get powers of e
    e_powers = []

    # O(log(|bin_e|)) iterations
    for i, v in enumerate(reversed(bin_e)):
        if v == '1':
            # O(log(|bin_e|))
            r = 1
            for _ in range(i):
                r *= 2
            e_powers.append(r)

    # put it together
    x = 1
    # O(log(|bin_e|)) iterations
    for i in e_powers:
        # O(log(i))
        x *= pow2(n, i) % m

    return x % m


@timer.timeit("  binary_exp_v2:")
#@profile # uncomment for line_profiler
def binary_exp_v2(n, e, m):
    """ Faster binary exp version
    """
    # remove 0b and first bin digit
    bin_e = str(bin(e))[3:]
    r = n
    # O(log(|bin_e|))
    for digit in bin_e:
        if digit == '1':
            r = r*r
            r = r*n
        else:
            r = r*r
        r = r % m
    return r % m



## Experiments

# x = n**e mod m
n = 5
m = 19

powers = [4, 5, 6, 7, 8, 10**2, 10**4, 10**5, 10**6, 10**7]
for power in powers:
    e = 10**power
    print("exponent zeroes:", power)

    a = python_pow(n, e, m)

    if e < 100000000:
        b = binary_exp(n, e, m)
        assert(a == b)

    c = binary_exp_v2(n, e, m)
    assert(a == c)

    if e < 10000000:
        d = naive_pow(n, e, m)
        assert(a == d)
    print()
