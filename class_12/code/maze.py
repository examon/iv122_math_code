"""
Tomas Meszaros

Generates maze.

Maze algorithms:
- http://www.astrolog.org/labyrnth/algrithm.htm
"""

import random

import dijkstar
from svglib import SVGImage


def make_graph(maze_side_length):
    """ Makes graph where nodes are rooms and edges are walls.
    @maze_side_length is number of rooms of the maze in one direction.

    """
    graph = dijkstar.Graph()
    cost = {"cost": 1}
    for row_id in range(maze_side_length):
        for room_id in range(maze_side_length):
            # add edge: current->right
            if room_id < maze_side_length-1:
                graph.add_edge((row_id, room_id), (row_id, room_id+1), cost)
            # add edge: current->left
            if room_id >= 1:
                graph.add_edge((row_id, room_id), (row_id, room_id-1), cost)
            # add edge: current->bottom
            if row_id < maze_side_length-1:
                graph.add_edge((row_id, room_id), (row_id+1, room_id), cost)
            # add edge: current->top
            if row_id >= 1:
                graph.add_edge((row_id, room_id), (row_id-1, room_id), cost)
    return graph

def generate_maze(graph):
    """ Runs DFS and determines which walls to destroy.
    Returns list of destroyed walls between rooms.
    """
    visited = []
    no_wall = []
    stack = []
    START = (0, 0) # upper top
    stack.append(START)
    visited.append(START)

    while len(stack) > 0:
        current = stack.pop()
        adj = list(graph[current].keys())
        # shuffle neighbours, so generation is randomized
        random.shuffle(adj)
        for neighbour in adj:
            if neighbour in visited:
                continue
            no_wall.append((current, neighbour))
            visited.append(neighbour)
            stack.append(neighbour)
    return no_wall

def draw_maze(filename, maze_side, missing_walls, show_start_end=True, animate=False, img_size=500, line_width=2):
    """ Draws maze into svg image.
    Checks if there should not be missing wall in @missing_walls.
    """
    size = img_size
    width = line_width
    img = SVGImage(size, size, center_origin=False, show_borders_and_origin=False, animate=animate, animation_speed=0.05)

    # draw borders
    img.add_line(0, 0, 0, size, width=2*width)
    img.add_line(0, size, size, size, width=2*width)
    img.add_line(size, size, size, 0, width=2*width)
    img.add_line(size, 0, 0, 0, width=2*width)

    # draw start and end
    # start is always upper-top and end always bottom-right
    if show_start_end:
        img.add_circle(size/maze_side/2, size/maze_side/2, size/maze_side/4, fill="green")
        img.add_circle(maze_side*(size/maze_side)-(size/maze_side/2), maze_side*(size/maze_side)-(size/maze_side/2), size/maze_side/4, fill="red")

    # draw vertical walls
    for row in range(maze_side):
        for col in range(maze_side-1):
            current_wall = ((row, col), (row, col+1))
            if current_wall in missing_walls or current_wall[::-1] in missing_walls:
                continue
            x0 = (col+1)*(size/maze_side)
            y0 = row*(size/maze_side)
            x1 = x0
            y1 = (row+1)*(size/maze_side)
            img.add_line(x0, y0, x1, y1, width=width)

    # draw horizontal walls
    for row in range(maze_side-1):
        for col in range(maze_side):
            current_wall = ((row, col), (row+1, col))
            if current_wall in missing_walls or current_wall[::-1] in missing_walls:
                continue
            x0 = col*(size/maze_side)
            y0 = (row+1)*(size/maze_side)
            x1 = (col+1)*(size/maze_side)
            y1 = y0
            img.add_line(x0, y0, x1, y1, width=width)
    img.save(filename)

MAZE_SIDE_LENGTH = 10
graph = make_graph(MAZE_SIDE_LENGTH)
no_wall = generate_maze(graph)
draw_maze(filename="img/rectangular_perfect.svg", maze_side=MAZE_SIDE_LENGTH, missing_walls=no_wall, show_start_end=True, animate=False, img_size=400, line_width=2)
draw_maze(filename="img/rectangular_perfect_animated.svg", maze_side=MAZE_SIDE_LENGTH, missing_walls=no_wall, show_start_end=False, animate=True, img_size=400, line_width=2)

MAZE_SIDE_LENGTH = 50
graph = make_graph(MAZE_SIDE_LENGTH)
no_wall = generate_maze(graph)
draw_maze(filename="img/rectangular_perfect_50.svg", maze_side=MAZE_SIDE_LENGTH, missing_walls=no_wall, show_start_end=False, animate=False, img_size=400, line_width=2)

MAZE_SIDE_LENGTH = 100
graph = make_graph(MAZE_SIDE_LENGTH)
no_wall = generate_maze(graph)
draw_maze(filename="img/rectangular_perfect_100.svg", maze_side=MAZE_SIDE_LENGTH, missing_walls=no_wall, show_start_end=False, animate=False, img_size=400, line_width=2)

MAZE_SIDE_LENGTH = 400
graph = make_graph(MAZE_SIDE_LENGTH)
no_wall = generate_maze(graph)
draw_maze(filename="img/rectangular_perfect_400.svg", maze_side=MAZE_SIDE_LENGTH, missing_walls=no_wall, show_start_end=False, animate=False, img_size=800, line_width=1)
