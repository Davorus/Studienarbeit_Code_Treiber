import matplotlib as mplt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from collections import deque

""" Visualizer Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten und eine schöne Oberfläche bieten
"""

class Visualizer():
    def __init__(self):
        # visualized data settings
        self.que: list = []
        self.que = deque(maxlen=40)

        # plot settings
        self.plot = plt
        self.plot.figure("Live Darstellung - EEG Messung")

    def visualize(self, data):
        # appending data
        self.que.append(data)
        # inverting x_axis, newest value has to be on the left
        self.plot.gca().invert_xaxis()

        # plotting
        self.plot.plot(self.que)
        self.plot.scatter(range(len(self.que)), self.que)

        # y axis range
        self.plot.ylim(-1, 1)

        # draw, pause and clear
        self.plot.draw()
        self.plot.pause(0.1)
        self.plot.clf()
