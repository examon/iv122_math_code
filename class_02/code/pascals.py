"""
Tomas Meszaros

Homework 2.B.

Draws colored Pascals triangle into image.


TODO:
- add nicer colors
- make triangle compact
- move constants up
"""


import sys

from bmplib import BMPImage



def generate_pascals(n=5, d=sys.maxsize):
    pascals = []
    for row in range(n):
        pascals.append([None]*(row+1))
        for i in range(row+1):
            if i == 0 or i == row:
                pascals[row][i] = 1
            else:
                pascals[row][i] = pascals[row-1][i-1] % d + pascals[row-1][i] % d
    return pascals


def draw_pascals():
    DEPTH = 30
    MODULUS = 5
    SCALE = 20
    pascals = generate_pascals(DEPTH, MODULUS)
    #for row in pascals: print(row)

    # the magic takes care of redundant column in case of even width
    img = BMPImage(width=(DEPTH*2 if DEPTH*2 % 2 != 0 else DEPTH*2-1), height=DEPTH, scale=SCALE, bg="black")

    # set color specturm
    spectrum = [0]*(MODULUS+MODULUS)
    step = int(255/len(spectrum))
    last = 0
    for i, num in enumerate(spectrum):
        spectrum[i] += last+step
        last = spectrum[i]
    #print(spectrum)


    # draw triangle to img
    spaces = int(DEPTH)-1
    for y in range(len(pascals)):
        for x in range(y+1):
            num = pascals[y][x]
            img.put_pixel(2*x+spaces, y, (spectrum[num], spectrum[num], int((spectrum[num]+spectrum[num])/2)))
        spaces -= 1

    img.save("img/pascals.bmp")

draw_pascals()
