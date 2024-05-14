import pandas as pd
import time
from loguru import logger
from Visualizer import *

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
            self.va.visualize(line[1]) # 1 um es zu testen, kann jeglicher Index sein
            time.sleep(0.1)


if __name__ == "__main__":
    fr = File_Reader()
    fr.read_line_of_file()