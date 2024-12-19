from heapq import heappop, heappush

grid = {}
grid_idx = {}

number_of_elements= 1024
start = (0,0)
end = (70,70)

obstacles = []
obstacle_candidates = []
line_id = 0

with open("input.in") as input_file:
    for line in input_file:
        line = line.strip().split(",")
        input_coord = (int(line[0]), int(line[1]))
        if line_id < number_of_elements:
            obstacles.append(input_coord)
        else:
            obstacle_candidates.append(input_coord)
        
        grid[input_coord] = line_id
        grid_idx[line_id] = input_coord

        line_id += 1



def find_neighbours(element, obstacle_list):
    x = element[0]
    y = element[1]

    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]

    return ([(x,y) for x,y in candidates if (x,y) not in obstacle_list and x >= start[0] and y >= start[1] and x <= end[0] and y <= end[1]])

def find_shortest_path(obstacle_list):
    prio_queue = []
    heappush(prio_queue, (0, start))

    visited = {}

    while len(prio_queue) > 0:
        element = heappop(prio_queue)
        neighbours = find_neighbours(element[1], obstacle_list)
        for n in neighbours:
            distance = element[0]+1
            if n not in visited:
                visited[n] = distance
                heappush(prio_queue, (distance, n))
    
    if end in visited:
        return visited[end]
    else:
        return False

guaranteed = find_shortest_path(obstacles)

print(f"Part 1 {guaranteed}")

#search for the breaking point
working = grid_idx[len(obstacles)-1]
breaking = (obstacle_candidates[len(obstacle_candidates)-1])

while abs(grid[working]-grid[breaking]) != 1:
    index = grid[working]+int((grid[breaking]-grid[working])/2)

    updated_obstacles = obstacles.copy() + obstacle_candidates[0:(index-len(obstacles))]

    attempt = find_shortest_path(updated_obstacles)

    if attempt != False:
        working = grid_idx[index-1]
    else:
        breaking = grid_idx[index-1]

print(f"Part two: {breaking}")