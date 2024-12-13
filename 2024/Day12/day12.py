# Parse the input into a grid dictionary
grid = {}
with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char

def find_neighbours(x,y,char, visited):
    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]

    out_temp = [ (nx, ny,char) for nx, ny in candidates if (nx, ny) in grid and grid[(nx, ny)] == char and (nx,ny,char) not in visited]
    out = [(x,y,char)]
    if len(out_temp) > 0:
        for el in out_temp:
            visited.add((el[0], el[1], el[2]))
            out = out + find_neighbours(el[0], el[1], el[2], visited)
        return out
            
    else:
        return out

   
def count_corners(x, y, region):
    corners = 0

    # Outer corners
    corners += (x - 1, y) not in region and (x, y - 1) not in region
    corners += (x + 1, y) not in region and (x, y + 1) not in region
    corners += (x + 1, y) not in region and (x, y - 1) not in region
    corners += (x - 1, y) not in region and (x, y + 1) not in region
    
    # Inner corners
    corners += (x - 1, y) in region and (x, y + 1) in region and (x - 1, y + 1) not in region
    corners += (x + 1, y) in region and (x, y + 1) in region and (x + 1, y + 1) not in region
    corners += (x - 1, y) in region and (x, y - 1) in region and (x - 1, y - 1) not in region
    corners += (x + 1, y) in region and (x, y - 1) in region and (x + 1, y - 1) not in region
    

    return corners
        
def count_perimeter(x,y,region):
    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]
    return len([(x,y) for x,y in candidates if (x,y) not in region])


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
    reg_simple =  [(r[0], r[1]) for r in reg]
    region = set(reg_simple)
    area = len(region)
    
    corners = 0
    perim = 0
    for point in region:
        corners += count_corners(point[0], point[1], reg_simple)
        perim += count_perimeter(point[0], point[1], reg_simple)
    total_price += area * perim
    total_price_2 += area * corners

print(f"total price part 1: {total_price}")
print(f"total price part 2: {total_price_2}")
