# Parse the input into a grid dictionary
grid = {}

guard_pos = (0,0)
next_direction = {(-1,0): (0,1),(0,1):(1,0), (1, 0):(0,-1), (0, -1):(-1,0)}
obstacles_pos = set()
new_obstacles = set()

with open("input1.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char
            if char == "^":
                guard_pos = (line_id, col_id)
                grid[guard_pos] = "X"
            elif char =="#":
                obstacles_pos.add((line_id,col_id))

def next_step(pos, direction):
    return (pos[0]+direction[0], pos[1]+direction[1])

initial_guard_pos = guard_pos
initial_direction = (-1,0)

def simulate_with_loop_detection(potential_obstacle):
    loop_detection = [(initial_guard_pos, initial_direction)]
    guard_pos = initial_guard_pos
    direction = initial_direction
    if potential_obstacle not in obstacles_pos and potential_obstacle not in new_obstacles and potential_obstacle in grid and guard_pos in grid:
        obstacles_pos.add(potential_obstacle)
        while guard_pos in grid:
            next_pos = next_step(guard_pos,direction)
            if next_pos in obstacles_pos:
                direction = next_direction[direction]
                if (guard_pos, direction) not in loop_detection and guard_pos in grid:
                    loop_detection.append((guard_pos, direction))
                elif (guard_pos, direction)  in loop_detection:
                    new_obstacles.add(potential_obstacle)
                    break
            else:
                guard_pos = next_pos
            
        obstacles_pos.remove(potential_obstacle)


def simulate(guard_pos, direction):
    grid_temp = grid.copy()
    step = 0
    while guard_pos in grid_temp:
        if step %500 == 0:
            print(f"Step {step}, obstacle_pos: {len(new_obstacles)}")
        step += 1
        next_pos = next_step(guard_pos,direction)
        if next_pos in obstacles_pos:
            direction = next_direction[direction]
        else:
            simulate_with_loop_detection(next_pos)
            guard_pos = next_pos
            if guard_pos in grid_temp:
                grid_temp[guard_pos] = "X"
    result = sum(value == "X" for value in grid_temp.values())
    return result



direction = initial_direction

sum_of_pos = simulate(guard_pos, (-1,0))

print(f"The guard visited {sum_of_pos} positions")
print(f"Part two: {len(new_obstacles)} obstacles")
