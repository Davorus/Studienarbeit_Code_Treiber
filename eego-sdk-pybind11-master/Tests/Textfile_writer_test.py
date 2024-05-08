import random

with open("eeg_simulation_data.txt", "w") as f:
    for i in range(0, 51):
        file_values: list = []
        output: str = ""
        for it in range(0, 8): 
            file_values.append(random.uniform(-1, 1))
            output = output + str(file_values[it]) + " "
            # last_cell_info = 1181.0000000000000000 + it
        output = output + str(0.0000000000000000) + " " + str(1181.0000000000000000 + i) + "\n"
        f.write(output)