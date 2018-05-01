"""
Tomas Meszaros

Linear regression.

https://en.wikipedia.org/wiki/Linear_regression

TODO:
- generate simulated data
- make some nice graphs using gradient descent
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_line(plt, x, a, b, color=(1, 0, 0)):
    """ Draw line
    """
    line_x = np.arange(min(x), max(x), 0.01)
    line_y = a*line_x+b
    plt.plot(line_x, line_y, color=(color[0], color[1], color[2]))

def formula(x, y):
    """ Compute a,b for y = ax + b with the classic formula.
    """
    ## Compute a
    n = len(x)
    a1 = 0
    for i, val in enumerate(x):
        a1 += x[i]*y[i]
    a2 = sum(x)
    a3 = sum(y)
    a4 = 0
    for i, val in enumerate(x):
        a4 += x[i]*x[i]
    a5 = sum(x)**2
    a = (n*a1-a2*a3)/(n*a4-a5)

    ## Compute b
    b1 = sum(y)
    b2 = sum(x)
    b = (1/n)*(b1-a*b2)

    return (a, b)

def gradient_descent(x, y, a_init=0, b_init=0, learning_rate=0.0005, iterations=1000):
    """ Compute a,b for y = ax + b using gradient descent.
    """
    def _new_ab(a, b, x, y, rate):
        a_grad, b_grad = 0, 0
        for i, _ in enumerate(x):
            a_grad += -(x[i] * (y[i] - ((a * x[i]) + b)))
            b_grad += -(y[i] - ((a*x[i]) + b))
        b = b-b_grad*rate
        a = a-a_grad*rate
        return (a, b)

    a, b = a_init, b_init
    for _ in range(iterations):
        a, b = _new_ab(a, b, x, y, rate=learning_rate)
    return (a, b)

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
    plt.scatter(x, y, color='grey', marker='.')

    lines = 8
    for i in range(1, lines+1):
        na, nb = gradient_descent(x, y, iterations=(2**i))
        print("a: %f, b: %f, iterations: %f" % (na, nb, 2**i))
        plot_line(plt, x, na, nb, color=(float(i/lines), 0, 0))

    a, b = formula(x, y)
    plot_line(plt, x, a, b, color=(0, 0, 1))
    print("a: %f, b: %f" % (a, b))
    plt.savefig("img/linear_regression_{TAG}.png".format(TAG=save_tag))

compute_and_plot("data/faithful.txt", save_tag="faithful")
compute_and_plot("data/linreg.txt", save_tag="linreg")
