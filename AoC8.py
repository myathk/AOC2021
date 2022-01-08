# 0: 6
# 1: 2  unique
# 2: 5 
# 3: 5 
# 4: 4  unique
# 5: 5
# 6: 6
# 7: 3  unique
# 8: 7  unique
# 9: 6

with open('AoC8input.txt') as f:
    contents = f.readlines()


list_of_outputs = list(map(lambda x: x.rsplit(" | ")[1].rsplit(" "), contents))

list_of_patterns = list(map(lambda x: x.rsplit(" | ")[0].rsplit(" "), contents))

list_of_outputs_len = []

for each in list_of_outputs:
    element_len_arr = []
    for i in range(0, 4):
        
        if i != 3:
            element_len_arr.append(len(each[i]))
        else:
            element_len_arr.append(len(each[i]) - 1)

    list_of_outputs_len.append(element_len_arr)


sum = 0
for each in list_of_outputs_len:
    sum+= each.count(2)
    sum+= each.count(4)
    sum+= each.count(3)
    sum+= each.count(7)


output_without_newline = list(map(lambda x: list(map(lambda y: y.strip(), x)), list_of_outputs))

def matching_string(str1, str2):
        matching = True
        for each in str1:
            matching = matching and each in str2
            
        return matching

def get_each_output(each_pattern, each_output):
    
    one_chars = list(filter(lambda x: len(x) == 2, each_pattern))[0]
    four_chars = list(filter(lambda x: len(x) == 4, each_pattern))[0]
    seven_chars = list(filter(lambda x: len(x) == 3, each_pattern))[0]
    eight_chars = list(filter(lambda x: len(x) == 7, each_pattern))[0]

    list_of_five_chars = list(filter(lambda x: len(x) == 5, each_pattern))
    list_of_six_chars = list(filter(lambda x: len(x) == 6, each_pattern))

    three_chars = list(filter(lambda x: matching_string(one_chars, x), list_of_five_chars))[0]
    list_of_five_chars.remove(three_chars)

    filler_char = four_chars

    for each in one_chars:
        filler_char = filler_char.replace(each, "")


    five_chars = list(filter(lambda x: matching_string(filler_char, x), list_of_five_chars))[0]

    six_chars = list(filter(lambda x: not matching_string(one_chars, x), list_of_six_chars))[0]


    list_of_six_chars.remove(six_chars)


    nine_chars = list(filter(lambda x: matching_string(four_chars, x), list_of_six_chars))[0]

    output_str = ""

    
    for each in each_output:
        length_each = len(each)

        if length_each == 2:
            output_str+="1"
        elif length_each == 4:
            output_str+="4"
        elif length_each == 3:
            output_str+="7"
        elif length_each == 7:
            output_str+="8"
        elif length_each == 6:
            if matching_string(each, six_chars):
                output_str+="6"
            elif matching_string(each, nine_chars):
                output_str+="9"
            else:
                output_str+="0"
        else:
            if matching_string(each, three_chars):
                output_str+="3"
            elif matching_string(each, five_chars):
                output_str+="5"
            else:
                output_str+="2"

    return int(output_str)

result = 0
for i in range(0, len(list_of_outputs)):
    result+=get_each_output(list_of_patterns[i], output_without_newline[i])
 

print(result)