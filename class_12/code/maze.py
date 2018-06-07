"""
Tomas Meszaros

Generates maze.
"""

import random
from pprint import pprint as pp

import dijkstar
from svglib import SVGImage

WALL = '#'
FREE_SPACE = '.'
ON_STACK = '*'
START = '1'
END = '2'
SIDE = 10
_START = (0, 0)
_END = (SIDE-1, SIDE-1)
_DEBUG = False

def print_maze(maze):
    for row in maze:
        for item in row:
            print(item+' ', end='')
        print()
    print()

# Make maze with full of walls
maze = []
for _ in range(SIDE):
    row = []
    for _ in range(SIDE):
        row.append(WALL)
    maze.append(row)
maze[0][0] = START
maze[SIDE-1][SIDE-1] = END
if _DEBUG:
    print_maze(maze)

# Convert maze to graph
graph = dijkstar.Graph()
cost = {"cost": 1}
for row_id in range(len(maze)):
    for room_id in range(len(maze[0])):
        # add edge: current->right
        if room_id < SIDE-1:
            graph.add_edge((row_id, room_id), (row_id, room_id+1), cost)
        # add edge: current->left
        if room_id >= 1:
            graph.add_edge((row_id, room_id), (row_id, room_id-1), cost)
        # add edge: current->bottom
        if row_id < SIDE-1:
            graph.add_edge((row_id, room_id), (row_id+1, room_id), cost)
        # add edge: current->top
        if row_id >= 1:
            graph.add_edge((row_id, room_id), (row_id-1, room_id), cost)

if _DEBUG:
    for i in graph.items():
        pp(i)
    print('----')

# Run DFS and determine which walls to destroy
visited = []
no_wall = []
stack = []
stack.append(_START)
visited.append(_START)

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
        if _DEBUG == True:
            print("visited:", visited)
            print("stack:", stack)
            print("no_wall:", no_wall)
            print("current:", current)
            print()

def draw_maze(filename, maze_side, missing_walls, show_start_end=True, animate=False, img_size=500, line_width=2):
    size = img_size
    width = line_width
    img = SVGImage(size, size, center_origin=False, show_borders_and_origin=False, animate=animate, animation_speed=0.05)

    # draw borders
    img.add_line(0, 0, 0, size, width=2*width)
    img.add_line(0, size, size, size, width=2*width)
    img.add_line(size, size, size, 0, width=2*width)
    img.add_line(size, 0, 0, 0, width=2*width)

    # draw start and end
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

draw_maze(filename="img/test.svg", maze_side=SIDE, missing_walls=no_wall, show_start_end=True, animate=False, img_size=400, line_width=2)
draw_maze(filename="img/test_animated.svg", maze_side=SIDE, missing_walls=no_wall, show_start_end=False, animate=True, img_size=400, line_width=2)
