# Parse the input into a grid dictionary
grid = {}
with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char


def find_direction(start, next):
    if next[0] == start[0] and next[1] +1 == start[1]:
        return "left"
    if next[0] == start[0] and next[1] -1 == start[1]:
        return "right"
    if next[1] == start[1] and next[0] -1 == start[0]:
        return "up"
    if next[1] == start[1] and next[0] -1 == start[0]:
        return "down"
    
def find_next(point, chain, perimeter):
    if (point[0], point[1]+1) in perimeter and (point[0], point[1]+1) not in chain:
        return (point[0], point[1]+1)
    if (point[0], point[1]-1) in perimeter and (point[0], point[1]-1) not in chain:
        return (point[0], point[1]-1)
    if (point[0]+1, point[1]) in perimeter and (point[0]+1, point[1]) not in chain:
        return (point[0]+1, point[1])
    if (point[0]-1, point[1]) in perimeter and (point[0]-1, point[1]) not in chain:
        return (point[0]-1, point[1])
    print("error ", point, chain)

def find_next_not_in_shape(point, region):
    if (point[0], point[1]+1) not in region:
        return (point[0], point[1]+1)
    if (point[0]+1, point[1]) not in region:
        return (point[0]+1, point[1])
    print("error ", point)






def find_neighbours_count(x,y,char):
    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]
    neighbours = [
        (nx, ny)
        for nx, ny in candidates
        if ((nx, ny) in grid and grid[(nx, ny)] != char) or (nx, ny) not in grid
    ]
    return neighbours

def find_neighbours(x,y,char, visited):
    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]

    out_temp = [ (nx, ny,char, len(find_neighbours_count(nx, ny, char)), find_neighbours_count(nx,ny,char)) for nx, ny in candidates if (nx, ny) in grid and grid[(nx, ny)] == char and (nx,ny,char) not in visited]
    out = [(x,y,char, len(find_neighbours_count(x,y,char)), find_neighbours_count(x,y,char))]
    if len(out_temp) > 0:
        for el in out_temp:
            visited.add((el[0], el[1], el[2]))
            out = out + find_neighbours(el[0], el[1], el[2], visited)
        return out
            
    else:
        return out
    
def find_neighbours_simple(x,y,region, perim):
    region = [(n[0],n[1]) for n in region ]
    
    neighbours = []
    if (x,y-1) in region and (x,y-1) not in perim and (((x-1,y) in perim and (x-1, y-1) in perim) or ((x+1,y) in perim and (x+1, y-1) in perim)):
        neighbours.append((x,y-1))
    if (x,y+1) in region and (x,y+1) not in perim and (((x-1,y) in perim and (x-1, y+1) in perim) or ((x+1,y) in perim and (x+1, y+1) in perim)):
        neighbours.append((x,y+1))
    if (x+1,y) in region and (x+1,y) not in perim and (((x+1,y-1) in perim and (x, y-1) in perim) or ((x+1,y+1) in perim and (x, y+1) in perim)):
        neighbours.append((x+1,y))
    if (x-1,y) in region and (x-1,y) not in perim and (((x-1,y-1) in perim and (x, y-1) in perim) or ((x-1,y+1) in perim and (x, y+1) in perim)):
        neighbours.append((x-1,y))

    return set(neighbours)
   

def find_straight_lines(perimeter, reg, perim):
    remove = 0
    neighb = set()
    neighbours = []
    for point in reg:
        neighbours = neighbours +[r[4] for r in reg if point[0] == r[0] and point[1] == r[1]][0]
    
    neighb = set(neighbours)

    for n in neighb:
        nb = find_neighbours_simple(n[0], n[1],neighb, perim)
        remove += len(nb)
        
    return perimeter-int(remove/2)

        
#manque 1: I, V, F

grid_c = list(grid.copy().keys())
regions = []
while len(grid_c) > 0:
    element = grid_c.pop()
    character = grid[element]
    neighbours = find_neighbours(element[0], element[1], character, set())
    regions.append(neighbours)

    for n in neighbours:
        if (n[0], n[1]) in grid_c:
            grid_c.remove((n[0], n[1]))

total_price = 0
total_price_2 = 0
for reg in regions:
    print(f"Letter {reg[0][2]} ")
    reg_no_neighbours =  [(r[0], r[1], r[2], r[3]) for r in reg]
    region = set(reg_no_neighbours)
    area = len(region)
    perimeter = sum([n[3] for n in region])
    total_price += perimeter*area
    

    #part two
    perimeter_points = [(element[0], element[1]) for element in region if element[3] > 0]
    straight = find_straight_lines( perimeter, reg, perimeter_points)
    print(f" area {area}, perimeter {perimeter}, straight {straight}")
    total_price_2 += area * straight
    


print(total_price)
print(total_price_2)

##too high 822076

##         824518