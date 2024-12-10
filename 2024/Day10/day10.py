grid = {}

queue = set()
queue_2 = []

endpoints = {}
trails = {}

#find all neighbours that are one height up
def find_next_steps(coord):
    number, x, y, start_x, start_y = coord
    candidates = [
        (x, y - 1), (x, y + 1),
        (x + 1, y), (x - 1, y)
    ]
    return [
        (number + 1, nx, ny, start_x, start_y)
        for nx, ny in candidates
        if (nx, ny) in grid and grid[(nx, ny)] == number + 1
    ]

#parse input
with open("input.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = int(char)
            if int(char) == 0:
                queue.add((0, line_id, col_id, line_id, col_id))
                queue_2.append((0, line_id, col_id, line_id, col_id))

#do part 1: use a set to deduplicate at each step
while len(queue) > 0:
    element = queue.pop()

    if element[0] == 9:
        if (element[3], element[4]) not in endpoints:
            endpoints[(element[3], element[4])] = set()
        endpoints[(element[3], element[4])].add((element[1], element[2]))
    else:
        queue = set(list(queue)+find_next_steps(element))

#do part 2: use a list to not deduplicate
while len(queue_2) > 0:
    element = queue_2.pop()

    if element[0] == 9:
        if (element[3], element[4]) not in trails:
            trails[(element[3], element[4])] = 0
        trails[(element[3], element[4])] += 1
    else:
        queue_2 = queue_2+find_next_steps(element)

result = 0
for trailhead in endpoints:
    result += len(endpoints[trailhead])

result_2 = 0
for trail in trails:
    result_2 += trails[trail]

print(f" The result of part one is {result}")
print(f" The result of part two is {result_2}")