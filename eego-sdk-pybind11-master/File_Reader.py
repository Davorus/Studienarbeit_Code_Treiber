import pandas as pd
import time
from loguru import logger

""" file_reader Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten
"""

logger.add("File_Reader.log")

class File_Reader():
    def __init__(self) -> None:
        self.file_ptr = open("eeg_simulation_data.txt", "r")
        self.line_ptr = 0
        self.amount_lines = 0
        open("File_Reader.log", "w").close() # empties log file

    def read_line_of_file(self):
        for line in pd.read_csv("./eeg_simulation_data.txt", sep=" ", chunksize=1, header=None): # now it should read from the simulation stream
            print(line) # [] indexing possible
            logger.info(f"{line}")
            time.sleep(0.01)
            


if __name__ == "__main__":
    fr = File_Reader()
    fr.read_line_of_file()