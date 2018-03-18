"""
Tomas Meszaros

Draws polygons and stars with turtle.

TODO:
- make stars properly centered
"""

import math

from myturtle import Turtle


def draw_polygons():
    t = Turtle(center_origin=True, show_borders_and_origin=False, animate=True, animation_speed=0.05)
    def draw_n_polygon(t, polygon_sides, triangle_side=100, line_width=1):
        """ Draws polygon
        polygon_sides: number of sides of the polygon
        triangle_side: length from the center of polygon to the endge
        """
        center_triangle_angle = 360 / polygon_sides
        point_angle = (180 - center_triangle_angle) / 2
        for i in range(1, polygon_sides+1):
            t.penup()
            t.forward(triangle_side, width=line_width)
            t.right(180 - point_angle)
            half = math.sin(math.radians(center_triangle_angle/2)) * triangle_side
            t.pendown()
            t.forward(half * 2, width=line_width)
            t.right(180 - point_angle)
            t.penup()
            t.forward(triangle_side, width=line_width)
            # get to right orientation
            t.angle += 180

    for i in range(3, 26):
        draw_n_polygon(t, i, triangle_side=20*i, line_width=i-2)
    t.save("img/3_to_25_polygons.svg")
draw_polygons()


def draw_stars():
    t = Turtle(center_origin=True, show_borders_and_origin=False, animate=True, animation_speed=0.1)
    def draw_n_star(t, star_points, triangle_side=200, line_width=1):
        """ Draws star
        star_points: number of star point
        triangle_side: line length from point ot point
        """
        n = star_points
        if n % 2 == 0:
            n += 1
        length = triangle_side
        # move to position
        t.penup()
        t.left(90)
        t.forward(length/2)
        t.pendown()
        for i in range(1, n+1):
            t.left(180-(360/n/2))
            t.forward(length, width=line_width)

    draw_n_star(t, 30, triangle_side=400)
    t.save("img/star.svg")
draw_stars()
