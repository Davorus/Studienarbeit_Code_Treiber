import random

"""Data_Simulator Klasse
Die Klasse hier simuliert theoretisch die Messung der AntNeuro Box. Sie schreibt in eine Datei im gleichen Stil wie die AntNeuro Box 8 'zufällige' (eigentlich gemessene aber hier halt zufällige) Werte in eine
Text-Datei und einmal die Erdung (0.0) und einen anderen Wert der sich immer um 1 erhöht. Anhand dieser Erkenntnisse ist das hier programmiert
"""

class Data_Simulator():
    def __init__(self):
        pass

    def check_if_file_exists(self):
        pass

    def write_simulation_data(self, data_amount: int):
        with open("eeg_simulation_data.txt", "w") as f:
            for i in range(0, data_amount):
                file_values = []
                output = ""
                for it in range(0, 8): 
                    file_values.append(random.uniform(-1, 1))
                    output = output + str(file_values[it]) + " "
                output = output + str(0.0000000000000000) + " " + str(0.0000000000000000 + i) + "\n"
                f.write(output)


if __name__ == "__main__":
    ds = Data_Simulator()
    ds.write_simulation_data(200)