"""
Tomas Meszaros

Solves maze where we want to connect 3 lamps with the shortest cable.
"""

import dijkstar

from pprint import pprint as pp

WALL = '#'
FREE_SPACE = '.'
CABLE = 'o'

def load_maze(file_path):
    """ Loads maze from file into 2D array. Assigns each node unique id.
    """
    with open(file_path) as f:
        rows = f.read().split()
        data = []
        node_id = 0
        for row in rows:
            new_row = []
            for node in row:
                new_row.append((node_id, node))
                node_id += 1
            data.append(new_row)
        return data

def maze_to_graph(maze):
    """ Transforms input into graph.
    """
    graph = dijkstar.Graph()

    for i, row in enumerate(maze):
        for j, node in enumerate(row):
            node_id, node_item = node
            cost = {"cost": 1}

            # skip walls, we want only empty corridors and lamps
            if node_item == WALL:
                continue
            # right
            if j < len(row)-1 and row[j+1][1] != WALL:
                graph.add_edge(node_id, row[j+1][0], cost)
            # left
            if j > 0 and row[j-1][1] != WALL:
                graph.add_edge(node_id, row[j-1][0], cost)
            # down
            if i+1 < len(maze) and maze[i+1][j][1] != WALL:
                graph.add_edge(node_id, maze[i+1][j][0], cost)
            # up
            if i > 0 and maze[i-1][j][1] != WALL:
                graph.add_edge(node_id, maze[i-1][j][0], cost)
    return graph

def find_path(graph, a, b):
    """ Finds shortest path from @a to @b in @graph and returns it in a list.
    """
    cost_func = lambda u, v, e, prev_e: e['cost']
    result = dijkstar.find_path(graph, a, b, cost_func=cost_func)
    return result.nodes

def get_lamps(maze):
    """ Finds lamps in the @maze and returns their IDs in a list.
    """
    lamps = []
    for row in maze:
        for node_id, node in row:
            if node != WALL and node != FREE_SPACE:
                lamps.append(node_id)
    return lamps

def find_shortest_cable(graph, lamps):
    """ Finds shortest cable and returns the position and center.
    """
    results = {}
    for node_id, edges in graph.items():
        paths = set()
        for lamp_id in lamps:
            for node in find_path(graph, node_id, lamp_id):
                paths.add(node)
        results[node_id] = (len(paths), paths)

    shortest_id = None
    for result_id in results.keys():
        if shortest_id is None or results[result_id][0] < results[shortest_id][0]:
            shortest_id = result_id
    return results[shortest_id][1]


def print_shortest_cable(maze_file):
    maze = load_maze(maze_file)
    graph = maze_to_graph(maze)
    lamps = get_lamps(maze)
    cable = find_shortest_cable(graph, lamps)

    # print input
    for row in maze:
        for node_id, node in row:
            print(node, end='')
        print()
    print()

    # print output (with cable)
    for row in maze:
        for node_id, node in row:
            if node_id in cable and node_id not in lamps:
                print(CABLE, end='')
            else:
                print(node, end='')
        print()
    print()

print_shortest_cable("3_lamps_small.txt")
print_shortest_cable("3_lamps.txt")
