import numpy as np
import matplotlib.pyplot as plt

NUM_OF_POINTS = 300
NUM_OF_REPEATS = 2


def uniform_distr():
    for i in range(NUM_OF_REPEATS):
        random_x = np.random.uniform(-1, 1, NUM_OF_POINTS)
        random_y = np.random.uniform(0, 5, NUM_OF_POINTS)
        #plt.plot(random_x, random_y, "ro")
        plt.scatter(random_x, random_y, linewidths=0.5)
        plt.show()


def guassian_distr():
    for i in range(NUM_OF_REPEATS):
        points = np.random.normal(loc=(1, 1), scale=2, size=(NUM_OF_POINTS, 2))
        plt.scatter(points[:, 0], points[:, 1], linewidths=0.05)
        plt.show()


def three_guassian_distr():
    for i in range(NUM_OF_REPEATS):
        all_points = np.zeros((NUM_OF_POINTS, 2))
        for i in range(1, 4):
            all_points[100 * (i - 1):100 * i, :] = np.random.normal(loc=(-i, i), scale=2 * i, size=(100, 2))
        plt.scatter(all_points[:, 0], all_points[:, 1], linewidths=0.05)
        plt.show()


def circle_ring():
    for i in range(NUM_OF_REPEATS):
        radius = np.random.uniform(0, 1, NUM_OF_POINTS)
        angle = np.random.uniform(0, 2 * np.pi, NUM_OF_POINTS)
        radius[0:200] += 2
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        plt.scatter(x, y, linewidths=0.05)
        plt.show()


def first_letters():
    # -----A------
    for i in range(NUM_OF_REPEATS):

        x = []
        y = []
        x1 = np.random.uniform(0, 5, (60, 1))
        x2 = np.random.uniform(5, 10, (60, 1))
        x3 = np.random.uniform(2, 8, (30, 1))
        y1 = 5 * x1
        y2 = -5 * x2 + 50
        y3 = 0 * x3 + 10
        x[0:59], x[60:119], x[120:149] = x1, x2, x3
        y[0:59], y[60:119], y[120:149] = y1, y2, y3

        # -----N------
        x1 = np.random.uniform(12, 12, (50, 1))
        y1 = np.random.uniform(0, 25, (50, 1))
        x2 = np.random.uniform(12, 20, (50, 1))
        y2 = -3 * x2 + 60
        x3 = np.random.uniform(20, 20, (50, 1))
        y3 = y1
        x[150:199], x[200:249], x[250:299] = x1, x2, x3
        y[150:199], y[200:249], y[250:299] = y1, y2, y3

        plt.scatter(x, y, linewidths=0.5)
        plt.show()

first_letters()