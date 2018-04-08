"""
Tomas Meszaros

Drawing of Mandelbrot set
"""

import math

from bmplib import BMPImage

WIDTH = 600
HEIGHT = int(2*(WIDTH/3))
RES_X = int(1.01*WIDTH)
RES_Y = int(1.01*HEIGHT)
ITERS = 66.5

def map_point(x, img_x1, img_x2, to_x1, to_x2):
    img_size = abs(img_x1-img_x2)
    to_size = abs(to_x1-to_x2)
    ratio = img_size/to_size
    adj_x = abs(to_x1-x) * ratio
    new_x = img_x1 + adj_x
    return new_x

def in_mandelbrot(x, y, iters):
    zn = complex(0, 0)
    for i in range(int(iters)):
        zn = zn*zn + complex(x, y)
        if (zn.real*zn.real + zn.imag*zn.imag) > 4:
            # map number of iterations to color
            c = int(map_point(i, 0, 255, 0, int(iters)))+1
            return (c%255+int(math.sqrt(c)), int(i/c), int(i/c))
    return (0, 0, 0)

def put_pixel(img, x, y, color):
    nx = x+WIDTH/3/2
    ny = y
    img.put_pixel(nx, ny, color)

def draw_mandelbrot(r1=-2, r2=1, i1=-1, i2=1, tag=""):
    assert(r1<r2 and i1<i2)
    cx = (r1+r2)/2
    cy = (i1+i2)/2
    dif_r = abs(r1-r2)
    dif_i = abs(i1-i2)
    zoom_lvl = 3/dif_r

    # increasing iterations by zoom level (found this one on net)
    iters = math.sqrt(2*math.sqrt(abs(1-math.sqrt(10*zoom_lvl))))*ITERS
    #iters = 50+math.log(((4/abs(dif_r))), 10)**5
    print("cx: %f, cy: %f, r1: %f, r2: %f, i1: %f, i2: %f, zoom_lvl: %f, iters: %f" % (cx, cy, r1, r2, i1, i2, zoom_lvl, iters))

    img = BMPImage(width=WIDTH, height=HEIGHT, scale=1, bg="white", origin="cartesian")
    for xi in range(RES_X):
        x = r1+dif_r*(xi/RES_X)
        for yi in range(RES_Y):
            y = i1+dif_i*(yi/RES_Y)
            color = in_mandelbrot(x, y, iters)
            new_x = x*HEIGHT/2
            new_y = y*HEIGHT/2
            nx = map_point(new_x, -400, 200, r1*200, r2*200)
            ny = map_point(new_y, -200, 200, i1*200, i2*200)
            put_pixel(img, nx, ny, color)
    img.save("img/mandelbrot/{TAG}mandelbrot_{R1}_{R2}_{I1}_{I2}.bmp".format(TAG=tag, R1=r1, R2=r2, I1=i1, I2=i2))

def make_mandelbrot_zoomed_sequence():
    r1 = -2
    r2 = 1
    i1 = -1
    i2 = 1
    frames = 100
    zoom_by = 9

    # target zoom coordinates (found on the net)
    tx = -0.743643887037158704752191506114774
    ty = 0.131825904205311970493132056385139

    for i in range(frames):
        frame_id = "%02d_" % i
        draw_mandelbrot(r1, r2, i1, i2, tag=frame_id)
        zoom = (abs(r1)-abs(r2))/zoom_by
        zoom_lvl = 3*abs(r1-r2)

        r1 += zoom
        r2 -= zoom
        i1 += zoom*2/3
        i2 -= zoom*2/3

        cx = abs(tx-(r1+r2)/2)/(0.8+1/zoom_lvl)
        cy = abs(ty-(i1+i2)/2)/(0.8+1/zoom_lvl)

        # zoom to the target point
        if abs(tx-((r1+cx)+(r2+cx))/2) < abs(tx-((r1-cx)+(r2-cx))/2):
            r1 += cx
            r2 += cx
        else:
            r1 -= cx
            r2 -= cx

        if abs(ty-((i1+cy)+(i2+cy))/2) < abs(ty-((i1-cy)+(i2-cy))/2):
            i1 += cy
            i2 += cy
        else:
            i1 -= cy
            i2 -= cy

make_mandelbrot_zoomed_sequence()
