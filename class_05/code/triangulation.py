"""
Tomas Meszaros

Draws triangulation of random points.
"""

import random
import math

from svglib import SVGImage


IMG_WIDTH = 1000
IMG_HEIGHT = 1000
POINTS_NUM = 10
POINTS_RADIUS = 4
LINE_WIDTH = 2
ANIMATION_SPEED = 0.05
BUFFER = 200

def get_random_number(a=0, b=IMG_WIDTH):
    return random.choice(range(a, b))

def intersect(line1, line2):
    """ Figure out if the intersect point is on the both lines

    TODO: needs some buffer, to handle intersection in vertecies
    """
    px, py = get_intersect(line1, line2)
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    l1 = False
    l2 = False
    print(px, py)

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
    print(l1)

    # second line
    if x3 <= x4:
        if y3 <= y4:
            if px >= x3 and px <= x4 and py >= y3 and py <= y4:
                l2 = True
        else:
            if px >= x3 and px <= x4 and py <= y3 and py >= y4:
                l2 = True
    else:
        if y3 <= y4:
            if px <= x3 and px >= x4 and py >= y3 and py <= y4:
                l2 = True
        else:
            if px <= x3 and px >= x4 and py <= y3 and py >= y4:
                l2 = True
    print(l2)

    return (l1 and l2)

def get_intersect(line1, line2):
    #line1 = tuple(map(lambda x: x+0.01, line1))
    #line2 = tuple(map(lambda x: x-0.01, line2))
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    px1 = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))
    px2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    if px2 == 0: px2 = 0.000001
    px = px1 / px2
    py1 = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))
    py2 = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    if py2 == 0: py2 = 0.000001
    py = py1 / py2
    return (px, py)

def draw_triangulation():
    img = SVGImage(IMG_WIDTH, IMG_HEIGHT, center_origin=False, show_borders_and_origin=True, animate=True, animation_speed=ANIMATION_SPEED)

    def generate_points(number):
        points = []
        for i in range(number):
            x = get_random_number(BUFFER, IMG_WIDTH-BUFFER)
            y = get_random_number(BUFFER, IMG_HEIGHT-BUFFER)
            points.append((x, y))
        return points


    points = generate_points(POINTS_NUM)
    #points = [(200, 200), (400, 150), (500, 400), (450, 700), (300, 600)]
    #points = [(200, 200), (400, 150), (500, 400), (450, 700)]
    #points = [(341, 518), (653, 605), (363, 476), (676, 308)]


    print(points)

    def shorten_line(line, step=10):
        x1, y1, x2, y2 = list(line)
        if x2 > x1:
            x = x2 - x1
            x1 += x/step
            x2 -= x/step
        else:
            x = x1 - x2
            x1 -= x/step
            x2 += x/step
        if y2 > y1:
            y = y2 - y1
            y1 += y/step
            y2 -= y/step
        else:
            y = y1 - y2
            y1 -= y/step
            y2 += y/step
        return (x1, y1, x2, y2)

    def intersect_some_collected(line, collected):
        for i in collected:
            a = shorten_line(i)
            b = shorten_line(line)

            if intersect(a, b):
                print("III", line, i)
                return True
        return False

    def get_lines(points):
        collected = []
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                if point1+point2 in collected:
                    continue
                if point2+point1 in collected:
                    continue
                line = point1 + point2

                if not intersect_some_collected(line, collected):
                    collected.append(line)
                print(collected)
        return collected

    lines = get_lines(points)
    """
    lines = [ (200, 200, 450, 700)]
    x = (300, 600, 400, 150)
    print(intersect_some_collected(x, lines))
    print(intersect(lines[0], x))
    img.add_line(*x, width=LINE_WIDTH*4)
    img.add_circle(330.7692307692308, 461.53846153846155, POINTS_RADIUS, fill="red")
    """

    ## draw points
    for point in points:
        img.add_circle(point[0], point[1], POINTS_RADIUS, color="black", fill="red")

    ## draw lines
    for line in lines:
        img.add_line(*line, width=LINE_WIDTH)

    img.save("img/triangulation_animate.svg")
draw_triangulation()
