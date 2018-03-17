"""
Tomas Meszaros

Drawing cool effects.
"""

from bmplib import BMPImage

img = BMPImage(scale=1, width=500, height=500, origin="top_left")

def draw_field(img):
    """ circle implicit
    (x-a)**2 + (y-b)**2 = r**2
    """

    box_width = int(img.get_width()/10)

    cy = int(box_width/2)
    for i in range(1, int(img.get_height()/box_width)+1):
        cx = int(box_width/2)
        for j in range(1, int(img.get_width()/box_width)+1):
            if (i+j) % 2 == 0:
                img.put_box(cx, cy, width=box_width)
            cx += box_width
        cy += box_width

def draw_circle(img, r1, r2):
    for x in img.get_x_coords():
        for y in img.get_y_coords():
            if (x)**2 + (y)**2 >= r1**2 and (x)**2 + (y)**2 <= r2**2:
                #r, g, b = img.get_pixel(x, y)
                #print(r, g, b)
                p = img.get_pixel(x, y)
                if p == (0, 0, 0):
                    img.put_pixel(x, y, (255, 255, 255))
                else:
                    img.put_pixel(x, y, (0, 0, 0))


draw_field(img)

img.put_pixel(0, 0, color=(255, 0, 0))
img.set_origin("cartesian")
img.put_pixel(0, 0, color=(255, 0, 0))

# TODO: fix this, cannot write more then 2 inversions
"""
num_circles = 10
for i in range(1, num_circles):
    print(i)
    r1 = i*20
    r2 = r1 + 20
    draw_circle(img, r1, r2)
"""
draw_circle(img, 80, 100)
draw_circle(img, 60, 80)
draw_circle(img, 40, 60)
draw_circle(img, 20, 40)


img.save("img/circles_effect.bmp")
