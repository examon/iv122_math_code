"""
Tomas Meszaros

Library for linear and affine transformations.

https://en.wikipedia.org/wiki/Linear_map
https://en.wikipedia.org/wiki/Affine_transformation
"""

from svglib import SVGImage
from lingebra import shear, rotate, scale, translate


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

    for _ in range(iterations):
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

    for _ in range(iterations):
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

    for _ in range(iterations):
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
