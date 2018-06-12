"""
Tomas Meszaros

Solves number maze puzzle.

Input is:

S2 4 4 3 3
 2 3 3 2 3
 3 2 3 1 3
 2 2 3 2 1
 1 4 4 4 X

Where S is Start and X is End.
We want to get from S to X, but we can make only N moves in any direction, where
N is number on the current tile.
"""

import dijkstar

_DEBUG = False

def load_maze(txt_file):
    """ Loads maze from @txt_file.
    Assigns each node unique @node_id, because node names are not unique.
    """
    with open(txt_file) as f:
        maze = f.read()
        rows = maze.strip().split('\n')
        out = []
        node_id = 0
        for row in rows:
            new_row = []
            for node in row.strip().split():
                new_row.append((node_id, node))
                node_id += 1
            out.append(new_row)
        return out

def solve_maze(maze_txt):
    """ Solves number maze and prints results.

    Transforms input into graph and uses dijkstar library to get shortest path.

    Input:

    S2 1 1 3
     3 2 1 1
     2 1 1 2
     3 1 2 X

    is transformed by first assigning each node unique id:

     [[(0, 'S2'), (1, '1'), (2, '1'), (3, '3')],
      [(4, '3'), (5, '2'), (6, '1'), (7, '1')],
      [(8, '2'), (9, '1'), (10, '1'), (11, '2')],
      [(12, '3'), (13, '1'), (14, '2'), (15, 'X')]]

    and then converted to directed graph:

    (0, {2: {'cost': 1}, 8: {'cost': 1}})
    (1, {0: {'cost': 1}, 2: {'cost': 1}, 5: {'cost': 1}})
    (2, {1: {'cost': 1}, 3: {'cost': 1}, 6: {'cost': 1}})
    (3, {0: {'cost': 1}, 15: {'cost': 1}})
    (4, {7: {'cost': 1}})
    (5, {7: {'cost': 1}, 13: {'cost': 1}})
    (6, {2: {'cost': 1}, 5: {'cost': 1}, 7: {'cost': 1}, 10: {'cost': 1}})
    (7, {3: {'cost': 1}, 6: {'cost': 1}, 11: {'cost': 1}})
    (8, {0: {'cost': 1}, 10: {'cost': 1}})
    (9, {5: {'cost': 1}, 8: {'cost': 1}, 10: {'cost': 1}, 13: {'cost': 1}})
    (10, {6: {'cost': 1}, 9: {'cost': 1}, 11: {'cost': 1}, 14: {'cost': 1}})
    (11, {3: {'cost': 1}, 9: {'cost': 1}})
    (12, {0: {'cost': 1}, 15: {'cost': 1}})
    (13, {9: {'cost': 1}, 12: {'cost': 1}, 14: {'cost': 1}})
    (14, {6: {'cost': 1}, 12: {'cost': 1}})

    in which, the path is found.

    """
    maze = load_maze(maze_txt)
    graph = dijkstar.Graph()
    start = maze[0][0][0]
    end = maze[-1][-1][0]
    from pprint import pprint as pp
    pp(maze)

    # Transform input into graph
    for i, row in enumerate(maze):
        for j, node in enumerate(row):
            if node[1] == 'X':
                # stop when we hit the end#
                continue
            elif node[1] == "S2":
                number = 2
            else:
                number = int(node[1])
            # right
            if j+number < len(row):
                graph.add_edge(node[0], row[j+number][0], {"cost": 1})
            # left
            if j-number >= 0:
                graph.add_edge(node[0], row[j-number][0], {"cost": 1})
            # top
            if i-number >= 0:
                graph.add_edge(node[0], maze[i-number][j][0], {"cost": 1})
            # down
            if i+number < len(maze):
                graph.add_edge(node[0], maze[i+number][j][0], {"cost": 1})

    if _DEBUG:
        for i in graph.items():
            pp(i)

    cost_func = lambda u, v, e, prev_e: e['cost']
    result = dijkstar.find_path(graph, start, end, cost_func=cost_func)
    nodes_ids = result.nodes

    # Get final path
    final_path = []
    for node_id in nodes_ids:
        for row in maze:
            for i, node in row:
                if node_id == i:
                    final_path.append((i, node))
    return final_path

print(solve_maze("number_maze_4x4.txt"))
print(solve_maze("number_maze_5x5.txt"))
