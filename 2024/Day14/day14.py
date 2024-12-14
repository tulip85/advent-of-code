from enum import Enum
from functools import reduce
from operator import mul
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation


lines = 103
cols = 101
seconds = 100

robot_commands = {}
robot_positions = {}
class Quadrants(Enum):
    TOPLEFT = 0
    TOPRIGHT = 1
    BOTTOMLEFT = 2
    BOTTOMRIGHT = 3

quadrant_mapping = [ ((0,0), (int((cols-1)/2-1), int((lines-1)/2-1))), #top left
                    ((0, int((lines-1)/2+1)), (int((cols-1)/2-1),lines-1)), #top right
                     ((int((cols+1)/2), 0), ((cols-1, int((lines-1)/2-1)))), #bottom left
                    ((int((cols+1)/2), int((lines-1)/2+1)), (cols-1, lines-1)) ] # bottom right



with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        input = line.split(" ")
        initial_pos_str = input[0].replace("p=","").split(",")
        initial_pos = (int(initial_pos_str[0]), int(initial_pos_str[1]))
        velocity_str = input[1].replace("v=","").split(",")
        vel = (int(velocity_str[0]), int(velocity_str[1]))
        robot_commands[line_id] = (vel)
        robot_positions[line_id] = (initial_pos)

robot_positions_part_2 = robot_positions.copy()

def calculate_updated_position(robot_id):
    pos = robot_positions[robot_id]
    com = robot_commands[robot_id]

    x_new = pos[0] + com[0]
    y_new = pos[1] + com[1]

    if x_new < 0:
        x_new = cols+x_new
    if y_new < 0:
        y_new = lines+y_new
    if x_new >= cols:
        x_new = x_new-cols
    if y_new >= lines:
        y_new = y_new - lines
    
    return (x_new,y_new)

def is_in_quadrant(quadrant, robot_id):
    constraints = quadrant_mapping[quadrant.value]
    pos = robot_positions[robot_id]
    if pos[0] >= constraints[0][0] and pos[0] <= constraints[1][0] and pos[1] >= constraints[0][1] and pos[1] <= constraints[1][1]:
        return True
    return False


for s in range(0, seconds):
    for robot in robot_positions:
        robot_positions[robot] = calculate_updated_position(robot)


quadrant_sum = []
for q in Quadrants:
    quadrant_sum.append(len([r_id for r_id in robot_positions if is_in_quadrant(q, r_id)]))

print(f"Solution to part 1: {reduce(mul,quadrant_sum)}")

#part two
robot_positions = robot_positions_part_2.copy()

iteration = 0
#assumption: all robots have a unique position
while True:
    iteration += 1
    for robot in robot_positions:
        robot_positions[robot] = calculate_updated_position(robot)
    all_robots = robot_positions.values()
    unique_pos = set(all_robots)
    if len(all_robots) == len(unique_pos):
        break

print(f"Solution to problem 2: {iteration}")

#show the Christmas Tree
fig = plt.figure()
x, y = zip(*robot_positions.values())
plt.scatter(x, y)
plt.show()  



