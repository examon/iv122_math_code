"""
Tomas Meszaros

L-Systems
"""

from myturtle import Turtle


def l_system_draw(turtle, img_out, axiom, rules, interpretation, depth=2):
    def expand(axiom, rules, interpretation, depth=2):
        word = axiom
        #print(word)
        for _ in range(depth):
            cur = ""
            for ch in word:
                if ch in rules:
                    cur += rules[ch]
                else:
                    cur += ch
            word = cur
            #print(word)
        return word

    expanded = expand(axiom, rules, interpretation, depth)
    for symbol in expanded:
        if symbol not in interpretation:
            continue
        fcn, by = interpretation[symbol]
        if fcn == "forward":
            turtle.forward(by)
        elif fcn == "right":
            turtle.right(by)
        elif fcn == "left":
            turtle.left(by)
        else:
            raise Exception("Error: wrong instruction", fcn)
    turtle.save(img_out)

def draw_koch_snowflake():
    turtle = Turtle(width=1000, height=1000, center_origin=False, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "F--F--F"
    rules = {"F": "F+F--F+F"}
    interpretation = {"F": ("forward", 1), "+": ("right", 60), "-": ("left", 60)}
    depth = 6

    turtle.set_x(150)
    turtle.set_y(300)
    l_system_draw(turtle, "img/koch_snowflake.svg", axiom, rules, interpretation, depth)
draw_koch_snowflake()

def draw_sierpinski_triange():
    turtle = Turtle(width=1100, height=1000, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "B"
    rules = {"A": "B+A+B", "B": "A-B-A"}
    interpretation = {"A": ("forward", 4), "B": ("forward", 4), "+": ("right", 60), "-": ("left", 60)}
    depth = 8

    turtle.left(180)
    turtle.set_x(500)
    turtle.set_y(-500)
    l_system_draw(turtle, "img/sierpinski_triangle.svg", axiom, rules, interpretation, depth)
draw_sierpinski_triange()

def draw_hilbert_curve():
    turtle = Turtle(width=1000, height=1000, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "-L"
    rules = {"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"}
    length = 10
    interpretation = {"F": ("forward", length), "+": ("right", 90), "-": ("left", 90)}
    depth = 4

    turtle.left(90)
    turtle.set_x(400)
    turtle.set_y(-400)
    l_system_draw(turtle, "img/hilbert_curve.svg", axiom, rules, interpretation, depth)
draw_hilbert_curve()
