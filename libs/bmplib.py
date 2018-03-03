from PIL import Image

"""
BMP library

Coordinate system:

- (0, 0) origin is in the upper left corner
- (x, y): x left -> right, y up -> down
"""

class BMPImage(object):
    def __init__(self, width=256, height=256, scale=1, bg="white"):
        self.width = width
        self.height = height
        self.scale = scale

        self.pixel_width = int(1*scale)
        self.pixel_height = int(1*scale)

        self.img = Image.new("RGB", (self.width*scale, self.height*scale), bg)
        self.pixels = self.img.load()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def save(self, path, file_format="BMP"):
        self.img.save(path, file_format)

    def put_pixel(self, x, y, rgb):
        for i in range(self.pixel_width):
            for j in range(self.pixel_height):
                self.pixels[x*self.scale+i, y*self.scale+j] = (rgb[0], rgb[1], rgb[2])

