import functools

patterns = []
towels = []

with open("input.in") as input_file:
    towels = input_file.readline().strip().split(",")
    
    #ignore the empty line
    input_file.readline()


    #parse the patterns
    for line in input_file:
        patterns.append(line.strip())

#max length of a single towel pattern
towels = [str.strip() for str in towels]
max_len = max([len(str) for str in towels])

#DFS
@functools.lru_cache(maxsize=409600)
def search(search_str):
    if len(search_str) == 0 or search_str in towels:
        return True
    
    for i in range(0, max_len+1):
        if i <= len(search_str):
            sub_str = search_str[0:i]
            if sub_str in towels:
                return_code = search(search_str[i::])
                if return_code:
                    return True
                
    return False

#DFS
@functools.lru_cache(maxsize=409600)
def search_cnt(search_str):
    if len(search_str) == 0:
        return 1
    
    return_code = 0
    
    for i in range(0, max_len+1):
        if i <= len(search_str):
            sub_str = search_str[0:i]
            if sub_str in towels:
                return_code+= search_cnt(search_str[i::])
                
    return return_code

possible_patterns = 0
possible_options = 0


for pattern in patterns:
    #print(f"Processing pattern: {pattern}")
    if search(pattern):
        possible_patterns += 1

    cnt = search_cnt(pattern)
    possible_options += cnt

print(f"Part 1: {possible_patterns}")
print(f"Part 2: {possible_options}")


