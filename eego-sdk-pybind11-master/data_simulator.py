import random

class Data_Simulator():
    def __init__(self):
        self.file_values = []
        self.output = ""

    def check_if_file_exists(self):
        pass

    def write_simulation_data(self, data_amount: int):
        for i in range(0, data_amount):
            with open("eeg_simulation_data.txt", "w") as f:
                for it in range(0, 8): 
                    self.file_values.append(random.uniform(-1, 1))
                    self.output = self.output + str(self.file_values[it]) + " "
                self.output = self.output + str(0.0000000000000000) + " " + str(1181.0000000000000000 + i) + "\n"
                f.write(self.output)

                

if __name__ == "__main__":
    ds = Data_Simulator()
    ds.write_simulation_data(100)