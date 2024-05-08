import pandas as pd

""" file_reader Klasse
Die Visualizer Klasse selbst ist nur für die Darstellung zuständig. Mehr soll diese nicht machen, nur plotten
"""

class File_Reader():
    def __init__(self) -> None:
        self.file_ptr = open("eeg_simulation_data.txt", "r")

    def read_line_from_file(self):
        pd.