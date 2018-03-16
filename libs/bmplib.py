from PIL import Image

"""
BMP library

Coordinate system:

- (0, 0) origin is in the upper left corner
- (x, y): x left -> right, y up -> down
"""

class BMPImage(object):
    def __init__(self, width=256, height=256, scale=1, bg="white", origin="upper_left"):
        """
        origin: upper_left|bottom_left|cartesian
        """
        self.width = width
        self.height = height
        self.scale = scale
        self.origin = origin

        self.pixel_width = int(1*scale)
        self.pixel_height = int(1*scale)

        self.img = Image.new("RGB", (self.width*scale, self.height*scale), bg)
        self.pixels = self.img.load()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x_coords(self):
        if self.origin == "cartesian":
            return range(-int(self.width/2), int(self.width/2))
        else:
            # TODO: for other origins
            return None

    def get_y_coords(self):
        if self.origin == "cartesian":
            return range(-int(self.height/2), int(self.height/2))
        else:
            # TODO: for other origins
            return None

    def save(self, path, file_format="BMP"):
        self.img.save(path, file_format)

    def put_pixel(self, x, y, rgb):
        for i in range(self.pixel_width):
            for j in range(self.pixel_height):
                if self.origin == "bottom_left":
                    self.pixels[x*self.scale+i, (self.height-y-1)*self.scale+j] = (rgb[0], rgb[1], rgb[2])
                elif self.origin == "cartesian":
                    self.pixels[(x+int(self.width/2))*self.scale+i, (self.height-(y+int(self.height/2))-1)*self.scale+j] = (rgb[0], rgb[1], rgb[2])
                elif self.origin == "upper_left":
                    self.pixels[x*self.scale+i, y*self.scale+j] = (rgb[0], rgb[1], rgb[2])
                else:
                    raise Exception("Invalid origin")
