import os
from vehicle import Vehicle
from ride import Ride
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
rides_data = data['rows']

rides = []
vehicles = []

def run():
    for i in range(num_vehicles):
        vehicle = Vehicle(i + 1)
        vehicles.append(vehicle)

    for i in range(len(rides_data)):
        ride = Ride(rides_data[i])
        rides.append(ride)

    for i in range(steps):
        grouped_vehicles = get_grouped_vehicles()
        moves = []

        for group in grouped_vehicles:
            possible_moves = get_all_possible_moves(group)
            best_move_for_group = find_best_moves(possible_moves)
            moves.append(best_move_for_group)

        move_vehicles(moves)

    generate_output()


def find_best_moves():
    # This will return an array of the best moves for each vehicle
    move_vehicles()
    update_ride_heuristics()



def get_all_possible_moves():
    # Return [{ <vehicle_id>: [1,2], <vehicle_id>: [2,3] }]

    # Look through all vehicles and generate an array of all possible moves.
    # I.e... [1: [1,2], 2: [1,3], 3: [1,5]]
    # Stay, Left, Up, Down, Right
    # For vehicles that are on a ride take one step closer and don't examine sub-tree.
    # Group vehicles into groups of 5 by distance from each other.



def get_grouped_vehicles():
    # Return an array of groups of vehicles.
    # Initially group vehicles by ID.
    # Optimization: Group vehicles by some heuristic probably distance from other vehicle.

def update_ride_heuristics():
    for(i in range(rides)):
        # Calculate ride heuristic

def calculate_vehicle_heuristic():
    for(i in range(vehicles)):
        # Calculate heuristic of vehicles positions

def move_vehicles():
    # This will move all the cars in the appropriate directions
    # If a vehicle takes a ride, store the ride on that vehicle

def generate_output():
    # Loop through all vehicles and output their ride ID's and the number of rides.

def make_moves(moves):
    # Move all the cars

run()