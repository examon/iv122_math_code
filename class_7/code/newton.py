"""
Tomas Meszaros

Draws Newton fractal
"""

import math

from bmplib import BMPImage

ITERS = 100
WIDTH = 1200
HEIGHT = 900
RES_X = int(1.1*WIDTH)
RES_Y = int(1.1*HEIGHT)

def pick_color(root):
    """ Choose color based on the proximity to some root.
    """
    if not root:
        return (0, 0, 0)
    a = complex(1, 0)
    b = complex(-0.5, math.sqrt(3)/2)
    c = complex(-0.5, -math.sqrt(3)/2)
    ar = abs(a-root)
    br = abs(b-root)
    cr = abs(c-root)
    if ar < br and ar < cr:
        return (255,0,0)
    if br < ar and br < cr:
        return (0,255,0)
    if cr < ar and cr < br:
        return (0,0,255)

def newtons_method(z):
    """ Computer root with Newtons method
    """
    for i in range(ITERS):
        fz = z*z*z-1
        fpz = 3*z*z
        if abs(fpz) == 0:
            return None
        z_new = z-fz/fpz
        if abs(z_new-z) < 0.0000000000001:
            return z
        z = z_new
    return None

def draw_newton(r1=-2, r2=2, i1=-2, i2=2, tag=""):
    assert(r1<r2 and i1<i2)
    dif_r = abs(r1-r2)
    dif_i = abs(i1-i2)

    img = BMPImage(width=WIDTH, height=HEIGHT, scale=1, bg="white", origin="cartesian")

    for xi in range(RES_X):
        x = r1+dif_r*(xi/RES_X)
        for yi in range(RES_Y):
            y = i1+dif_i*(yi/RES_Y)
            root = newtons_method(complex(x, y))
            nx = x*WIDTH/4
            ny = y*HEIGHT/4
            img.put_pixel(nx, ny, pick_color(root))
    img.save("img/newton/{TAG}.bmp".format(TAG=tag))

draw_newton()
