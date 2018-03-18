"""
Tomas Meszaros

Computation of Pi using various methods.
"""

import math
import random
import datetime

from decimal import Decimal, getcontext

import mpmath


RUN_SECONDS = 1


def _get_end_time():
    return datetime.datetime.now() + datetime.timedelta(seconds=RUN_SECONDS)

def leibniz_formula():
    pi = 0
    subtract = False
    i = 1

    end = _get_end_time()
    while datetime.datetime.now() < end:
        x = 1/i
        i += 2
        if subtract:
            pi -= x
            subtract = False
        else:
            pi += x
            subtract = True
    return pi*4

def archimedes():
    ai = 2*math.sqrt(3)
    bi = 3
    a = 0
    b = 0

    end = _get_end_time()
    while datetime.datetime.now() < end:
        a = (2*ai*bi)/(ai+bi)
        b = math.sqrt(a*bi)
        ai = a
        bi = b
    return (a, b)

def monte_carlo():
    """
    equation of circle
    (x-a)**2 + (y-b)**2 = r**2

    our center is in (a,b)=(0,0) and r=1

    point is inside quart circle if:
    x**2 + y**2 <= 1

    pi = 4 * num of points inside quart circle / num of points
    """
    inside = 0
    points = 0

    end = _get_end_time()
    while datetime.datetime.now() < end:
        xi = random.uniform(0, 1)
        yi = random.uniform(0, 1)
        if xi**2 + yi**2 <= 1:
            inside += 1
        points += 1
    return 4 * inside / points

def gauss_legendre():
    """ TODO: this seems broken, should have better precision
    """
    getcontext().prec = 50

    an = Decimal(1)
    bn = Decimal(1/math.sqrt(2))
    tn = Decimal(1/4)
    pn = Decimal(1)
    pi = Decimal(0)

    end = _get_end_time()
    while datetime.datetime.now() < end:
        an1 = Decimal((an+bn)/2)
        bn1 = Decimal(math.sqrt(an*bn))
        tn1 = Decimal(tn - pn*(an-an1)**2)
        pn1 = Decimal(2*pn)
        pi = Decimal((an1+bn1)**2/(4*tn1))

        an = an1
        bn = bn1
        tn = tn1
        pn = pn1
    return pi

def show_precision(pi, my_pi):
    for i, _ in enumerate(pi):
        if pi[i] != my_pi[i]:
            return my_pi[:i] + "*"
    return my_pi


print("=== running each method for %d seconds ===" % RUN_SECONDS)

mpmath.mp.dps = 50
pi = str(mpmath.mp.pi)
print(" pi (50 digits):", pi)

l = str(format(leibniz_formula(), '.50f'))
print("Leubniz formula:", show_precision(pi, l))

a = str(format(archimedes()[0], '.50f'))
print("     Archimedes:", show_precision(pi, a))

m = str(format(monte_carlo(), '.50f'))
print("   Monter Carlo:", show_precision(pi, m))

g = str(format(gauss_legendre(), '.50f'))
print(" Gauss-Legendre:", show_precision(pi, g))
