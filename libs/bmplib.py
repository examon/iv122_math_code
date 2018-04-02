import math

from PIL import Image

"""
BMP library
"""

class BMPImage(object):
    def __init__(self, width=256, height=256, scale=1, bg="white", origin="top_left"):
        """
        origin: top_left|bottom_left|cartesian
        """
        self.width = width
        self.height = height
        self.scale = scale
        self.origin = origin

        self.pixel_width = int(scale)
        self.pixel_height = int(scale)

        self.img = Image.new("RGB", (self.width*scale, self.height*scale), bg)
        self.pixels = self.img.load()

    def set_origin(self, origin):
        assert(origin == "top_left" or origin == "bottom_left" or origin == "cartesian")
        self.origin = origin

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pixel(self, x, y):
        i = 0;
        j = 0;
        if self.origin == "bottom_left":
            return self.pixels[x*self.scale+i, (self.height-y-1)*self.scale+j]
        elif self.origin == "cartesian":
            return self.pixels[(x+int(self.width/2))*self.scale+i, (self.height-(y+int(self.height/2))-1)*self.scale+j]
        elif self.origin == "top_left":
            return self.pixels[x*self.scale+i, y*self.scale+j]
        return None

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

    def put_pixel(self, x, y, color):
        for i in range(self.pixel_width):
            for j in range(self.pixel_height):
                if self.origin == "bottom_left":
                    self.pixels[x*self.scale+i, (self.height-y-1)*self.scale+j] = (color[0], color[1], color[2])
                elif self.origin == "cartesian":
                    self.pixels[(x+int(self.width/2))*self.scale+i, (self.height-(y+int(self.height/2))-1)*self.scale+j] = (color[0], color[1], color[2])
                elif self.origin == "top_left":
                    self.pixels[x*self.scale+i, y*self.scale+j] = (color[0], color[1], color[2])
                else:
                    raise Exception("Invalid origin")

    def put_box(self, x, y, color=(0, 0, 0), width=1):
        """ draws bos around (x, y) of specified width
        """
        assert(width > 0)
        if width == 1:
            self.put_pixel(x, y, color=color)
            return
        for i in range(x-int(width/2), x+int(width/2)):
            for j in range(y-int(width/2), y+int(width/2)):
                self.put_pixel(i, j, color=color)

    def draw_rect(self, x1, y1, x2, y2, color=(0, 0, 0), width=1, precision=1000):
        self.draw_line(x1, y1, x1+1, y2, color, width, precision)
        self.draw_line(x1, y2+1, x2, y2, color, width, precision)
        self.draw_line(x2, y2, x2+1, y1, color, width, precision)
        self.draw_line(x2, y1+1, x1, y1, color, width, precision)


    def draw_line(self, x1=0, y1=0, x2=0, y2=0, color=(0, 0, 0), width=1, precision=10):
        """ Draws line

        TODO: this algo is not that good...

        precision: more == smoother line, without missing pixels

        implicit:
        a*x + b*y + c = 0
        parametric:
        x = t
        y = a*t + b
        """
        # so we do not divide by 0
        if x2 == 0:
            x2 = 1

        # in degrees
        x1 += 0.000001
        angle = math.atan(abs(y2-y1)/abs(x2-x1)) * 180 / math.pi
        x1 = int(x1)
        x2 = int(x2)

        if x2-x1 < 0:
            sample = range(abs(x2-x1+1)*precision, -1, -1)
        else:
            sample = range(0, (x2-x1)*precision)

        for dx in sample:
            tan_angle = math.tan(math.radians(angle))
            dy = dx * math.tan(math.radians(angle))
            nx = int(x1+dx/precision)
            ny = int(y1+dy/precision)
            if x2-x1 <= 0:
                nx = int(x1-dx/precision)
            if y2-y1 <= 0:
                ny = int(y1-dy/precision)
            self.put_box(nx, ny, color=color, width=width)
