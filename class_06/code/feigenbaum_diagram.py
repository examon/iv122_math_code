"""
Tomas Meszaros

Drawing of bifurcation diagram.
"""

from bmplib import BMPImage


def feigenbaum_diagram(r1=0, r2=4, x1=0, x2=1, draw_rect=True):
    assert(r1 < r2 and x1 < x2)
    assert(0 <= r1 <= 4 and 0 <= r2 <= 4)
    assert(0 <= x1 <= 1 and 0 <= x2 <= 1)

    WIDTH = 1000
    HEIGHT = 600
    GENERATIONS = 500
    GENERATIONS_TAKE = 100
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    img = BMPImage(width=WIDTH, height=HEIGHT, scale=1, bg="black", origin="bottom_left")

    if draw_rect:
        # draw red rectangle in upper-right quadrant
        img.draw_rect(WIDTH/2, HEIGHT/2, WIDTH-5, HEIGHT-5, color=RED)

    for growth_rate in range(WIDTH):
        x = 0.5
        r = growth_rate/WIDTH*(r2-r1)
        assert(r2 >= r1+r >= r1)
        population = []
        for generation in range(GENERATIONS):
            x = (r1+r)*x*(1-x)
            if x1 < x < x2 and generation > (GENERATIONS-GENERATIONS_TAKE):
                population.append(x)
        assert(0.0 <= x <= 1.0)
        attractors = list(set(population))
        for x in attractors:
            a = int(r*WIDTH/(r2-r1))
            b = int(x*HEIGHT)

            nb = b-(x1*HEIGHT)
            nx = (x2-x1)*HEIGHT
            bb = nb/nx*HEIGHT
            img.put_pixel(a, bb, WHITE)
    img.save("img/feigenbaum_diagram_r1_{R1}_r2_{R2}_x1_{X1}_x2_{X2}.bmp".format(
        R1=r1, R2=r2, X1=x1, X2=x2))

diagram = ((0, 4, 0, 1, True), (2, 4, 0.5, 1, True), (3, 4, 0.75, 1, True), (3.5, 4, 0.875, 1, False))
for i, area in enumerate(diagram):
    feigenbaum_diagram(*area)
