"""
Tomas Meszaros

Library for linear and affine transformations.

https://en.wikipedia.org/wiki/Linear_map
https://en.wikipedia.org/wiki/Affine_transformation

http://ecademy.agnesscott.edu/~lriddle/ifs/levy/levy.htm
"""

import math
import numpy


def _transform(point, matrix, vector=(0, 0)):
    """ Performs transformations using homogeneous coordinates.

    https://en.wikipedia.org/wiki/Homogeneous_coordinates

    @point: [x, y]
    @matrix: [[a, b], [c, d]]
    @vecor: [e, f]

    (a, b)   (x)   (e)
    (c, d) = (y) + (f)

    (a, b, e)   (x)
    (c, d, f) * (y)
    (0, 0, 1)   (1)
    """
    x, y = point
    a, b = matrix[0]
    c, d = matrix[1]
    e, f = vector

    m = numpy.matrix([[a, b, e],
                      [c, d, f],
                      [0, 0, 1]])
    v = numpy.matrix([[x],
                      [y],
                      [1]])
    x, y, _ = m @ v
    return (x.item(0), y.item(0))

def rotate(point, alpha, vector=[0, 0]):
    """ Rotates @point by @alpha degrees
    """
    alpha = math.radians(alpha)
    m = ((math.cos(alpha), -math.sin(alpha)),
         (math.sin(alpha),  math.cos(alpha)))
    return _transform(point, m, vector)

def translate(point, tx, ty):
    """ Moves @point from its position by @tx and @ty pixels in given direction.
    """
    m = ((1, 0),
         (0, 1))
    v = (tx, ty)
    return _transform(point, m, v)

def scale(point, sx, sy, vector=[0, 0]):
    """ Scales @point by factor of @sx and @sy in given direction.
    """
    m = ((sx, 0),
         (0,  sy))
    return _transform(point, m, vector)

def shear(point, sx):
    """ Shears @point by factor of @sx around x axis.
    """
    m = ((1, sx),
         (0, 1))
    return _transform(point, m)
