import random

with open("eeg_simulation_data.txt", "w") as f:
    file_values: list = []
    for it in range(0, 8): 
        file_values.append(random.uniform(-3, 3))
        print("Random generated values: " + str(file_values[it]))
        last_cell_info = 1181.0000000000000000 + it
        f.write(str(file_values[it]) + " " )