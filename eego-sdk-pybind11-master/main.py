"""
Run ant_neuro_stream.py, File_Reader and Visualizer parallel
"""
from ant_neuro_stream import EEGO_Connection
from File_Reader import File_Reader
from Visualizer import Visualizer
import concurrent.futures
import queue

def run_eego_connection():
    con = EEGO_Connection()
    con.open_stream(2)

def run_file_reader(data_queue):
    fr = File_Reader(data_queue)
    fr.read_line_of_file()

def run_visualizer(data_queue):
    vis = Visualizer()
    vis.visualize(data_queue)

if __name__ == "__main__":
    data_queue = queue.Queue()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(run_eego_connection)
        future2 = executor.submit(run_file_reader, data_queue)
        future3 = executor.submit(run_visualizer, data_queue)
        
        concurrent.futures.wait([future1, future2, future3])