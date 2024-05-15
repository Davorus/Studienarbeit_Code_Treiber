import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

""" Visualizer Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten und eine schöne Oberfläche bieten
"""

class Visualizer():
    def __init__(self):
        # visualized alpha que
        self.que_alpha = []

        # visualized bet que
        self.que_beta = []

        # boundary on how long the array should be
        self.max_data_length = 40 

        # plot settings
        self.figure, (self.plot_alpha, self.plot_beta) = plt.subplots(2, 1)
        self.figure.canvas.manager.set_window_title("Live Darstellung - EEG Messung")
        self.figure.tight_layout()
        self.figure.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

    def waterfall_3D_plot(self):
        pass

    def show_plot(self):
        """
        Should show the whole plot with a waterfall diagram
        """
        # clear previous plots
        self.plot_alpha.clear()
        self.plot_beta.clear()

        # plot all data
        self.plot_alpha.plot(self.que_alpha, color='b')
        self.plot_beta.plot(self.que_beta, color='r')

        # y axis range for alpha subplot
        self.plot_alpha.set_ylim(-1, 1)

        # y axis range for beta subplot
        self.plot_beta.set_ylim(-1, 1)

        # inverting x_axis, alpha
        self.plot_alpha.invert_xaxis()

        # inverting x_axis, beta
        self.plot_beta.invert_xaxis()

        # draw and pause
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.show()
        
    def visualize(self, alpha: float, beta: float, data_number: int):
        """
        1. Check for array length, if it gets too long the plot-process will turn out too slow
        """
        # appending alpha array
        if len(self.que_alpha) > self.max_data_length:
            self.que_alpha.pop(0)
            self.que_alpha.append(alpha)
        else:
            self.que_alpha.append(alpha)
        
        # appending beta array
        if len(self.que_beta) > self.max_data_length:
            self.que_beta.pop(0)
            self.que_beta.append(beta)
        else:
            self.que_beta.append(beta)
        
        """
        2. Clear the subplots before drawing on them, they have to be reset with the data representation as it bugs then
        """
        # clear plot alpha
        self.plot_alpha.clear()

        # clear plot alpha
        self.plot_beta.clear()
        
        """
        3. Settings for the subplots
        """
        # inverting x_axis, alpha
        self.plot_alpha.invert_xaxis()

        # inverting x_axis, beta
        self.plot_beta.invert_xaxis()

        # title set alpha
        self.plot_alpha.set_title("Alpha Daten")

        # title set beta
        self.plot_beta.set_title("Beta Daten")

        # y axis range alpha
        self.plot_alpha.set_ylim(-1, 1)

        # y axis range beta
        self.plot_beta.set_ylim(-1, 1)

        # # set x axis ticks
        # if data_number <= 40:
        #     x_ticks = np.arange(0, data_number, 1)
        #     x_labels = [f"{x}" for x in x_ticks]
        # else:
        #     x_ticks = np.arange(data_number-40, data_number, 1)
        #     x_labels = [f"{x}" for x in x_ticks]
        # self.plot_alpha.set_xticks(x_ticks, labels=x_labels)
        # self.plot_beta.set_xticks(x_ticks, labels=x_labels)

        """
        4. Now let it plot
        """
        # plotting alpha data
        self.plot_alpha.plot(self.que_alpha, color="b")

        # plotting beta data
        self.plot_beta.plot(self.que_beta, color="r")

        """ 
        5. At lastly it shall draw on its canvas
        """
        # draw, pause and clear
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.pause(0.1)

    def save_plot(self):
        # save plot as pdf
        pdf = PdfPages("Messung.pdf")
        pdf.savefig()
        pdf.close()