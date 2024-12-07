all_ops = []
valid_ops = []
with open("input.in") as input_file:
    for line in input_file:
        input = line.split(":")
        all_ops.append([int(input[0])]+list(map(int, input[1].split())))

def is_valid(test):
    result = test[0]
    test_queue = [test[1]]
    for i in range(2, len(test)):
        temp = []
        for children in test_queue:
            temp.append(children * test[i])
            temp.append(children + test[i])
        test_queue = temp

    return sum([1 for x in test_queue if x == result])

def is_valid_part_two(test):
    result = test[0]
    test_queue = [test[1]]
    for i in range(2, len(test)):
        temp = []
        for children in test_queue:
            temp.append(children * test[i])
            temp.append(children + test[i])
            temp.append(int(str(children) + "" + str(test[i])))
        test_queue = temp

    return sum([1 for x in test_queue if x == result])

total = 0
total_part_two = 0
for ops in all_ops:
    if is_valid(ops) > 0:
        total += ops[0]
    if is_valid_part_two(ops) > 0:
        total_part_two += ops[0]

print(f"The total for part 1 is: {total}")
print(f"The total for part 2 is: {total}")