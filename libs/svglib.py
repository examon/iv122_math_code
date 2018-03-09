
"""
<svg xmlns="http://www.w3.org/2000/svg">

<line x1="15" y1="20" x2="30" y2="80"
stroke="black" stroke-width="1"/>

<circle cx="130" cy="50" r="30" stroke="blue"
stroke-width="2" fill="green" />

<polyline fill="none" stroke="red" stroke-width="4"
points="160,20 180,30 200,10 234,80"/>

</svg>
"""

class SVGImage(object):
    def __init__(self, width=800, height=600, center_origin=False, show_borders_and_origin=False):
        """
        width: image width in px
        height: image height in px
        center_origin: if True, uses cartesian system (instead of 0,0 at the top left)
        show_borders_and_origin: if True, prints origin and image borders
        """
        self.width = width
        self.height = height
        self.center_origin = center_origin
        self.header = '<svg width="%d" height="%d" xmlns="http://www.w3.org/2000/svg">\n' % (self.width, self.height)
        self.tail = "</svg>\n"
        self.elements = []

        if show_borders_and_origin:
            self.add_boarders_and_origin()

    def save(self, path):
        f = open(path, 'w')
        f.write(self.header)
        for i in self.elements:
            f.write(i)
            f.write('\n')
        f.write(self.tail)
        f.close()

    def add_boarders_and_origin(self, color="red", width=5):
        self.add_line(0, 0, 0, self.height, color, width, center_origin=False)
        self.add_line(0, self.height, self.width, self.height, color, width, center_origin=False)
        self.add_line(self.width, self.height, self.width, 0, color, width, center_origin=False)
        self.add_line(0, 0, self.width, 0, color, width, center_origin=False)
        self.add_circle(0, 0, 3, color, width, color)

    def add_line(self, x1, y1, x2, y2, color="black", width=1, center_origin=None):
        center_origin = self.center_origin if center_origin is None else center_origin
        if center_origin:
            x1 += self.width / 2
            x2 += self.width / 2
            y1 += (self.height / 2) - (2 * y1)
            y2 += (self.height / 2) - (2 * y2)
        self.elements.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%d"/>' % (x1, y1, x2, y2, color, width))

    def add_circle(self, x, y, r, color="black", width=1, fill="black", center_origin=None):
        center_origin = self.center_origin if center_origin is None else center_origin
        if center_origin:
            x += self.width / 2
            y += self.height / 2
        self.elements.append('<circle cx="%d" cy="%d" r="%d" stroke="%s" stroke-width="%d" fill="%s" />' % (x, y, r, color, width, fill))

