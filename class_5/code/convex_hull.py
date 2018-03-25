"""
Tomas Meszaros

Draws convex hull around points.
"""

import random
import math

from svglib import SVGImage


IMG_WIDTH = 1000
IMG_HEIGHT = 1000
POINTS_NUM = 200
POINTS_RADIUS = 4
LINE_WIDTH = 2
ANIMATION_SPEED = 0.02
BUFFER = 100

def get_random_number(a=0, b=100):
    return random.choice(range(a, b))

def get_angle(point1, point2, direction):
    x1, y1 = point1
    x2, y2 = point2
    x = abs(x1-x2)
    y = abs(y1-y2)
    c = math.sqrt(x**2 + y**2)
    angle = math.acos(y / c) * 180 / math.pi

    if x1 <= x2 and y1 <= y2:
        if direction == "right":
            return angle
        else:
            return 180 + angle
    if x1 <= x2 and y1 >= y2:
        if direction == "right":
            return 180 - angle
        else:
            return 360 - angle
    if x1 >= x2 and y1 <= y2:
        if direction == "right":
            return 180 + angle
        else:
            return 180 - angle
    if x1 >= x2 and y1 >= y2:
        if direction == "right":
            return 180 + angle
        else:
            return angle

def draw_convex_hull():
    def generate_points(number):
        points = []
        for i in range(number):
            x = get_random_number(BUFFER, IMG_WIDTH-BUFFER)
            y = get_random_number(BUFFER, IMG_HEIGHT-BUFFER)
            points.append((x, y))
        return points

    def get_lines(points):
        if len(points) < 1:
            return []
        ## final lines to be drawn
        lines = []

        ## get the leftmost and rightmost point
        first = points[0]
        last = points[0]
        for point in points:
            if point[0] < first[0]:
                first = point
            if point[0] > last[0]:
                last = point

        point1 = first
        direction = "right"
        while True:
            candidate = None
            candidate_angle = 360
            for point2 in points:
                if point1 == point2:
                    continue
                x1, y1 = point1
                x2, y2 = point2
                angle = get_angle(point1, point2, direction)

                if angle <= candidate_angle:
                    candidate = point2
                    candidate_angle = angle
            lines.append(candidate+point1)
            point1 = candidate
            if candidate == last and direction == "right":
                direction = "left"
            if candidate == first and direction == "left":
                break
        return lines

    def draw_points(points):
        for point in points:
            img.add_circle(point[0], point[1], POINTS_RADIUS, color="black", fill="red")

    def draw_lines(lines):
        for line in lines:
            img.add_line(*line, width=LINE_WIDTH)

    ## Draw the stuff
    img = SVGImage(IMG_WIDTH, IMG_HEIGHT, center_origin=False, show_borders_and_origin=False, animate=True, animation_speed=ANIMATION_SPEED)

    points = generate_points(POINTS_NUM)
    draw_points(points)
    print(points)

    while len(points) > 0:
        lines = get_lines(points)
        draw_lines(lines)

        ## remove used points
        for line in lines:
            x1, y1, x2, y2 = line
            print(line)
            points.remove((x1, y1))
            print(points)

    img.save("img/convex_hull_concentric_animate.svg")
draw_convex_hull()
