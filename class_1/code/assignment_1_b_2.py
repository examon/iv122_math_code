"""
Tomas Meszaros

Test drawings using bitmap graphics.
"""

from bmplib import BMPImage

img = BMPImage(width=256, height=256)

for i in range(img.width):
    for j in range(img.height):
        img.put_pixel(i, j, (i, 0, j))

img.save("test_bmp.bmp")
