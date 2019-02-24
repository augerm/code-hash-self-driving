import os
from file_reader import *

header_cols = ['rows', 'cols', 'num_vehicles', 'num_rides', 'bonus', 'steps']
row_cols = ['x1', 'y1', 'x2', 'y2', 'earliest_start', 'latest_finish']

data = read_file(os.path.join('data', 'a_example.in'), header_cols, row_cols)

rows = data['header']['rows']
cols = data['header']['cols']
num_vehicles = data['header']['num_vehicles']
num_rides = data['header']['num_rides']
bonus = data['header']['bonus']
steps = data['header']['steps']

rides = data['rows']

vehicles = []