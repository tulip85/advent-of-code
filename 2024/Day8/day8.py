grid = {}

border_line = 0
border_col = 0

with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            if char != ".":
                if char in grid:
                    grid[char].append((line_id, col_id))
                else:
                    grid[char] = [(line_id, col_id)]

            if col_id > border_col:
                border_col = col_id
            if line_id > border_line:
                border_line = line_id
                                

antinodes = set()
antinodes_2 = set()

def is_in_grid(pair):
    if pair[0] >= 0 and pair[0] <= border_line and pair[1]>= 0 and pair[1]<= border_col:
        return True
    else:
        return False
    
def get_antinodes(antenna_1, antenna_2, distance):
    x_dist = abs(antenna_2[0]-antenna_1[0])
    y_dist = abs(antenna_2[1]-antenna_1[1])

    antinode_1, antinode_2 = (0,0), (0,0)
    antinodes_return = []

    if antenna_1[0] >= antenna_2[0] and antenna_1[1] >= antenna_2[1]:
        antinode_1 = (antenna_1[0] + x_dist*distance, antenna_1[1] + y_dist*distance)
        antinode_2 = (antenna_2[0] - x_dist*distance, antenna_2[1]- y_dist*distance)
    elif antenna_1[0] < antenna_2[0] and antenna_1[1] < antenna_2[1]:
        antinode_1 = (antenna_1[0] - x_dist*distance, antenna_1[1] - y_dist*distance)
        antinode_2 = (antenna_2[0] + x_dist*distance, antenna_2[1]+ y_dist*distance)
    elif antenna_1[0] < antenna_2[0] and antenna_1[1] >= antenna_2[1]:
        antinode_1 = (antenna_1[0] - x_dist*distance, antenna_1[1] + y_dist*distance)
        antinode_2 = (antenna_2[0] + x_dist*distance, antenna_2[1]- y_dist*distance)
    elif antenna_1[0] >= antenna_2[0] and antenna_1[1] < antenna_2[1]:
        antinode_1 = (antenna_1[0] + x_dist*distance, antenna_1[1] - y_dist*distance)
        antinode_2 = (antenna_2[0] - x_dist*distance, antenna_2[1]+ y_dist*distance)
    else:
        print("error")                

    if  is_in_grid(antinode_1):
        antinodes_return.append(antinode_1)
    if is_in_grid(antinode_2):
        antinodes_return.append(antinode_2)
    
    return antinodes_return

for char in grid:
    for antenna_1 in grid[char]:
        for antenna_2 in grid[char]:
            if antenna_1 != antenna_2:
                dst = 0
                antinodes_temp = get_antinodes(antenna_1, antenna_2, dst)   
                while len(antinodes_temp) >= 1:
                    for antinode in antinodes_temp:
                        if dst == 1:
                            antinodes.add(antinode)
                        
                        antinodes_2.add(antinode)

                    dst += 1
                    antinodes_temp = get_antinodes(antenna_1, antenna_2, dst)


print(f"Part one: {len(antinodes)} antinodes")
print(f"Part two: {len(antinodes_2)} antinodes")
