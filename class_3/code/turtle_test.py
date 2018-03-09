from myturtle import Turtle

# octagon
t = Turtle(center_origin=True, show_borders_and_origin=True)
sides = 5
length = 100
for _ in range(sides):
    t.left(360/sides)
    t.forward(length)
t.left(360/sides+360/sides/2)
# TODO: cos to find length
t.forward(100)

t.save("turtle_pentagram.svg")


"""
t2 = Turtle(center_origin=True, show_borders_and_origin=True)
for _ in range(4):
    t2.left(45)
    t2.forward(100)
t2.save("turtle_star.svg")
"""
