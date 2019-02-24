import os
from file_reader import *

header_cols = ['rows', 'cols', 'num_vehicles', 'num_rides', 'bonus', 'steps']
row_cols = ['x1', 'y1', 'x2', 'y2', 'earliest_start', 'latest_finish']

data = read_file(os.path.join('data', 'a_example.in'), header_cols, row_cols)

rides = []
vehicles = []