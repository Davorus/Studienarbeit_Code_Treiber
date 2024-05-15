import pandas as pd
from loguru import logger
from Visualizer import Visualizer
from Data_Simulator import Data_Simulator

""" file_reader Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten
"""

logger.add("File_Reader.log")

class File_Reader():
    def __init__(self) -> None:
        self.file_ptr = open("eeg_simulation_data.txt", "r")
        open("File_Reader.log", "w").close() # empties log file
        self.va = Visualizer()

    def read_line_of_file(self):
        for line in pd.read_csv("./eeg_simulation_data.txt", sep=" ", chunksize=1, header=None): # now it should read from the simulation stream
            # print(line) # [] indexing possible
            logger.info(f"{line}")
            self.va.visualize(line[1], line[2], line[9]) # 1 um es zu testen, kann jeglicher Index sein
            # time.sleep(0.1)
        # after measuring is done save plot
        self.va.save_plot()
        # show plot after saving
        self.va.show_plot()

if __name__ == "__main__":
    # define amount of data that shall be simulated
    ds = Data_Simulator()
    ds.write_simulation_data(50)

    # read data and visualize it
    fr = File_Reader()
    fr.read_line_of_file()