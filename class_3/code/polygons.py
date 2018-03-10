"""
Tomas Meszaros
"""

import math

from myturtle import Turtle


t = Turtle(center_origin=True, show_borders_and_origin=False)

def draw_n_polygon(t, polygon_sides, triangle_side=100, path="n_body.svg", show_intriangle_side=False):
    """ Draws polygon
    polygon_sides: number of sides of the polygon
    triangle_side: length from the center of polygon to the endge
    """
    center_triangle_angle = 360 / polygon_sides
    point_angle = (180 - center_triangle_angle) / 2
    for i in range(1, polygon_sides+1):
        t.penup()
        t.forward(triangle_side)
        t.right(180 - point_angle)
        half = math.sin(math.radians(center_triangle_angle/2)) * triangle_side
        t.pendown()
        t.forward(half * 2)
        t.right(180 - point_angle)
        t.penup()
        t.forward(triangle_side)
        # get to right orientation
        t.angle += 180

for i in range(3, 11):
    draw_n_polygon(t, i, triangle_side=20*i)
t.save("img/3_to_10_polygons.svg")





"""
t2 = Turtle(center_origin=True, show_borders_and_origin=True)
for _ in range(4):
    t2.left(45)
    t2.forward(100)
t2.save("turtle_star.svg")
"""
