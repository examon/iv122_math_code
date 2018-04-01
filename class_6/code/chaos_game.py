"""
Tomas Meszaros

Drawing images using chaos game.

TODO:
- implement generic n-polygon fcn
"""

import random
import math

from bmplib import BMPImage

WIDTH = 1000
HEIGHT = 1000
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

def get_random_point():
    return (random.choice(range(-int(WIDTH/2), int(WIDTH/2))), random.choice(range(-int(HEIGHT/2), int(HEIGHT/2))))

def point_between_points(a, b, r=0.5):
    """ Returns point between points @a and @b.
    If @r is 0.5, point is located exactly half way between @a and @b.
    """
    x1, y1 = a
    x2, y2 = b
    nx = int(abs(x1 - x2) * r)
    ny = int(abs(y1 - y2) * r)
    if x1 <= x2 and y1 <= y2:
        return (x1+nx, y1+ny)
    elif x1 >= x2 and y1 <= y2:
        return (x1-nx, y1+ny)
    elif x1 >= x2 and y1 >= y2:
        return (x1-nx, y1-ny)
    elif x1 <= x2 and y1 >= y2:
        return (x1+nx, y1-ny)
    else:
        raise Exception("Invalid condition:", chosen_point, x, r)


def draw_sierpinski_triangle(r=0.5, iterations=1000000, save_after=[1000, 10000, 100000]):
    img = BMPImage(width=WIDTH, height=HEIGHT, scale=1, bg="black", origin="cartesian")

    SIDE = int(HEIGHT/1.2)
    ITERATIONS = iterations
    DISCARD = 100

    h = int((math.sqrt(3)/2)*SIDE)

    a = (-SIDE/2, -int(h/2))
    b = (SIDE/2, -int(h/2))
    c = (0, int(h/2))
    x = get_random_point()

    for i in range(ITERATIONS):
        chosen_point = random.choice([a, b, c])
        nx = point_between_points(chosen_point, x, r)
        if i > DISCARD:
            # Throw away first N points
            img.put_pixel(*nx, WHITE)
        x =  nx
        if i in save_after:
            img.save("img/chaos_game_sierpinski_r_{R}_after_{ITERS}.bmp".format(R=r, ITERS=i))
    img.save("img/chaos_game_sierpinski_r_{R}_after_{ITERS}.bmp".format(R=r, ITERS=ITERATIONS))

#for i in range(0, 10):
#    draw_sierpinski_triangle(r=i/10)
