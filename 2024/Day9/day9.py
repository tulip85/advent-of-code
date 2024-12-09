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

def compact_string_tuples(in_str):
    out_str = []
    element = None
    element_count = 0
    for c in in_str:
        if c[0] == DOT:
            if c[0] == element:
                element_count += c[1]
            else:
                if element != None and element == DOT:
                    out_str.append((element, element_count))
                element = c[0]
                element_count = c[1]
        else:
            if element == DOT:
                out_str.append((element, element_count))
            element = c[0]
            element_count = c[1]
            out_str.append(c)

    if element == DOT and (len(out_str) == 0 or out_str[len(out_str)-1] != (element, element_count) ):
        out_str.append((element, element_count))
    return out_str

def calculate_result(rs_file):
    result =  0
    multiplier = 0
    for i in range(0,len(rs_file)):
        
        for j in range(0, rs_file[i][1]):
            if rs_file[i][0] != DOT:
                result += multiplier*rs_file[i][0]
            multiplier += 1
    return result

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
            file.append((i, characters[i], i))
            if len(spaces) > i:
                if spaces[i] > 0:
                    file.append((DOT, spaces[i]))

        file2 = file.copy()
        ##part1
        ch_to_check = [c for c in file if c[0] != DOT]
        ch_to_check.reverse()

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

        ##part2
        index = len(file2)-1
        result_file_2 = file2.copy()
        i = index

        for c in ch_to_check:
            index = result_file_2.index(c)
            for i in range(0, index):
                if result_file_2[i][0] == DOT and result_file_2[i][1] >= c[1]:
                    #move the number
                    if c[1] < result_file_2[i][1]:
                        result_file_2[i] = (result_file_2[i][0], result_file_2[i][1]-c[1] )
                        result_file_2.insert(i, c)   
                        result_file_2[index+1] = (DOT, c[1])
                    else:
                        result_file_2.pop(i)
                        result_file_2.insert(i, c)   
                        result_file_2[index] = (DOT, c[1])
                    
                    result_file_2 = compact_string_tuples(result_file_2)
                    break
        


        print(f"The answer to the first part is {calculate_result(result_file)}")
        print(f"The answer to the second part is {calculate_result(result_file_2)}")