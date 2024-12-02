

def is_safe(line):
    previous = None
    direction = line[0] - line[1]
    for previous, element in zip(line, line[1:]):
        if previous is not None and not(((previous is not None and direction > 0 and previous > element) or (previous is not None and direction < 0 and previous < element)) and abs(previous-element)<= 3):
            return False  
    return True

with open("input.in") as input_file:
    counter = 0
    counter2 = 0
    for line_in in input_file:
        line =  list(map(int, line_in.split()))
        
        #first scenario: check if it is safe
        if is_safe(line):
            counter += 1
        
        #brute force: try removing one element and see if it is safe now
        if any(is_safe(line[:i] + line[i + 1:]) for i in range(len(line))):
             counter2 += 1

    print(f"The answer is {counter} for the first exercise and {counter2} for the second.")
