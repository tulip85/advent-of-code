
import functools

def calculate_next_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone))%2 == 0:
        number = str(stone)
        middle = int(len(number)/2)
        return [int(number[0:middle]),int(number[middle::])]
    else:
        return [stone * 2024]
    
@functools.lru_cache(maxsize=409600)
def process(element, it):
    if it == 0:
        return 1
    else:
        next = calculate_next_stone(element)
        ret = 0
        for n in next:
            ret += process(n,it-1)
        return ret



with open("input.in") as input_file:
    for line_in in input_file:
        line =  list(map(int, line_in.split()))

line.sort()

iterations = 75

memory = {}


new_queue = [] 
result = 0


for element in line:
    out = process(element, iterations)
    print(f"processed {element}: {out}")
    result += out



print(result)
