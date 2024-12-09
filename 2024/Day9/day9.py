DOT ="."

def compact_string(in_str):
    out_str = []
    element = in_str[0]
    element_count = 1
    for c in in_str[1::]:
        if c == element:
            element_count += 1
        else:
            if element != None:
                out_str.append((element, element_count))
            element = c
            element_count = 1

    if len(out_str) == 0 or out_str[len(out_str)-1] != (element, element_count):
        out_str.append((element, element_count))
    return out_str

#open file in
with open("input.in") as input_file:
    spaces = []
    characters = []
    file = []
    for line in input_file:
        counter = 0
        characters = list(map(int, line[0::2]))
        spaces = list(map(int, line[1::2]))

        file = []
        ##part 1
        #generate the full string
        for i in range(0,len(characters)):
            file.append((i, characters[i]))
            if len(spaces) > i:
                if spaces[i] > 0:
                    file.append((DOT, spaces[i]))

        index = 0
        result_file = []
        while index < len(file):
            if file[index][0] != DOT:
                result_file.append(file[index])
            else:
                spaces = file[index][1]
                temp_string = []
                for i in range(0, spaces):
                    last_element = file[len(file)-1]
                    while last_element[0] == DOT:
                        file.pop()
                        last_element = file[len(file)-1]

                    temp_string.append(last_element[0])

                    if file[len(file)-1][1] == 1:
                        last_element = file.pop()
                    else:
                        file[len(file)-1] = (file[len(file)-1][0], file[len(file)-1][1]-1)
                result_file = result_file + compact_string(temp_string)
            index = index+1
                



        #calculate result
        result =  0
        multiplier = 0
        for i in range(0,len(result_file)):
            for j in range(0, result_file[i][1]):
                result += multiplier*result_file[i][0]
                multiplier += 1

        print(f"The answer to the first part is {result}")