first_list = []
second_list = []
second_lookup = {}

#read the input
with open("input1.in") as input_file:
    for line in input_file:
        first_item, second_item = map(int, line.split("   ", maxsplit=1))
        first_list.append(first_item)
        second_list.append(second_item)
        second_lookup[second_item] = second_lookup.get(second_item, 0) + 1

#sort the two lists
first_list.sort()
second_list.sort()

#calculate distances and similarity
sum_distances = sum(abs(first - second) for first, second in zip(first_list, second_list))
sum_similarity = sum(first * second_lookup.get(first, 0) for first in first_list)

#print results
print(f"Distances: {sum_distances}")
print(f"Similarity: {sum_similarity}")