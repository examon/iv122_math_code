"""
Tomas Meszaros

Clusters detection.

"""

import matplotlib.pyplot as plt
import numpy as np

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

def compute_and_plot(dataset, save_tag):
    x, y = get_x_y_from_data(dataset)
    plot = plt.figure()
    #plt.scatter(x, y, color='grey', marker='.')
    plt.plot(10, 10, 'ro')

    plt.savefig("img/clusters_detection_{TAG}.png".format(TAG=save_tag))

compute_and_plot("data/faithful.txt", save_tag="faithful")
#compute_and_plot("data/linreg.txt", save_tag="linreg")
