"""
Tomas Meszaros

Drawing cool effects on the checkerboard.
"""

import random

from bmplib import BMPImage


def draw_field(img):
    """ Draws checkerboard field
    """
    box_width = int(img.get_width()/10)
    cy = int(box_width/2)
    for i in range(1, int(img.get_height()/box_width)+1):
        cx = int(box_width/2)
        for j in range(1, int(img.get_width()/box_width)+1):
            if (i+j) % 2 == 0:
                img.put_box(cx, cy, width=box_width)
            cx += box_width
        cy += box_width

def draw_inverted_circle(img, r1, r2):
    """ Draws circle with inverted color on the board
    """
    for x in img.get_x_coords():
        for y in img.get_y_coords():
            if x**2 + y**2 >= r1**2 and x**2 + y**2 <= r2**2:
                if img.get_pixel(x, y)  == (0, 0, 0):
                    img.put_pixel(x, y, (255, 255, 255))
                else:
                    img.put_pixel(x, y, (0, 0, 0))

def draw_inverted_ellipse(img, r1, r2, a=1, b=0.5, tilt=1):
    """ Draws ellipse with inverted color on the board
    """
    for x in img.get_x_coords():
        for y in img.get_y_coords():
            e = (x/a)**2 + (y/b)**2 + (tilt*x*y)
            if e >= r1**2 and e <= r2**2:
                if img.get_pixel(x, y)  == (0, 0, 0):
                    img.put_pixel(x, y, (255, 255, 255))
                else:
                    img.put_pixel(x, y, (0, 0, 0))

def draw_circles(img):
    num_circles = 20
    circle_width = 3
    scale_factor = 1.6
    for i in range(0, num_circles, 2):
        r1 = i*(circle_width/2)
        r2 = r1 + circle_width
        draw_inverted_circle(img, r1, r2)
        circle_width *= scale_factor

def draw_effect_concentric_circles():
    img = BMPImage(scale=1, width=1000, height=1000, origin="top_left")
    draw_field(img)
    img.set_origin("cartesian")
    draw_circles(img)
    img.save("img/circles_effect.bmp")
draw_effect_concentric_circles()

def draw_effect_ellipses(num_of_ellipses, r1, r2, a, b):
    img = BMPImage(scale=1, width=1000, height=1000, origin="top_left")
    draw_field(img)
    img.set_origin("cartesian")

    for i in range(1, num_of_ellipses+1):
        draw_inverted_ellipse(img, r1, r2, a=a, b=b, tilt=i)
    for i in range(-num_of_ellipses, 0):
        draw_inverted_ellipse(img, r1, r2, a=a, b=b, tilt=i)
    img.save("img/ellipses_effect_{num_of_ellipses}_{r1}_{r2}_{a}_{b}.bmp".format(num_of_ellipses=num_of_ellipses, r1=r1, r2=r2, a=a, b=b))
draw_effect_ellipses(200, 200, 700, 0.8, 0.8)
