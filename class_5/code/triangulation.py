"""
Tomas Meszaros

Draws triangulation of random points.
"""

import random
import math

from svglib import SVGImage


IMG_WIDTH = 1000
IMG_HEIGHT = 1000
POINTS_NUM = 5
POINTS_RADIUS = 4
LINE_WIDTH = 2
ANIMATION_SPEED = 0.05
BUFFER = 300

def get_random_number(a=0, b=100):
    return random.choice(range(a, b))

def intersect(line1, line2, t=5):
    """ Figure out if the intersect point is on the both lines

    TODO: needs some buffer, to handle intersection in vertecies
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
    line1 = tuple(map(lambda x: x+0.000001, line1))
    line2 = tuple(map(lambda x: x-0.000001, line2))

    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    #print("1:", line1)
    #print("2:", line2)
    px1 = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))
    px2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    #if px2 == 0: px2 = 0.000001
    px = px1 / px2
    py1 = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))
    py2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    #if py2 == 0: py2 = 0.000001
    py = py1 / py2
    return (px, py)

def draw_triangulation():
    img = SVGImage(IMG_WIDTH, IMG_HEIGHT, center_origin=False, show_borders_and_origin=True, animate=False, animation_speed=ANIMATION_SPEED)

    def generate_points(number):
        points = []
        for i in range(number):
            x = get_random_number(BUFFER, IMG_WIDTH-BUFFER)
            y = get_random_number(BUFFER, IMG_HEIGHT-BUFFER)
            points.append((x, y))
        return points

    """
    a = (482.000001, 307.000001, 489.000001, 500.000001)
    b = (489.000001, 500.000001, 482.000001, 307.000001)
    img.add_line(*a)
    img.add_line(*b)
    """

    points = generate_points(POINTS_NUM)
    print(points)
    lines = []

    def get_lines():
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                if point1+point2 in lines:
                    continue
                if point2+point1 in lines:
                    continue
                line = point1 + point2

                isect = False
                for i in lines:
                    if intersect(line, i):
                        isect = True
                        img.add_line(*line, color="blue", width=5)
                        img.add_line(*i, color="red", width=5)
                if not isect:
                    lines.append(line)
    get_lines()
    #get_lines()
    #get_lines()

    ## draw points
    for point in points:
        img.add_circle(point[0], point[1], POINTS_RADIUS, color="black", fill="red")

    ## draw lines
    for line in lines:
        img.add_line(*line, width=LINE_WIDTH)

    img.save("img/triangulation_animate.svg")
draw_triangulation()
