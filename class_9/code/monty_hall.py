"""
Tomas Meszaros

Monty Hall Problem Simulation

Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors,
opens another door, say No. 3, which has a goat. He then says to you,
"Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
"""

import random

def generate_problem():
    doors = ["goat"]*3
    doors[random.choice([0, 1, 2])] = "car"
    return doors

def run(strategy, iterations=1000):
    win = 0
    nowin = 0
    for _ in range(iterations):
        if strategy() == True:
            win += 1
        else:
            nowin += 1
    print("strategy: {STRATEGY}, win chance: {WIN_CHANCE}".format(STRATEGY=strategy.__name__, WIN_CHANCE=win/iterations))

def not_changing_pick():
    """ Player does not change his pick.
    """
    doors = generate_problem()
    my_pick = random.choice([0, 1, 2])

    # check what is behind the door
    if doors[my_pick] == "car":
        return True
    return False

def changing_pick():
    """ Player changes his pick after host shows him the door with goat.
    """
    doors = generate_problem()
    my_pick = random.choice([0, 1, 2])

    # host picks the door that has the goat
    host_pick = None
    for i, _ in enumerate(doors):
        if i != my_pick and doors[i] == "goat":
            host_pick = i
            break

    # player picks the unopened door
    for i, _ in enumerate(doors):
        if i != my_pick and i != host_pick:
            my_pick = i
            break

    # check what is behind the door
    if doors[my_pick] == "car":
        return True
    return False

def random_change_pick():
    """ Player acts randomly. He sometimes changes his pick and sometimes not.
    """
    if random.choice([0, 1]) == 0:
        return not_changing_pick()
    else:
        return changing_pick()

run(not_changing_pick)
run(changing_pick)
run(random_change_pick)
