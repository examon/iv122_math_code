"""
Tomas Meszaros

Draws filled polygon.
"""

import math
import sys
import random

from bmplib import BMPImage


def draw_polygon(img, points, color=(0, 0, 0), line_width=2, precision=1):
    """
    TODO:
    - polygon points are not always touching when the angle at point is too small
      (this is is bug in line drawing algo
    """
    for i, point in enumerate(points):
        if i < len(points)-1:
            x1 = point[0]
            y1 = point[1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            img.draw_line(x1, y1, x2, y2, color=color, width=line_width, precision=precision)
        img.draw_line(points[0][0], points[0][1], points[-1][0], points[-1][1], color=color, width=line_width, precision=precision)

def flood_fill(img, x, y, color=(255, 0, 0)):
    # TODO: make this iterative
    if x < 0 or x >= img.get_width() or y < 0 or y >= img.get_height():
        return
    r, g, b = img.get_pixel(x, y)
    if r == 255 and g == 255 and b == 255:
        img.put_pixel(x, y, color)
        flood_fill(img, x+1, y)
        flood_fill(img, x-1, y)
        flood_fill(img, x, y+1)
        flood_fill(img, x, y-1)

img = BMPImage(scale=5, width=200, height=200, origin="bottom_left")

polygon_points = [(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)]
draw_polygon(img, polygon_points, line_width=7, precision=10)
sys.setrecursionlimit(sys.getrecursionlimit()*10)

# TODO: 15 15 is works only sometimes
flood_fill(img, 15, 15)

img.save("img/polygon.bmp")
