"""
Tomas Meszaros

Test drawings using vector graphics.
"""

import os

from svglib import SVGImage


w = 800
h = 800
height = h / 2


## Binary Star
"""
def draw_star(x1, x2, y1, y2, x1_step, y1_step, x2_step, y2_step, x2_is_negative=False):
    while x2 <= height:
        img.add_line(x1, y1, -x2 if x2_is_negative else x2, y2)
        x1 += x1_step
        y1 += y1_step
        x2 += x2_step
        y2 += y2_step
"""
def draw_star(y1, y1_step, x2_step, x2_is_negative=False):
    x2 = 0
    while x2 <= height:
        img.add_line(0, y1, -x2 if x2_is_negative else x2, 0)
        y1 += y1_step
        x2 += x2_step

img = SVGImage(w, h, center_origin=True, show_borders_and_origin=False)
draw_star(  height, -4,  4)
draw_star(  height, -8,  8, x2_is_negative=True)
draw_star( -height, 16, 16, x2_is_negative=True)
draw_star( -height, 32, 32)

# non-abstracted code for star
"""
# 1. quadrant
y1 = height
x2 = 0
while x2 <= height:
    img.add_line(0, y1, x2, 0)
    y1 -= 2
    x2 += 2

# 2. quadrant
y1 = height
x2 = 0
while x2 <= height:
    img.add_line(0, y1, -x2, 0)
    y1 -= 4
    x2 += 4

# 3. quadrant
y1 = -height
x2 = 0
while x2 <= height:
    img.add_line(0, y1, -x2, 0)
    y1 += 8
    x2 += 8

# 4. quadrant
y1 = -height
x2 = 0
while x2 <= height:
    img.add_line(0, y1, x2, 0)
    y1 += 16
    x2 += 16
"""

img.save("test_svg_star.svg")


## "Fibonnaci" Rectangle

#####################
# non-abstracted code for rectangle
rect_img = SVGImage(w, h, center_origin=True, show_borders_and_origin=False)

def draw_rect(x1, x2, y1, y2, x1_step, y1_step, x2_step, y2_step, x2_is_negative=False):
    while x2 <= height:
        img.add_line(x1, y1, -x2 if x2_is_negative else x2, y2)
        x1 += x1_step
        y1 += y1_step
        x2 += x2_step
        y2 += y2_step

x1 = -height
y2 = height
while x1 <= height:
    rect_img.add_line(x1, height, height, y2)
    x1 += 8
    y2 -= 8

x1 = height
y2 = height
while -x1 <= height:
    rect_img.add_line(x1, height, -height, y2)
    x1 -= 13
    y2 -= 13

x1 = -height
y2 = height
while x1 <= height:
    rect_img.add_line(x1, -height, -height, y2)
    x1 += 21
    y2 -= 21

x1 = -height
y2 = -height
while x1 <= height:
    rect_img.add_line(x1, -height, height, y2)
    x1 += 34
    y2 += 34
rect_img.save("test_svg_rect.svg")
