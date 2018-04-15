"""
Tomas Meszaros

Library for linear and affine transformations.

https://en.wikipedia.org/wiki/Linear_map
https://en.wikipedia.org/wiki/Affine_transformation
"""

import math
import numpy

from svglib import SVGImage


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

def rotate(point, alpha, origin=[0, 0]):
    """ Rotates @point by @alpha degrees
    """
    alpha = math.radians(alpha)
    m = ((math.cos(alpha), -math.sin(alpha)),
         (math.sin(alpha),  math.cos(alpha)))
    return _transform(point, m, origin)

def translate(point, tx, ty):
    """ Moves @point from its position by @tx and @ty pixels in given direction.
    """
    m = ((1, 0),
         (0, 1))
    v = (tx, ty)
    return _transform(point, m, v)

def scale(point, sx, sy):
    """ Scales @point by factor of @sx and @sy in given direction.
    """
    m = ((sx, 0),
         (0,  sy))
    return _transform(point, m)

def shear(point, sx):
    """ Shears @point by factor of @sx around x axis.
    """
    m = ((1, sx),
         (0, 1))
    return _transform(point, m)



def draw_square_shaered():
    img = SVGImage(1200, 400, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.01)

    o = [[-50, -50, 50, -50],
        [50, -50, 50, 50],
        [50, 50, -50, 50],
        [-50, 50, -50, -50]]
    angle = -10
    sx = 0.9
    sy = 0.9
    sh = 1.3
    tx = 50
    ty = 50
    origin = [0, 0]
    iterations = 40

    for i in range(iterations):
        for i, line in enumerate(o):
            x1, y1, x2, y2 = line
            img.add_line(x1, y1, x2, y2, width=2)
            x1, y1 = shear((x1, y1), sh)
            x2, y2 = shear((x2, y2), sh)
            x1, y1 = rotate((x1, y1), angle, origin)
            x2, y2 = rotate((x2, y2), angle, origin)
            x1, y1 = scale((x1, y1), sx, sy)
            x2, y2 = scale((x2, y2), sx, sy)
            x1, y1 = translate((x1, y1), tx, ty)
            x2, y2 = translate((x2, y2), tx, ty)
            o[i] = [x1, y1, x2, y2]
    img.save("img/square_sheared.svg")
#draw_square_shaered()

def draw_square_blackhole():
    img = SVGImage(1000, 800, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.01)

    o = [[-200, -200, 200, -200],
        [200, -200, 200, 200],
        [200, 200, -200, 200],
        [-200, 200, -200, -200]]
    angle = 10
    sx = 1.1
    sy = 0.8
    origin = [0, 0]
    iterations = 60

    for i in range(iterations):
        for i, line in enumerate(o):
            x1, y1, x2, y2 = line
            img.add_line(x1, y1, x2, y2, width=2)
            x1, y1 = rotate((x1, y1), angle, origin)
            x2, y2 = rotate((x2, y2), angle, origin)
            x1, y1 = scale((x1, y1), sx, sy)
            x2, y2 = scale((x2, y2), sx, sy)
            o[i] = [x1, y1, x2, y2]
    img.save("img/square_blackhole.svg")
#draw_square_blackhole()

def draw_square_snail():
    img = SVGImage(1000, 800, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.01)

    o = [[0, 0, 10, 0],
        [10, 0, 10, 10],
        [10, 10, 0, 10],
        [0, 10, 0, 0]]
    angle = 25
    sx = 1.1
    sy = 1.1
    tx = 1
    ty = 2
    origin = [0, 0]
    iterations = 37

    for i in range(iterations):
        for i, line in enumerate(o):
            x1, y1, x2, y2 = line
            img.add_line(x1, y1, x2, y2, width=2)
            x1, y1 = rotate((x1, y1), angle, origin)
            x2, y2 = rotate((x2, y2), angle, origin)
            x1, y1 = scale((x1, y1), sx, sy)
            x2, y2 = scale((x2, y2), sx, sy)
            x1, y1 = translate((x1, y1), tx, ty)
            x2, y2 = translate((x2, y2), tx, ty)
            o[i] = [x1, y1, x2, y2]
    img.save("img/square_snail.svg")
#draw_square_snail()
