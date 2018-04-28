"""
Tomas Meszaros

L-Systems
"""

import random

from myturtle import Turtle


def l_system_draw(turtle, img_out, axiom, rules, interpretation, depth=2, debug=False):
    def expand(axiom, rules, interpretation, depth=2):
        word = axiom
        if debug:
            print(word)
        for _ in range(depth):
            cur = ""
            for ch in word:
                if ch in rules:
                    rule = rules[ch]
                    ## Determine weather we need to use stochastic rules
                    if type(rule) is list:
                        cur += rule[random.choice(range(len(rule)))]
                    else:
                        cur += rule
                else:
                    cur += ch
            word = cur
            if debug:
                print(word)
        return word

    expanded = expand(axiom, rules, interpretation, depth)
    turtle_position = list()
    for symbol in expanded:
        if symbol not in interpretation:
            continue
        fcn, by = interpretation[symbol]
        if fcn == "forward":
            turtle.forward(by)
        elif fcn == "right":
            if type(by) is list:
                turtle.right(by[random.choice(range(len(by)))])
            else:
                turtle.right(by)
        elif fcn == "left":
            if type(by) is list:
                turtle.left(by[random.choice(range(len(by)))])
            else:
                turtle.left(by)
        elif fcn == "stack":
            if by == "push":
                turtle_position.append((turtle.get_x(), turtle.get_y(), turtle.get_angle()))
            elif by == "pop":
                x, y, angle = turtle_position.pop()
                turtle.set_x(x)
                turtle.set_y(y)
                turtle.set_angle(angle)
            else:
                raise Exception("Error: wrong stack instruction", by)
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
#draw_koch_snowflake()

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
#draw_sierpinski_triange()

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
#draw_hilbert_curve()

def draw_basic_tree():
    turtle = Turtle(width=600, height=600, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "A"
    rules = {"A": "F[+A]-A", "F": "FF"}
    length = 1
    angle = 30
    interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
    depth = 9

    turtle.left(90)
    turtle.set_y(-300)
    l_system_draw(turtle, "img/basic_tree.svg", axiom, rules, interpretation, depth)
#draw_basic_tree()


def draw_fancy_tree_1():
    turtle = Turtle(width=500, height=800, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "F"
    rules = {"F": "F[+F]F[-F]F"}
    length = 3
    angle = 25.7
    interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
    depth = 5

    turtle.left(90)
    turtle.set_y(-400)
    l_system_draw(turtle, "img/fancy_tree_1.svg", axiom, rules, interpretation, depth)
#draw_fancy_tree_1()

def draw_fancy_tree_2():
    turtle = Turtle(width=700, height=1000, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "F"
    rules = {"F": "F[+FF]F[-FF]F"}
    length = 3
    angle = 25.7
    interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
    depth = 5

    turtle.left(90)
    turtle.set_y(-500)
    l_system_draw(turtle, "img/fancy_tree_2.svg", axiom, rules, interpretation, depth)
#draw_fancy_tree_2()

def draw_fancy_tree_3_stochastic():
    turtle = Turtle(width=800, height=1000, center_origin=True, show_borders_and_origin=False, animate=False, animation_speed=0.001)
    axiom = "F"
    rules = {"F": ["[+F]F[−F]", "F[+F]F", "F[-F]F"]}
    length = 5
    angle = [25, 30, 35]
    interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
    depth = 9

    turtle.left(90)
    turtle.set_y(-500)
    l_system_draw(turtle, "img/fancy_tree_3_stochastic.svg", axiom, rules, interpretation, depth, debug=True)
#draw_fancy_tree_3_stochastic()
