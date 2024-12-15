from enum import Enum

class Objects(Enum):
    WALL = "#"
    BOX = "O"
    EMPTY = "."
    ROBOT = "@"

movements = {"^": (-1,0), ">": (0,1), "v": (1, 0), "<": (0,-1)}

def do_movement(m, robot):
    next = (robot[0]+movements[m][0], robot[1]+movements[m][1])
    if next not in grid:
        return robot
    if grid[next] == Objects.EMPTY:
        return next
    
    #try to find a new place for the box
    box_pos = next
    while box_pos in grid and grid[box_pos] != Objects.EMPTY and grid[box_pos] != Objects.WALL:
        box_pos = (box_pos[0]+movements[m][0], box_pos[1]+movements[m][1])
    
    if box_pos in grid and grid[box_pos] == Objects.EMPTY:
        grid[next] =  Objects.EMPTY
        grid[box_pos] = Objects.BOX
        return next
    else:
        return robot
    
def draw_map():
    for line_n in range(0, max([i[0] for i in grid])+1):
        line = ""
        for col_n in range(0, max([i[1] for i in grid])+1):
            if (line_n, col_n) == robot_pos:
                line += "@"
            else:
                line += grid[(line_n, col_n)].value
        print(line)


#create the map
grid = {}
robot_pos = (0,0)
with open("map.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            if char == Objects.ROBOT.value:
                robot_pos = (line_id, col_id)
                grid[(line_id, col_id)] = Objects.EMPTY
            elif char == Objects.BOX.value:
                grid[(line_id, col_id)] = Objects.BOX
            elif char == Objects.EMPTY.value:
                grid[(line_id, col_id)] = Objects.EMPTY
            elif char == Objects.WALL.value:
                grid[(line_id, col_id)] = Objects.WALL

#do the movements
with open("movements.in") as input_file:
    for line in input_file:
        for char in line.strip():
            robot_pos = do_movement(char, robot_pos)

#print(robot_pos)
draw_map()

part_1_result = sum([(100*i[0])+i[1] for i in grid if grid[i] == Objects.BOX])


print(f"The result for part 1 is: {part_1_result}")