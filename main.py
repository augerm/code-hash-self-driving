import sys
import os

inFile = os.path.join('data', 'infile.in')

with open(inFile, 'r') as i:
	lines = i.readlines()

rides = []
vehicles = []

def get_ride_heuristic():
