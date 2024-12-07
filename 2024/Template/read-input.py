#open file in
with open("input1.in") as input_file:


#convert a line to a list of ints
line =  list(map(int, line_in.split()))


# Parse the input into a grid dictionary
grid = {}
with open("input1.in") as input_file:
    for line_id, line in enumerate(input_file):
        for col_id, char in enumerate(line.strip()):
            grid[(line_id, col_id)] = char