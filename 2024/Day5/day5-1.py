
all_rules = []
to_be_sorted = []

sum_of_middle_correct = 0
sum_of_middle_not_correct = 0

def is_sorted(list_in, rules):  
    for rule_first, rule_second in rules:
        if rule_first in list_in and rule_second in list_in:
            if list_in.index(rule_first) > list_in.index(rule_second):
                return False
    return True

#bubble sort
def perform_sort(list_in, rules):
    while not is_sorted(list_in, rules):
        for rule_first, rule_second in rules:
            if rule_first in list_in and rule_second in list_in and list_in.index(rule_first) > list_in.index(rule_second):
                first, second = list_in.index(rule_first),list_in.index(rule_second)
                list_in[second] = rule_first
                list_in[first] = rule_second
    return list_in


#open file in
with open("input1.in") as input_file:

    rules = True
    for line in input_file:
        if line == "\n":
            rules = False
        elif rules:
            input_a,input_b = list(map(int, line.strip().split("|")))
            all_rules.append((input_a, input_b))
        else:
            line_lst = list(map(int, line.strip().split(",")))
            
            if is_sorted(line_lst, all_rules):
                sum_of_middle_correct += line_lst[int((len(line_lst)-1)/2)]
            else:
                sorted_list = perform_sort(line_lst, all_rules)
                sum_of_middle_not_correct += sorted_list[int((len(sorted_list)-1)/2)]

print(sum_of_middle_correct, sum_of_middle_not_correct)