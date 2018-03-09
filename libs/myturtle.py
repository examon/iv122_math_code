import math

from svglib import SVGImage


class Turtle(object):
    def __init__(self, width=800, height=600, center_origin=False, show_borders_and_origin=False):
        self.img = SVGImage(width, height, center_origin, show_borders_and_origin)
        # current turtle state
        self.x = 0
        self.y = 0
        # angle in degrees
        self.angle = 0
        self.is_pendown = True

    def save(self, path):
        self.img.save(path)

    def reset(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def forward(self, steps):
        """ steps: in pixels
        """
        nx = self.x + math.cos(math.radians(self.angle))*steps
        ny = self.y + math.sin(math.radians(self.angle))*steps
        if self.is_pendown:
            self.img.add_line(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny

    def back(self, steps):
        # TODO
        pass

    def right(self, angle):
        """ angle: in degrees
        """
        self.right -= angle

    def left(self, angle):
        """ angle: in degrees
        """
        self.angle += angle

    def penup(self):
        self.is_pendown = False

    def pendown(self):
        self.is_pendown = True