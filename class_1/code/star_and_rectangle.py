"""
Tomas Meszaros

Test drawings using vector graphics.
"""

import os

from svglib import SVGImage


W = 800
H = 800
HEIGHT = H / 2


def draw_star():
    def draw_star_part(y1, y1_step, x2_step, x2_is_negative=False):
        x2 = 0
        while x2 <= HEIGHT:
            img.add_line(0, y1, -x2 if x2_is_negative else x2, 0)
            y1 += y1_step
            x2 += x2_step

    img = SVGImage(W, H, center_origin=True, show_borders_and_origin=False, animate=True, animation_speed=0.01)
    draw_star_part(  HEIGHT, -4,  4)
    draw_star_part(  HEIGHT, -8,  8, x2_is_negative=True)
    draw_star_part( -HEIGHT, 16, 16, x2_is_negative=True)
    draw_star_part( -HEIGHT, 32, 32)

    img.save("img/test_svg_star.svg")
draw_star()


def draw_rectangle():
    # non-abstracted code for rectangle
    rect_img = SVGImage(W, H, center_origin=True, show_borders_and_origin=False, animate=True, animation_speed=0.05)

    x1 = -HEIGHT
    y2 = HEIGHT
    while x1 <= HEIGHT:
        rect_img.add_line(x1, HEIGHT, HEIGHT, y2)
        x1 += 8
        y2 -= 8

    x1 = HEIGHT
    y2 = HEIGHT
    while -x1 <= HEIGHT:
        rect_img.add_line(x1, HEIGHT, -HEIGHT, y2)
        x1 -= 13
        y2 -= 13

    x1 = -HEIGHT
    y2 = HEIGHT
    while x1 <= HEIGHT:
        rect_img.add_line(x1, -HEIGHT, -HEIGHT, y2)
        x1 += 21
        y2 -= 21

    x1 = -HEIGHT
    y2 = -HEIGHT
    while x1 <= HEIGHT:
        rect_img.add_line(x1, -HEIGHT, HEIGHT, y2)
        x1 += 34
        y2 += 34

    rect_img.save("img/test_svg_rect.svg")
draw_rectangle()
