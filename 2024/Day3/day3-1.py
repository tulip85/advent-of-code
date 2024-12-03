import re
from re import finditer


pattern = r"mul\(\d{1,3},\d{1,3}\)"
pattern_do = r"do\(\)"
pattern_dont = r"don\'t\(\)"


sum_of_mul_bo = 0

def mul(a,b):
    return a*b

with open("input.in") as input_file:
    for line in input_file:
        blackout = []

        #second part
        do = {match.start() for match in finditer(pattern_do,line)}
        dont = {match.start() for match in finditer(pattern_dont,line)}
        multiplications = {(match.start(), eval(match.group())) for match in  finditer(pattern, line)}

        #calculate blackout ranges
        for b_out in dont:
            index = b_out
            while index not in do and index <= len(line):
                blackout.append(index)
                index += 1

        #calculate the sum - first part
        sum_of_mul = sum([x for (y,x) in multiplications])

        #calculate the sum - second part
        sum_of_mul_bo = sum([x for (y,x) in multiplications if y not in blackout])

        print(f"Answer first star: {sum_of_mul}")
        print(f"Answer second star {sum_of_mul_bo}")






