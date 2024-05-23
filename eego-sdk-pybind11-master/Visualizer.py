import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from typing import Final
import numpy as np
import pickle

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

    def show_plot(self, alpha_data, beta_data):
        """
        Should show the whole plot with a waterfall diagram
        """
        # clear previous plots
        self.plot_alpha.clear()
        self.plot_beta.clear()

        # plotting alpha data
        self.plot_alpha.plot(alpha_data, color="b")
        
        # plotting beta data
        self.plot_beta.plot(beta_data, color="r")

        # inverting x_axis, alpha
        self.plot_alpha.invert_xaxis()

        # inverting x_axis, beta
        self.plot_beta.invert_xaxis()

        # draw and pause
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.show()
        
        self.save_plot(figure=self.figure, name="Live_Plot")
        
    def create_3d_waterfall_diagram(self, alpha: list, beta: list):        
        alpha_data = alpha
        beta_data = beta

        # num of data points
        num_data_points = len(alpha_data)
    
        # y values for every data point 
        y = np.arange(num_data_points)
    
        # plot 3D-Plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # plot alpha data
        ax.plot(y, alpha_data, zs=0, zdir='z', label='Alpha', color='b', alpha=0.7)

        # plot beta data
        ax.plot(y, beta_data, zs=1, zdir='z', label='Beta', color='r', alpha=0.7)

        # label axes
        ax.set_xlabel("Zeit")
        ax.set_ylabel("Wert")
        ax.set_zlabel("Alpha/Beta")

        # set x axe
        ax.set_zticks([0, 1])
        ax.set_zticklabels(['Alpha', 'Beta'])

        # title of plot
        ax.set_title("3D Wasserfalldiagramm")
        fig.canvas.manager.set_window_title("3D Darstellung - EEG Messung")

        # show legend
        ax.legend()

        # draw plot
        plt.show()
        
        self.save_plot(figure=fig, name="Waterfall_Plot")

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

    def save_plot(self, figure, name: str):
        with open(f"{name}.pkl", "wb") as f:
            pickle.dump(figure, f)

    def open_plot(self, type: str):
        """
        type = Live_Plot or Waterfall_Plot
        """
        with open(f"{type}.pkl", "rb") as f:
            loaded_fig = pickle.load(f)
        
        # Sicherstellen, dass die Figur von pyplot verwaltet wird
        new_manager = plt.figure().canvas.manager
        new_manager.canvas.figure = loaded_fig
        loaded_fig.set_canvas(new_manager.canvas)
        plt.show()