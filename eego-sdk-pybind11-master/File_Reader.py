import pandas as pd
from loguru import logger
from Visualizer import Visualizer
from ant_neuro_stream import EEGO_Connection
import queue
from data_simulator import Data_Simulator

# Was made for debugging purpose
# from Data_simulator import Data_Simulator

""" file_reader Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten
"""

logger.add("File_Reader.log")

class File_Reader():
    def __init__(self, data_queue: queue.Queue) -> None:
        open("File_Reader.log", "w").close() # empties log file
        self.va = Visualizer()
        self.data_queue = data_queue
        
    def read_column_of_file(self, col: int):
        data = pd.read_csv("EE411-012303-000742-eeg.txt", sep="\s+", header=None)
        return data[col]

    def read_line_of_file(self):
        # for line in pd.read_csv("EE411-012303-000742-eeg.txt", sep=" ", chunksize=1, header=None): # now it should read from the stream
        for line in pd.read_csv("eeg_simulation_data.txt", sep=" ", chunksize=1, header=None): # now it should read from the simulation stream
            line = line.iloc[0]  # Get the first row of the chunk
            logger.info(f"{line}")
            alpha = float(line[1])
            beta = float(line[2])
            self.data_queue.put((alpha, beta))

if __name__ == "__main__":
    # define amount of data that shall be simulated
    ds = Data_Simulator()
    ds.write_simulation_data(40)

    # eego = EEGO_Connection()
    # eego.open_stream(1)

    data_queue = queue.Queue

    # read data and visualize it
    fr = File_Reader(data_queue=data_queue)
    fr.read_line_of_file()
    
    fr.show_plots()
    # fr.va.open_plot("Live_Plot")
    fr.va.open_plot("Waterfall_Plot")
