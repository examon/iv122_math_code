"""
Tomas Meszaros

Generates maze that looks like pyramid.

Maze algorithms:
- http://www.astrolog.org/labyrnth/algrithm.htm
"""

import random
import math

import dijkstar
from svglib import SVGImage

_DEBUG = False

def make_graph(pyramid_level):
    """ Makes graph where nodes are rooms and edges are walls.
    @pyramid_level is number of pyramid levels, starts from 0!

    Graph will looks like this. Nodes are numbered.

            1
            |
        2---3---4
        |       |
    5---6---7---8---9

    """
    graph = dijkstar.Graph()
    cost = {"cost": 1}

    # give each node ID, from top to bottom and left to right
    """
    make horizontal connections in graph
    e.g. for pyramid_level == 2

            1

        2---3---4

    5---6---7---8---9
    """
    current_node_id = 1
    for level in range(pyramid_level+1):
        nodes_per_level = level*2+1
        for node in range(nodes_per_level):
            if node < nodes_per_level-1:
                a = current_node_id
                b = current_node_id+1
                if _DEBUG:
                    print("connecting:", a, b)
                    print("connecting:", b, a)
                graph.add_edge(a, b, cost)
                graph.add_edge(b, a, cost)
            current_node_id += 1
    """
    make vertical connections in graph
    e.g. for pyramid_level == 2

            1
            |
        2   3   4
        |       |
    5   6   7   8   9
    """
    next_node_offset = 2 # goes up by N+2 per level
    current_node_id = 1

    for level in range(pyramid_level):
        nodes_per_level = level*2+1
        if _DEBUG:
            print("nodes_per_level:", nodes_per_level)
            print("next_node_offset:", next_node_offset)
            print("current_node_id:", current_node_id)
        for node_id in range(current_node_id, current_node_id+nodes_per_level, 2):
            a = node_id
            b = node_id+next_node_offset
            if _DEBUG:
                print("node_id:", node_id)
                print("connecting:", a, b)
                print("connecting:", b, a)
            graph.add_edge(a, b, cost)
            graph.add_edge(b, a, cost)
        next_node_offset += 2
        current_node_id += nodes_per_level

    return graph

def generate_maze(graph, start=1):
    """ Runs DFS and determines which walls to destroy.
    Returns list of destroyed walls between rooms.
    """
    visited = []
    no_walls = []
    stack = []
    START = start # node id
    stack.append(START)
    visited.append(START)

    while len(stack) > 0:
        current = stack.pop()
        adj = list(graph[current].keys())
        if _DEBUG:
            print(current, adj)
        # shuffle neighbours, so generation is randomized
        random.shuffle(adj)
        for neighbour in adj:
            if neighbour in visited:
                continue
            no_walls.append((current, neighbour))
            no_walls.append((neighbour, current))
            visited.append(neighbour)
            stack.append(neighbour)
            if _DEBUG:
                print("no_walls:", no_walls)
                print("visited:", visited)
                print("stack:", stack)
    return no_walls

def draw_maze(img_file, no_wallss, img_size=400, animate=True, levels=4, side_length=50):
    """ Draws maze.
    """
    def draw_triangle(img, x=0, y=0, side_length=50, drop_ab=False, drop_bc=False, drop_ca=False):
        """ Draws triangle with side @side_length.
        Bottom left corner is at the @x,@y coordinates.
        Able to not draw specific side of triangle by setting @drop_* to True.
        """
        ax = x
        ay = y
        bx = x+side_length
        by = y
        cx = x+side_length/2
        cy = y-(math.sqrt(3)/2)*side_length
        if not drop_ab:
            img.add_line(ax, ay, bx, by)
        if not drop_bc:
            img.add_line(bx, by, cx, cy)
        if not drop_ca:
            img.add_line(cx, cy, ax, ay)

    img = SVGImage(img_size, img_size, center_origin=False, show_borders_and_origin=False, animate=animate, animation_speed=0.05)
    x = img_size/2-side_length/2
    y = (math.sqrt(3)/2)*side_length

    current_node_id = 1 # node id of the triangle we are drawing

    for level in range(levels+1):
        current_x = x
        for triangle in range(level+1):
            # draw only walls that are not in @no_walls
            drop_ab, drop_bc, drop_ca = False, False, False
            for wall in no_walls:
                node_id, neighbor_id = wall
                if node_id == current_node_id:
                    if node_id == neighbor_id+1:
                        # dropping wall to the left (ac)
                        drop_ca = True
                    if node_id == neighbor_id-1:
                        # dropping wall to the right (bc)
                        drop_bc = True
                    if node_id+1 < neighbor_id:
                        # dropping wall to the bottom (ab)
                        drop_ab = True
            draw_triangle(img, x=current_x, y=y, side_length=side_length, drop_ab=drop_ab, drop_bc=drop_bc, drop_ca=drop_ca)
            current_x += side_length
            if triangle < level:
                current_node_id += 2
        x -= side_length/2
        y += (math.sqrt(3)/2)*side_length
        current_node_id += 1

    img.save(img_file)


graph = make_graph(10)
no_walls = generate_maze(graph, start=1)
draw_maze("img/maze_pyramid_10.svg", no_walls, side_length=35, animate=False, levels=10)
draw_maze("img/maze_pyramid_animate_10.svg", no_walls, side_length=35, animate=True, levels=10)

graph = make_graph(100)
no_walls = generate_maze(graph, start=1)
draw_maze("img/maze_pyramid_100.svg", no_walls, img_size=800, side_length=7, animate=False, levels=100)
draw_maze("img/maze_pyramid_animate_100.svg", no_walls, img_size=800, side_length=7, animate=True, levels=100)
