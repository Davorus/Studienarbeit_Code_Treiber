import matplotlib.pyplot as plt
from collections import deque

""" Visualizer Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten und eine schöne Oberfläche bieten
"""

class Visualizer():
    def __init__(self):
        # visualized data settings
        self.que_alpha = []
        #self.que_alpha = deque(maxlen=40)

        self.que_beta = []
        #self.que_beta = deque(maxlen=40)

        self.max_data_length = 40 # boundary on how long the array should be

        # plot settings
        self.figure, (self.plot_alpha, self.plot_beta) = plt.subplots(2, 1)
        self.figure.canvas.manager.set_window_title("Live Darstellung - EEG Messung")
        self.figure.tight_layout()

        # title set alpha
        self.plot_alpha.set_title("Alpha Daten")

        # title set beta
        self.plot_beta.set_title("Beta Daten")
        
        # inverting x_axis, alpha
        self.plot_alpha.invert_xaxis()

        # inverting x_axis, beta
        self.plot_beta.invert_xaxis()
        
    def visualize(self, alpha, beta):
        # appending alpha array
        self.que_alpha.append(alpha)
        
        # appending beta array
        self.que_beta.append(beta)

        # plotting alpha data
        self.plot_alpha.plot(self.que_alpha, color="b")

        # plotting beta data
        self.plot_beta.plot(self.que_beta, color="r")

        # y axis range alpha
        self.plot_alpha.set_ylim(-1, 1)

        # y axis range beta
        self.plot_beta.set_ylim(-1, 1)

        # draw, pause and clear
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.pause(0.1)
