import math

from svglib import SVGImage


class Turtle(object):
    def __init__(self, width=800, height=600, center_origin=False, show_borders_and_origin=False, animate=False, animation_speed=0.1):
        self.img = SVGImage(width, height, center_origin=center_origin, show_borders_and_origin=show_borders_and_origin, animate=animate, animation_speed=animation_speed)
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

    def forward(self, steps, color="black", width=1, debug=False):
        """ steps: in pixels
        """
        print(self.x, self.y, self.angle) if debug else None
        nx = self.x + math.cos(math.radians(self.angle))*steps
        ny = self.y + math.sin(math.radians(self.angle))*steps
        if self.is_pendown:
            self.img.add_line(self.x, self.y, nx, ny, color=color, width=width)
        self.x = nx
        self.y = ny
        print(self.x, self.y, self.angle) if debug else None

    def back(self, steps, color="black", width=1, debug=False):
        """ steps: in pixels
        """
        print(self.x, self.y, self.angle) if debug else None
        self.forward(-steps, color=color, width=width)
        print(self.x, self.y, self.angle) if debug else None

    def right(self, angle):
        """ angle: in degrees
        """
        self.angle -= angle

    def left(self, angle):
        """ angle: in degrees
        """
        self.angle += angle

    def penup(self):
        """ stop drawing
        """
        self.is_pendown = False

    def pendown(self):
        """ start drawing
        """
        self.is_pendown = True
