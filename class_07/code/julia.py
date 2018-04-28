"""
Tomas Meszaros

Draws Julia set
"""

import math

from bmplib import BMPImage

ITERS = 250
WIDTH = 300
HEIGHT = 200
RES_X = int(1.4*WIDTH)
RES_Y = int(1.4*HEIGHT)


def map_point(x, img_x1, img_x2, to_x1, to_x2):
    img_size = abs(img_x1-img_x2)
    to_size = abs(to_x1-to_x2)
    ratio = img_size/to_size
    adj_x = abs(to_x1-x) * ratio
    new_x = img_x1 + adj_x
    return new_x

def in_julia(c, x, y, iters):
    zn = complex(x, y)
    for i in range(int(iters)):
        zn = zn*zn + c
        if (zn.real*zn.real + zn.imag*zn.imag) > 4:
            # map number of iterations to color
            col = int(map_point(i, 0, 255, 0, int(iters)))
            return (col, col*i, col*col)
    col = int(map_point(i, 0, 255, 0, int(iters)))
    return (255, 255, 255)

def draw_julia(c, r1=-2, r2=2, i1=-2, i2=2, tag=""):
    assert(r1<r2 and i1<i2)
    dif_r = abs(r1-r2)
    dif_i = abs(i1-i2)
    zoom_lvl = 3/dif_r
    iters = ITERS
    print("c.real: %f, c.imag: %f, iters: %f" % (c.real, c.imag, iters))

    img = BMPImage(width=WIDTH, height=HEIGHT, scale=1, bg="white", origin="cartesian")
    for xi in range(RES_X):
        x = r1+dif_r*(xi/RES_X)
        for yi in range(RES_Y):
            y = i1+dif_i*(yi/RES_Y)
            color = in_julia(c, x, y, iters)
            nx = x*WIDTH/4
            ny = y*HEIGHT/4
            img.put_pixel(nx, ny, color)
    img.save("img/julia/{TAG}.bmp".format(TAG=tag, CR=c.real, CI=c.imag))

def julia_standard():
    real = -0.8
    frames = 100
    imag1 = list(range(-int(frames/2), int(frames/2)))
    imag2 = list(range(int(frames/2), -int(frames/2), -1))

    for i, val in enumerate(imag1+imag2):
        print(val/frames)
        c = complex(real, val/frames)
        draw_julia(c, tag="%04d" % i)
#julia_standard()

def julia_francy():
    base = (0.7885*math.e)
    frames = 100
    for i, val in enumerate(range(int(frames))):
        c = base**complex(0, 3*math.pi*val/frames)
        draw_julia(c, tag="%04d" % i)
#julia_francy()
