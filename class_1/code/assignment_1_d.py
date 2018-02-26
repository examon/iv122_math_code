"""
Tomas Meszaros

Visualizations of the Greatest common divisor.
"""

import math

from bmplib import BMPImage
from pprint import pprint as pp


def gcd_mod_variant(a, b, steps=1):
    """ From slides
    """
    if b == 0:
        return (a, steps)
    else:
        return gcd_mod_variant(b, a % b, steps+1)

def gcd_sub_variant(a, b):
    """ From wikipedia
    """
    steps = 1
    if a == 0 or b == 0:
        return (1, steps)
    while a != b:
        if a > b:
           a = a - b
        else:
           b = b - a
        steps += 1
    return (a, steps)

width = 512
height = 512
img_divs = BMPImage(width, height)
img_euclid_steps_mod = BMPImage(width, height)
img_euclid_steps_sub = BMPImage(width, height)
img_euclid_steps_mix = BMPImage(width, height)

for i in range(int(img_divs.width)):
    for j in range(img_divs.height):
        div_mod, steps_mod = gcd_mod_variant(i, j)
        _, steps_sub = gcd_sub_variant(i, j)

        # to get nicer colors
        steps_mod *= 20
        steps_sub *= 10
        steps_mix = int((steps_mod + steps_sub) / 2)
        div_mod = int(math.log(1 if div_mod == 0 else div_mod, 1.5) * 10)

        img_divs.put_pixel(i, j, (div_mod, div_mod, div_mod))
        img_euclid_steps_mod.put_pixel(i, j, (steps_mod, steps_mod, steps_mod))
        img_euclid_steps_sub.put_pixel(i, j, (steps_sub, steps_sub, steps_sub))
        img_euclid_steps_mix.put_pixel(i, j, (steps_mix, steps_mix, steps_mix))


img_divs.save("gcd_visualization.bmp")
img_euclid_steps_mod.save("euclid_steps_mod_visualization.bmp")
img_euclid_steps_sub.save("euclid_steps_sub_visualization.bmp")
img_euclid_steps_mix.save("euclid_steps_mix_visualization.bmp")
