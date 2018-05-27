# Class 11

---

## Number maze

[code](code/number_maze.py)

```
    We have input:

     S2 1 1 3
      3 2 1 1
      2 1 1 2
      3 1 2 X

    where S is Start and X is End.
    We want to get from S to X, but we can make only N moves in any direction,
    where N is number on the current tile.

    Input is transformed, first by assigning each node unique id:

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

    in which, the path is found:

     [(0, 'S2'), (2, '1'), (3, '3'), (15, 'X')]
```

---

## Maze variations - Lamps connecting

[code](code/3_lamps.py)

```
1..#
.#2#
.#..
3..#

1oo#
o#2#
o#..
3..#
```

```
1..#.##
.#.#...
.....#2
#.##.#.
.....#.
.#3.##.

1..#.##
o#.#ooo
ooooo#2
#o##.#.
.oo..#.
.#3.##.
```
