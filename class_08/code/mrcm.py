"""
Tomas Meszaros

Multiple Reduction Copy Machine
"""

import lingebra

from svglib import SVGImage
from pprint import pprint as pp

img = SVGImage(800, 800, center_origin=True, show_borders_and_origin=True, animate=False, animation_speed=0.01)

a = {"lines": [[0,0,100,0], [100,0,100,100], [100,100,0,100], [0,100,0,0]],
     "attractor": [0, 0]
    }
b = {"lines": [[100,100,200,100], [200,100,200,200], [200,200,100,200], [100,200,100,100]],
     "attractor": [100, 100]
    }

group_set = []
init_group = [a, b]
group_set.append(init_group)
sx = 0.9
sy = 0.9
iterations = 30

pp(group_set)
for _ in range(iterations):
    new_group_set = []
    while len(group_set) > 0:
        group = group_set.pop()
        new_group = []
        for item in group:
            new_item = {"lines": [], "attractor": None}
            for line in item["lines"]:
                img.add_line(*line)
                x1, y1, x2, y2 = line
                # TODO: second retangle is scaling by different point
                x1, y1 = lingebra.scale((x1, y1), sx, sy, item["attractor"])
                x2, y2 = lingebra.scale((x2, y2), sx, sy, item["attractor"])
                new_line = [x1, y1, x2, y2]
                new_item["lines"].append(new_line) ## set the new lines
            new_item["attractor"] = item["attractor"] ## keep the original attractor
            new_group.append(new_item)
        new_group_set.append(new_group)
    group_set = new_group_set
pp(group_set)



img.save("img/mrcm_test.svg")
