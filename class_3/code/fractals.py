"""
Tomas Meszaros

Draws fractals using turtle.

TODO:
-
"""

import math

from myturtle import Turtle



def snowflake():
    t = Turtle(width=1000, height=1000, center_origin=True, show_borders_and_origin=True, animate=True, animation_speed=0.01)
    n = 5
    pentagon_side = 20
    center_angle = 360 / n
    triangle_angle = (180 - center_angle) / 2
    turn_angle = 2 * (180 - triangle_angle - 90)

    def draw_snowflake(t, pentagon_side):
        #t.set_x(x)
        #t.set_y(y)

        def draw_pentagon(t, pentagon_side):
            for _ in range(n):
                t.left(turn_angle)
                t.forward(pentagon_side)
            t.back(pentagon_side)
            t.left(turn_angle)

        for _ in range(5):
            draw_pentagon(t, pentagon_side)

    print(turn_angle / 2)

    MAGIC = 4.2
    for i in range(1, 2*n, 2):
        draw_snowflake(t, pentagon_side)
        t.left(i/2 * turn_angle) # level to 0
        t.back(MAGIC * pentagon_side, width=3)
        t.reset_angle()

    for i in range(1, 2*n, 2):
        draw_snowflake(t, pentagon_side)
        t.left(i/2 * turn_angle) # level to 0
        t.back(MAGIC * pentagon_side, width=3)
        t.reset_angle()

    t.save("img/snowflake_fractal.svg")

## Draw tree fractal
def tree():
    t = Turtle(width=800, height=800, center_origin=True, show_borders_and_origin=True, animate=True, animation_speed=0.005)

    t.set_y(-400)
    length = 200
    branch_angle = 20
    branch_scale = 0.7
    steps = 10
    t.left(90) # starting position
    t.forward(length, width=steps/2)

    def draw_branch(length, direction, steps):
        if steps == 0:
            return

        if direction == "left":
            t.left(branch_angle)
        else:
            t.right(branch_angle)

        t.forward(length, width=steps/3)
        draw_branch(length*branch_scale, "left", steps-1)
        draw_branch(length*branch_scale, "right", steps-1)

        t.penup()
        t.back(length, width=3)
        if direction == "left":
            t.right(branch_angle)
        else:
            t.left(branch_angle)
        t.pendown()

    draw_branch(length*branch_scale, "left", steps)
    draw_branch(length*branch_scale, "right", steps)

    t.save("img/tree_fractal.svg")
tree()
