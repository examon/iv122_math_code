"""
Tomas Meszaros

Clusters detection.

Doc:
https://matplotlib.org/api/markers_api.html
https://matplotlib.org/2.0.2/api/colors_api.html

"""

import random
import math

import matplotlib.pyplot as plt
import numpy as np

from pprint import pprint as pp

COLOR_MARKERS = ['g', 'r', 'c', 'm']
YELLOW = 'y'
BLACK = 'k'
BLUE = 'b'
RED = 'r'
SQUARE_MARKER = 's'
PLUS_MARKER = '+'


def generate_data(filename, num=20, valmin=0, valmax=100):
    f = open(filename, 'w')
    for _ in range(num):
        f.write("%d %d\n" % (get_random(valmin, valmax), get_random(valmin, valmax)))
    f.close()

def get_x_y_from_data(data_file):
    """ Transform data from file to x,y vectors.
    """
    data = open(data_file)
    x = []
    y = []
    for pair in data.read().strip().split('\n'):
        px, py = pair.split(' ')
        x.append(float(px))
        y.append(float(py))
    return (x, y)

def get_random(x, y):
    return random.choice(range(int(x), int(y)))

def plot_data(x, y, marker):
    assert len(x) == len(y)
    for i, _ in enumerate(x):
        plt.plot(x[i], y[i], marker)

def points_distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def _get_new_center(points):
    new_x = 0
    new_y = 0
    for _, val in enumerate(points):
        new_x += val[0]
        new_y += val[1]
    return (new_x/len(points), new_y/len(points))

def _plot_centers(plot, centers):
    for i, center in enumerate(centers):
        plot.plot(center[0], center[1], BLACK+SQUARE_MARKER)


def _get_random_centers(x, y, num_of_centers):
    centers = []
    for _ in range(num_of_centers):
        cx = get_random(min(x), max(x))
        cy = get_random(min(y), max(y))
        centers.append([cx, cy])
    return centers

def compute_and_plot(dataset, num_clusters, iterations, tag, img_size=4, points_markers=PLUS_MARKER):
    x, y = get_x_y_from_data(dataset)
    #x = list(map(lambda i: i*20, x))
    assert len(x) == len(y)

    centers = _get_random_centers(x, y, num_clusters)

    for iteration in range(iterations):
        ## Plot initial points and centers
        plt.figure()
        plt.figure(figsize=(img_size, img_size))
        _plot_centers(plt, centers)
        plot_data(x, y, marker=YELLOW+points_markers)
        plt.savefig("img/clusters_detection_init_{ITER}_{TAG}.png".format(ITER=iteration, TAG=tag))

        ## Categorize points to current centers
        categorized_points = []
        for i in range(num_clusters):
            categorized_points.append([])
        for i, _ in enumerate(x):
            best_fit = {"best_center": None, "distance": None}
            point = (x[i], y[i])
            for center_idx, center in enumerate(centers):
                dist = points_distance(point[0], point[1], center[0], center[1])
                if best_fit["best_center"] is None or dist < best_fit["distance"]:
                    best_fit["best_center"] = center_idx
                    best_fit["distance"] = dist
            categorized_points[best_fit["best_center"]].append(point)

        ## Plot categorized points
        plt.figure()
        plt.figure(figsize=(img_size, img_size))
        _plot_centers(plt, centers)
        for i, points in enumerate(categorized_points):
            if len(points) > 0:
                a, b = zip(*points)
                plot_data(a, b, marker=COLOR_MARKERS[i]+points_markers)
        plt.savefig("img/clusters_detection_after_{ITER}_{TAG}.png".format(ITER=iteration, TAG=tag))

        ## Compute new centers
        for i, points in enumerate(categorized_points):
            if len(points) > 0:
                cx, cy = _get_new_center(points)
                print(cx, cy)
                centers[i] = [cx, cy]

#generate_data("data/test.txt", num=300)
compute_and_plot(dataset="data/test.txt", num_clusters=4, tag="test", iterations=4, points_markers=PLUS_MARKER)
compute_and_plot(dataset="data/linreg.txt", num_clusters=2, tag="linreg", iterations=3, points_markers=PLUS_MARKER)
compute_and_plot(dataset="data/faithful.txt", num_clusters=2, tag="faithful", iterations=3, points_markers=PLUS_MARKER)
