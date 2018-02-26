from PIL import Image

"""

from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (250,250), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()

"""

class BMPImage(object):
    def __init__(self, width=256, height=256, bg="white"):
        self.width = width
        self.height = height
        self.img = Image.new("RGB", (self.width, self.height), bg)
        self.pixels = self.img.load()

    def save(self, path, file_format="BMP"):
        self.img.save(path, file_format)

    def put_pixel(self, x, y, rgb):
        self.pixels[x, y] = (rgb[0], rgb[1], rgb[2])
