from heapq import heapify, heappop, heappush

grid = {}

reindeer = (0,0)
end = (0,0)
with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char
            if char == "S":
                reindeer = (line_id, col_id)
                grid[(line_id, col_id)] = "."
            if char == "E":
                end = (line_id, col_id)
                grid[(line_id, col_id)] = "."


prio_queue = []
heappush(prio_queue, (0, reindeer, (0,1)))

visited = {}

path_tracker = [reindeer]

def find_neighbours(element, D):
    x = element[0]
    y = element[1]

    return_array = []


    if D != (0, -1) and grid[(x, y+1)] == ".":
        if D == (0,1):
            return_array.append(((x, y+1), 1, D))
        else:
            return_array.append(((x, y+1), 1001, (0, 1)))
    if D != (0, 1) and grid[(x, y-1)] == ".":
        if D == (0,-1):
            return_array.append(((x, y-1), 1, D))
        else:
            return_array.append(((x, y-1), 1001, (0, -1)))
    if D != (-1, 0) and grid[(x+1, y)] == ".":
        if D == (1, 0):
            return_array.append(((x+1, y), 1, D))
        else:
            return_array.append(((x+1, y), 1001, (1, 0)))
    if D != (1, 0) and grid[(x-1, y)] == ".":
        if D == (-1, 0):
            return_array.append(((x-1, y), 1, D))
        else:
            return_array.append(((x-1, y), 1001, (-1, 0)))

    return return_array

while len(prio_queue) > 0:
    element = heappop(prio_queue)
    #find all neighbours
    neighbours = find_neighbours(element[1], element[2])
    for n in neighbours:
        distance = element[0]+n[1]
        if n[0] not in visited:
            visited[n[0]] = distance
            heappush(prio_queue, (distance, n[0], n[2]))


print(visited[end])

# find the paths
queue = [end]

path_tracker = set()
print(reindeer)

def draw_map():
    for line_n in range(0, max([i[0] for i in grid])+1):
        line = ""
        for col_n in range(0, max([i[1] for i in grid])+1):
            if (line_n, col_n) == reindeer:
                line += "S"
            elif (line_n, col_n) == end:
                line += "E"
            elif (line_n, col_n) in path_tracker:
                line += "0"
            else:
                line += grid[(line_n, col_n)]
        print(line)

solution = set()

def find_path(input, path):
    element = input[0]
    distance = input[1]
    D = input[2]
    if element == reindeer:
        print("found")
        path.append(reindeer)
        return path
    else:
        if element in visited:
            neighbours = find_neighbours(element, D)
            next_step = [n for n in neighbours if n[0] in visited and n[0] not in path]
            result = []
            for el in next_step:
                new_path = path.copy()
                new_distance =  distance - el[1]
                new_path.append(element)
                res = find_path((el[0],new_distance, el[2]), new_path)
                if el[0] == reindeer:
                    print("hello")
                if res is not None and len(res) > 0:
                    result +=find_path(el, new_path)
            return result
        else:
            return None

x = find_path((end, visited[end], (element[2][0]*-1,element[2][1]*-1) ), [])
print(x)
path_tracker = list(set(x))

draw_map()
#and visited[n[0]] == min_distance 

        
print(len(path_tracker))