import pandas as pd
from loguru import logger
from Visualizer import Visualizer
from data_simulator import Data_Simulator

""" file_reader Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten
"""

logger.add("File_Reader.log")

class File_Reader():
    def __init__(self) -> None:
        self.file_ptr = open("EE411-012303-000742-eeg.txt", "r")
        open("File_Reader.log", "w").close() # empties log file
        self.va = Visualizer()
        
    def read_column_of_file(self, col: int):
        data = pd.read_csv("EE411-012303-000742-eeg.txt", sep="\s+", header=None)
        return data[col]

    def read_line_of_file(self):
        for line in pd.read_csv("EE411-012303-000742-eeg.txt", sep=" ", chunksize=1, header=None): # now it should read from the simulation stream
            # print(line) # [] indexing possible
            line = line.iloc[0]  # Get the first row of the chunk
            logger.info(f"{line}")
            self.va.visualize(float(line[1]), float(line[2]))
        
        self.va.show_plot()
        
        alpha_data = self.read_column_of_file(0)
        beta_data = self.read_column_of_file(1)
        
        self.va.create_3d_waterfall_diagram(alpha=alpha_data, beta=beta_data)
        # after measuring is done save plot
        self.va.save_plot()

if __name__ == "__main__":
    # define amount of data that shall be simulated
    # ds = Data_Simulator()
    # ds.write_simulation_data(40)

    # read data and visualize it
    fr = File_Reader()
    fr.read_line_of_file()
    fr.va.create_3d_waterfall_diagram()
