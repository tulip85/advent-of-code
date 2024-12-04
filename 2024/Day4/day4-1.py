
directions = {"HL": (0,-1), "HR": (0,1), "VU": (-1,0), "VD": (1,0), "DUL": (-1, -1), "DUR": (-1, 1), "DDL": (1,-1), "DDR": (1,1)}
directions_xmas = [
    {"M": [(-1, -1), (-1, 1)], "S": [(1, -1), (1, 1)]},
    {"M": [(-1, -1), (1, -1)], "S": [(-1, 1), (1, 1)]},
    {"M": [(1, -1), (1, 1)], "S": [(-1, 1), (-1, -1)]},
    {"M": [(-1, 1), (1, 1)], "S": [(-1, -1), (1, -1)]},
    ]


def add_tuple(tuple1, tuple2):
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])

def find_xmas(tuple,grid, letters, direction):
    next_pos = add_tuple(tuple,directions[direction])
    if next_pos in grid and grid[next_pos] == letters[0]:
        if len(letters) == 1:
            return 1
        return find_xmas(next_pos, grid, letters[1::], direction)
    return 0

def find_x_mas(tuple, grid):
    for option in directions_xmas:
        m_positions = [add_tuple(tuple, offset) for offset in option["M"]]
        s_positions = [add_tuple(tuple, offset) for offset in option["S"]]

        if all(pos in grid and grid[pos] == "M" for pos in m_positions) and \
           all(pos in grid and grid[pos] == "S" for pos in s_positions):
            return 1
    return 0


with open("input1.in") as input_file:

    grid = {}
    solution, solution2 = 0,0

    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char

    for position, character in grid.items():

        #first problem
        if character == "X":
            for dir in directions:
                solution += find_xmas(position, grid, ["M","A", "S"], dir)

        #second problem
        if character == "A":
            solution2 += find_x_mas(position, grid)


    print(f"The solution to the first problem is {solution}")
    print(f"The solution to the second problem is {solution2}")