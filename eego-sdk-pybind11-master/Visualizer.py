import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from typing import Final
import numpy as np

class Visualizer():
    def __init__(self):
        # visualized alpha que
        self.que_alpha = []

        # visualized beta que
        self.que_beta = []

        # boundary on how long the array should be
        self.max_data_length: Final[int] = 40 

        # live plot settings
        self.figure, (self.plot_alpha, self.plot_beta) = plt.subplots(2, 1)
        self.figure.canvas.manager.set_window_title("Live Darstellung - EEG Messung")
        self.figure.tight_layout()
        self.figure.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

        # Initialize data_index to keep track of time points
        self.data_index = list(range(self.max_data_length))

    def show_plot(self):
        """
        Should show the whole plot with a waterfall diagram
        """
        # clear previous plots
        self.plot_alpha.clear()
        self.plot_beta.clear()

        # plotting alpha data
        self.plot_alpha.plot(self.data_index[:len(self.que_alpha)], self.que_alpha, color="b")
        
        # plotting beta data
        self.plot_beta.plot(self.data_index[:len(self.que_beta)], self.que_beta, color="r")

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
        
    def create_3d_waterfall_diagram(self, alpha: list, beta: list):        
        alpha_data = alpha
        beta_data = beta

        # Anzahl der Datenpunkte
        num_data_points = len(alpha_data)
    
        # Y-Werte für die einzelnen Datenpunkte (hier einfach eine aufsteigende Zahlenreihe)
        y = np.arange(num_data_points)
    
        # Erstellen des 3D-Plots
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plotten der Alpha-Daten
        ax.plot(y, alpha_data, zs=0, zdir='z', label='Alpha', color='b', alpha=0.7)

        # Plotten der Beta-Daten
        ax.plot(y, beta_data, zs=1, zdir='z', label='Beta', color='r', alpha=0.7)

        # Achsenbeschriftungen
        ax.set_xlabel("Datenpunkte")
        ax.set_ylabel("Wert")
        ax.set_zlabel("Alpha/Beta")

        # Setzen der Z-Achse
        ax.set_zticks([0, 1])
        ax.set_zticklabels(['Alpha', 'Beta'])

        # Titel des Plots
        ax.set_title("3D Wasserfalldiagramm")

        # Anzeigen der Legende
        ax.legend()

        # Anzeigen des Plots
        plt.show()

    def visualize(self, alpha: float, beta: float):
        """
        1. Check for array length, if it gets too long the plot-process will turn out too slow
        """
        if len(self.que_alpha) >= self.max_data_length:
            # Remove the oldest data point
            self.que_alpha.pop(0)
            self.que_beta.pop(0)
            self.data_index.pop(0)

        # Append the new data points
        self.que_alpha.append(alpha)
        self.que_beta.append(beta)
        self.data_index.append(self.data_index[-1] + 1 if self.data_index else 0)
        
        """
        2. Clear the subplots before drawing on them, they have to be reset with the data representation as it bugs then
        """
        # clear plot alpha
        self.plot_alpha.clear()

        # clear plot beta
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

        """
        4. Now let it plot
        """
        # plotting alpha data
        self.plot_alpha.plot(self.data_index[:len(self.que_alpha)], self.que_alpha, color="b")

        # plotting beta data
        self.plot_beta.plot(self.data_index[:len(self.que_beta)], self.que_beta, color="r")

        """ 
        5. At lastly it shall draw on its canvas
        """
        # draw, pause and clear
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.pause(0.001)

    def save_plot(self):
        # save plot as pdf
        pdf = PdfPages("Messung.pdf")
        pdf.savefig(self.figure)
        pdf.close()
