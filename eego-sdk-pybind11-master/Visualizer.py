import matplotlib as mplt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

""" Visualizer Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten und eine schöne Oberfläche bieten
"""

class Visualizer():
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def visualize(self, data):
        self.graph = self.ax.plot(data, color="g")[0]
        plt.ylim(0, 10)
        def update(frame):
            self.graph.set_xdata(data)
            self.graph.set_ydata(3)
            plt.xlim(data[1], data[0])
        anim = FuncAnimation(self.fig, update, frames=None)
        plt.show()
