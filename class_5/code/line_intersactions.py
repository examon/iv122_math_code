"""
Tomas Meszaros

Draws random line segments of the same length.
Draws intersections of the line segments.
"""

import random
import math

from svglib import SVGImage


IMG_WIDTH = 1000
IMG_HEIGHT = 1000
LINE_COUNT = 50
LINE_LENGTH = 800
LINE_WIDTH = 4
INTERSECT_RADIUS = 5
ANIMATION_SPEED = 0.01

def get_random_number(a=0, b=100):
    return random.choice(range(a, b))

def get_random_angle():
    return random.choice(range(360))

def get_random_line(length):
    x1 = get_random_number(0, IMG_WIDTH)
    y1 = get_random_number(0, IMG_HEIGHT)
    angle = get_random_angle()
    x2 = x1 + math.cos(math.radians(angle)) * length
    y2 = y1 + math.sin(math.radians(angle)) * length
    return (x1, y1, x2, y2)

def intersect(line1, line2):
    """ Figure out if the intersect point is on the both lines
    """
    px, py = get_intersect(line1, line2)
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    l1 = False
    l2 = False

    # first line
    if x1 <= x2:
        if y1 <= y2:
            if px >= x1 and px <= x2 and py >= y1 and py <= y2:
                l1 = True
        else:
            if px >= x1 and px <= x2 and py <= y1 and py >= y2:
                l1 = True
    else:
        if y1 <= y2:
            if px <= x1 and px >= x2 and py >= y1 and py <= y2:
                l1 = True
        else:
            if px <= x1 and px >= x2 and py <= y1 and py >= y2:
                l1 = True

    # second line
    if x3 <= x4:
        if y3 <= y4:
            if px >= x3 and px <= x4 and py >= y3 and py <= y4:
                l2 = True
        else:
            if px >= x4 and px <= x4 and py <= y3 and py >= y4:
                l2 = True
    else:
        if y3 <= y4:
            if px <= x3 and px >= x4 and py >= y3 and py <= y4:
                l2 = True
        else:
            if px <= x3 and px >= x4 and py <= y3 and py >= y4:
                l2 = True

    return (l1 and l2)

def get_intersect(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    ## Possible division by zero
    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    return (px, py)

def draw_lines_and_intersects():
    img = SVGImage(IMG_WIDTH, IMG_HEIGHT, center_origin=False, show_borders_and_origin=False, animate=False, animation_speed=ANIMATION_SPEED)
    lines = []

    ## draw lines
    for i in range(LINE_COUNT):
        line = get_random_line(LINE_LENGTH)
        lines.append(line)
        img.add_line(*line, width=LINE_WIDTH)

    ## draw intersections
    for line in lines:
        for i in lines:
            if line == i:
                continue
            if intersect(line, i):
                px, py = get_intersect(line, i)
                img.add_circle(px, py, INTERSECT_RADIUS, color="black", fill="red")

    img.save("img/line_intersections.svg")
draw_lines_and_intersects()
