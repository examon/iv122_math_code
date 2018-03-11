"""
Tomas Meszaros

Draws images using relative (turtle) or absolute approach.

TODO:
-
"""

import math

from myturtle import Turtle
from svglib import SVGImage

## Pentagram: Relative, using turtle

t = Turtle(center_origin=True, show_borders_and_origin=True, animate=True, animation_speed=0.5)
def draw_polygon_pentagram_relative(t, line_width=1):
    n = 5
    polygon_side = 200

    center_angle = 360 / n
    triangle_angle = (180 - center_angle) / 2
    turn_angle = 180 - triangle_angle - 90

    # move to starting position
    x = math.cos(math.radians(turn_angle)) * polygon_side
    t.penup()
    t.forward(x)
    t.left(180 - turn_angle)
    t.pendown()

    # draw polygon
    for _ in range(n):
        t.forward(polygon_side, width=line_width)
        t.left(2 *turn_angle)

    # move to position for pentagram
    t.reset_angle()
    t.left(180)

    # draw pentagram
    pentagram_polygon_side = 2*x
    for _ in range(n):
        t.forward(pentagram_polygon_side, width=line_width)
        t.left(180 - center_angle/2)
    t.reset()

draw_polygon_pentagram_relative(t, 5)
t.save("img/pentagram_relative.svg")


## Pentagram: Absolute
img = SVGImage(center_origin=True, show_borders_and_origin=True, animate=True, animation_speed=0.5)

def draw_polygon_pentagram_absolute(img, line_width=1):
    n = 5
    center_to_side = 200
    center_angle = 360 / n
    offset_angle = 90 - center_angle

    x = 0
    y = 0
    points = [(x,y)]
    ## Draw polygon
    for i in range(1, n+2):
        nx = math.cos(math.radians(i*center_angle + offset_angle)) * center_to_side
        ny = math.sin(math.radians(i*center_angle + offset_angle)) * center_to_side
        points.append((nx, ny))
        if i != 1:
            img.add_line(x, y, nx, ny, width=line_width)
        x = nx
        y = ny
    # remove center and last duplicate
    points = points[1:-1]

    ## draw pentagram
    last = 0
    for _ in range(n):
        point_1 = points[last]
        point_2 = points[(last+2) % n]
        last = (last+2) % n
        img.add_line(point_1[0], point_1[1], point_2[0], point_2[1], width=line_width)

draw_polygon_pentagram_absolute(img, 5)
img.save("img/pentagram_absolute.svg")
