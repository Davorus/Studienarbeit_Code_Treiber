import matplotlib as mplt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from collections import deque

""" Visualizer Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten und eine schöne Oberfläche bieten
"""

class Visualizer():
    def __init__(self):
        self.que: list = []
        self.que = deque(maxlen=40)

    def visualize(self, data):
        # appending data
        self.que.append(data)

        # plotting
        plt.plot(self.que)
        plt.scatter(range(len(self.que)), self.que)

        # y axis range
        plt.ylim(-1, 1)

        # draw, pause and clear
        plt.draw()
        plt.pause(0.1)
        plt.clf()
