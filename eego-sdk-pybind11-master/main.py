"""
Run ant_neuro_stream.py, File_Reader and Visualizer parallel
"""
from ant_neuro_stream import EEGO_Connection
from File_Reader import File_Reader
from Visualizer import Visualizer

if __name__ == "__main__":
    # define class pointers
    eego_con = EEGO_Connection()
    file_reader = File_Reader()
    visualizer = Visualizer()

    #
    alpha_data = file_reader.read_column_of_file(0)
    beta_data = file_reader.read_column_of_file(1)
    visualizer.show_plot(alpha_data=alpha_data, beta_data=beta_data)
    visualizer.create_3d_waterfall_diagram(alpha=alpha_data, beta=beta_data)