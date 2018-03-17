"""
Tomas Meszaros

Drawing basic shapes using bitmap graphics.

TODO:
- fix spiral sparse lines (draw bunch of pixels near each pixel
- ellipse tilt
"""

import math

from bmplib import BMPImage


def circle_implicit(save_file, r, a=None, b=None, img_scale=3):
    """ circle implicit
    (x-a)**2 + (y-b)**2 = r**2
    """
    img = BMPImage(scale=3)
    if not a and not b:
        a = img.get_width()/2
        b = img.get_height()/2
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            if (x-a)**2 + (y-b)**2 < r**2:
                img.put_pixel(x, y, (0, 0, 0))
    img.save(save_file)
circle_implicit("img/circle_implicit.bmp", r=50)

def circle_parametric(save_file, r, edge_width, a=None, b=None, spirale_turns=1, img_scale=3):
    """ circle parametric
    x = a + r*cos(t)
    y = b + r*sin(t)

    spirale_turns: if > 1, circle will become spirale with spirale_turns turns
    """
    img = BMPImage(width=1000, height=1000, scale=img_scale)
    if not a and not b:
        a = img.get_width()/2
        b = img.get_height()/2
    for t in range(360*spirale_turns):
        for i in range(r, r+edge_width):
            ni = 0
            if spirale_turns > 1:
                ni = t/spirale_turns
            x = a + (i+ni)*math.cos(math.radians(t))
            y = a + (i+ni)*math.sin(math.radians(t))
            img.put_pixel(x, y, (0, 0, 0))
    img.save(save_file)
circle_parametric("img/circle_parametric.bmp", r=100, edge_width=4)
circle_parametric("img/spirale_parametric.bmp", r=10, edge_width=4, spirale_turns=10)

def triangle(save_file, img_scale=3, a=None, b=None):
    """ triangle
    when using cartesian coords:
    y <= x+10 and y <= -x+10 and y >= 0
    """
    img = BMPImage(scale=img_scale, origin="cartesian")
    side = 70
    for x in img.get_x_coords():
        for y in img.get_y_coords():
            if y <= x+side and y <= -x+side and y >= 0:
                img.put_pixel(x, y, (2*abs(x), abs(x)+abs(y), 2*abs(y)))
    img.save(save_file)
triangle("img/triangle.bmp")

def ellipse(save_file, img_scale=1, r=250, a=1, b=0.5):
    """ ellipse
    implicit:
    (x/a)**2 + (y/b)**2 = r**2
    parametric:
    x = a*cos(t)
    y = b*sin(t)
    """
    img = BMPImage(width=500, height=500, scale=img_scale, origin="cartesian")
    for x in img.get_x_coords():
        for y in img.get_y_coords():
            if (x/a)**2 + (y/b)**2 <= r**2:
                c = int(math.sqrt((x/a)**2 + (y/b)**2))
                img.put_pixel(x, y, (c, c, c))
    """
    for t in range(360):
        for i in range(r):
            x = int(a*math.cos(math.radians(t)) * i)
            y = int(b*math.sin(math.radians(t+45)) * i)
            img.put_pixel(x, y, (x, y, 0))
    """
    img.save(save_file)
ellipse("img/ellipse.bmp")
