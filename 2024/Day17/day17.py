import math

instructions = []
A = 0
B = 0
C = 0
pointer = 0
out = []

with open("input.in") as input_file:
    for line in input_file:
        in_arr = line.strip().split(":")
        match in_arr[0]:
            case "Program":
                instructions = list(map(int, in_arr[1].split(",")))
            case "Register A":
                A = int(in_arr[1].strip())
            case "Register B":
                B = int(in_arr[1].strip())
            case "Register C":
                C = int(in_arr[1].strip())

def get_combo_operand(operand):
    global A, B, C
    match operand:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return A
        case 5: return B
        case 6: return C
        case 7: 
            print("error, invalid program")
            return False

def treat_opcode(opcode, operand):
    global A, B, C, pointer, out
    match opcode:
        #adv: division
        case 0:
            A = A // (2**get_combo_operand(operand))
        #bxl: bitwise xor
        case 1:
            B = B ^ operand 
        #bst: modulo
        case 2:
            B = get_combo_operand(operand) % 8
        #jnz
        case 3:
            if A != 0: 
                pointer = operand
                return True
        #bxc
        case 4:
            B = B ^ C
        #output
        case 5:
            out.append(get_combo_operand(operand)%8)
        #bdv
        case 6:
            B = A // (2**get_combo_operand(operand))
        #cdv
        case 7:
            C = A // (2**get_combo_operand(operand))
    return False
        

while pointer < len(instructions)-1:
    jump = treat_opcode(instructions[pointer], instructions[pointer+1])
    if not jump:
        pointer += 2

print(",".join(str(o) for o in out))

##part 2
def count_matches(out):
    count = 0
    for i in range(0, len(out)):
        if out[i] == instructions[i]:
            count += 1
    return count

A = 0

#update start_A each time a next match is found to narrow down the solution
start_A = 71133671526017
print(start_A)
number_matches = 0
increments = {4:[], 5:[], 6:[], 7:[],8:[], 9:[], 10: [], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[]}
match_start = 0
increment = 1
program = ",".join(str(o) for o in instructions)
while True:
    pointer = 0
    A = start_A+ increment
    start_A = A
    out = []
    
    loop = 0
    while pointer < len(instructions)-1 :
        jump = treat_opcode(instructions[pointer], instructions[pointer+1])
        if not jump:
            pointer += 2

    if len(instructions) > len(out):
        #find the zone where the output is 16 instructions long
        start_A *= 2

    if len(instructions) == len(out) and count_matches(out) > 6:
        increments[count_matches(out)].append(start_A)
        print(start_A, count_matches(out))

    
    if len(instructions) == len(out) and count_matches(out) > number_matches:
        print("New match ", count_matches(out), start_A)
        number_matches = count_matches(out)
        if match_start > 0:
            #increment = start_A-match_start
            start_A = start_A-match_start
        match_start = start_A
        #every time a match occurs, the difference gets bigger, hence we can skip ahead a bit
    
    if len(out) > len(instructions):
        print("something went wrong")
        break

    #if start_A % 5000 == 0:
    #    print(start_A,increments)
    
    if program in ",".join(str(o) for o in out):
        print(start_A)
        break