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


depth = 30
modulus = 5
scale = 4
pascals = generate_pascals(depth, modulus)
#for row in pascals: print(row)

# the magic takes care of redundant column in case of even width
img = BMPImage(width=(depth*2 if depth*2 % 2 != 0 else depth*2-1), height=depth, scale=scale, bg="black")

# set color specturm
spectrum = [0]*(modulus+modulus)
step = int(255/len(spectrum))
last = 0
for i, num in enumerate(spectrum):
    spectrum[i] += last+step
    last = spectrum[i]
print(spectrum)


# draw triangle to img
spaces = int(depth)-1
for y in range(len(pascals)):
    for x in range(y+1):
        num = pascals[y][x]
        img.put_pixel(2*x+spaces, y, (spectrum[num], spectrum[num], int((spectrum[num]+spectrum[num])/2)))
    spaces -= 1

img.save("pascals.bmp")
