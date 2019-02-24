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

# Parameters
DENSITY_TOLERANCE = 5 # Defines the size of the boundary when calculating density of an area.

ENDPOINT_DENSITY_MULTIPLIER = 1
BONUS_DISTANCE_TRADE_OFF_MULTIPLIER = 1
GRAB_BONUS_MULTIPLIER = 1

rides = []
vehicles = []
cur_step = 0

def run():
    for i in range(num_vehicles):
        vehicle = Vehicle(i + 1)
        vehicles.append(vehicle)

    for i in range(len(rides_data)):
        ride = Ride(rides_data[i], i + 1)
        rides.append(ride)

    for i in range(steps):
        grouped_vehicles = get_grouped_vehicles()
        moves = []

        for group in grouped_vehicles:
            possible_moves = get_all_possible_moves(group)
            best_move_for_group = find_best_moves(possible_moves)
            moves.append(best_move_for_group)

        move_vehicles(moves)
        cur_step += 1 # TODO: This might need to come before

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
    for ride in rides:
        endpoint_density = get_ride_density(ride.end_point)
        distance = get_distance(ride.start_point, ride.end_point)
        bonus_distance_trade_off = bonus/distance
        heuristic_val = (10/(ride.earliest_start - cur_step)) * GRAB_BONUS_MULTIPLIER + (endpoint_density * ENDPOINT_DENSITY_MULTIPLIER) + \
                        (bonus_distance_trade_off * BONUS_DISTANCE_TRADE_OFF_MULTIPLIER)
        ride.update_value(heuristic_val)

def get_distance(start_point, end_point):
    return abs(start_point[0] - end_point[0]) + abs(start_point[1] - end_point[1])

def get_ride_density(point):
    count = 0
    for ride in rides:
        dist = get_distance(ride.start_point, point)
        if dist < DENSITY_TOLERANCE:
            count += 1
    return count

def calculate_vehicle_heuristic():
    for(vehicle in vehicles):
        # Calculate heuristic of vehicles positions
        # if vehicle.target_position:
        #     return vehicle.target_position - vehicle.cur_location
        # if not vehicle.target_position:
        #     return ride

def move_vehicles(moves):
    # Move all the cars
    for (move in moves):
        vehicle_id = move.vehicle_id
        target_position = move.target_position
        vehicle = vehicles[vehicle_id - 1]
        vehicle.cur_position = target_position
        vehicle.end_trip_if_done()
        take_ride_if_available(vehicle)

def take_ride_if_available(vehicle):
    for ride in rides:
        if ride.earliest_start <= cur_step:
            if ride.take_ride():
                vehicle.rides_taken.append(ride.id)
                ride.on_trip = True


def generate_output():
    # Loop through all vehicles and output their ride ID's and the number of rides.
    f = open("rides.out", "w+")
    output = []
    for (vehicle in vehicles):
        for(ride in vehicles.rides_taken):
            subject = "rides" if len(ride) else "ride"
            output.append(vehicle.id+" this vehicle is assigned "+len(ride)+" "+subject+": "+vehicles.rides_taken)
    f.writelines(output)
    f.close

run()
