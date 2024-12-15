from enum import Enum

class Objects(Enum):
    WALL = "#"
    BOX = "O"
    EMPTY = "."
    ROBOT = "@"
    BOX_START = "["
    BOX_END = "]"

movements = {"^": (-1,0), ">": (0,1), "v": (1, 0), "<": (0,-1)}

def calculate_position(position, movement):
    return (position[0]+movements[movement][0], position[1]+movements[movement][1])

def calculate_position_box(position, movement):
    return ((position[0][0]+movements[movement][0], position[0][1]+movements[movement][1]), (position[1][0]+movements[movement][0], position[1][1]+movements[movement][1]))

def get_all_box_positions():
    return  [a[0]for a in boxes]+[a[1]for a in boxes]
def get_all_box_start_positions():
    return  [a[0]for a in boxes]
def get_all_box_end_positions():
    return  [a[1]for a in boxes]

def get_box(pos):
    if pos in get_all_box_start_positions():
        return (pos, calculate_position(pos, ">"))
    else:
        return (calculate_position(pos, "<"), pos)
    
def move_box_up_or_down(position, m, simulate):
    #retrieve the right box
    if position in get_all_box_start_positions():
        box = (position, calculate_position(position, ">"))
    else:
        box = (calculate_position(position, "<"), position)
     
    next = calculate_position_box(box, m)

    if next[0] in walls or next[1] in walls:
        return False
    
    all_boxes = get_all_box_positions()

    boxes_to_move = []
    if next[0] in all_boxes:
        if next[0] in get_all_box_start_positions():
            boxes_to_move.append((next[0], calculate_position(next[0], ">")))
        else:
            boxes_to_move.append((calculate_position(next[0], "<"), next[0]))
    if next[1] in all_boxes:
        if next[1] in get_all_box_start_positions():
            boxes_to_move.append((next[1], calculate_position(next[1], ">")))

    
    boxes_to_move = list(set(boxes_to_move))
    if sum([move_box_up_or_down(b[0],m, simulate) for b in boxes_to_move]) == len(boxes_to_move):
        if not simulate and box in boxes:
            boxes.remove(box)
            boxes.append(next)
        return True
    else:
        return False


def do_movement(m, robot):
    next = calculate_position(robot, m)
    if next in walls:
        return robot
    if next not in get_all_box_positions():
        return next
    
    #try to find a new place for the box
    if m == "<" or m == ">":
        next_robot = next
        empty_slot = calculate_position(next_robot, m)
        while empty_slot not in walls and empty_slot in get_all_box_positions():
            empty_slot = calculate_position(empty_slot, m)

        if empty_slot not in walls and empty_slot not in get_all_box_positions():
            #move all boxes
            if m == "<":
                for i in range(empty_slot[1]+1, robot[1], 2):
                    if ((robot[0], i), (robot[0], i+1)) in boxes:
                        boxes.remove(((robot[0], i), (robot[0], i+1)))
                        boxes.append(((robot[0], i-1), (robot[0], i)))
            elif m == ">":
                for i in range(robot[1]+1, empty_slot[1], 2):
                    if ((robot[0], i), (robot[0], i+1)) in boxes:
                        boxes.remove(((robot[0], i), (robot[0], i+1)))
                        boxes.append(((robot[0], i+1), (robot[0], i+2)))


            return next_robot
        else:
            return robot
    if m == "v" or m == "^":
        do_movement = move_box_up_or_down(get_box(next)[0], m, True)
        if do_movement:
            move_box_up_or_down(get_box(next)[0], m, False)
            return next
        else:
            return robot
    
def draw_map():
    for line_n in range(0, max([i[0] for i in walls])+1):
        line = ""
        start_box = get_all_box_start_positions()
        end_box = get_all_box_end_positions()
        for col_n in range(0, max([i[1] for i in walls])+1):
            if (line_n, col_n) == robot_pos:
                line += Objects.ROBOT.value
            elif (line_n, col_n) in walls:
                line += Objects.WALL.value
            elif (line_n, col_n) in start_box:
                line += "["
            elif (line_n, col_n) in end_box:
                line += "]"
            else:
                line += Objects.EMPTY.value
        print(line)


#create the map
robot_pos = (0,0)
walls = []
boxes = []
with open("map.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            if char == Objects.ROBOT.value:
                robot_pos = (line_id, col_id*2)
            elif char == Objects.BOX.value:
                boxes.append(((line_id, col_id*2),(line_id, col_id*2+1)))
            elif char == Objects.WALL.value:
                walls.append((line_id, col_id*2))
                walls.append((line_id, col_id*2+1))

draw_map()
#do the movements
with open("movements.in") as input_file:
    for line in input_file:
        for char in line.strip():
            #print(char)
            robot_pos = do_movement(char, robot_pos)
            #draw_map()


draw_map()


part_2_result = sum([(100*i[0][0])+i[0][1] for i in boxes ])

print(part_2_result)

