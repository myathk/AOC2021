data = dict()
pair_counts = dict()
with open('AoC14input.txt') as f:
    line = f.readline()

    while line:
        mapping = [x for x in line.strip('\n').split(' -> ')]
        if data.get(mapping[0]) == None:
            data[mapping[0]] = mapping[1]
        line = f.readline()

start_string = 'NNSOFOCNHBVVNOBSBHCB'
possible_chars = ['N', 'S', 'O', 'F', 'C', 'H', 'B', 'V', 'K', 'P']
arr = []

for i in range(0, len(start_string)):
    arr.append(start_string[i])

start_string = arr

for each in possible_chars:
    for second_element in possible_chars:
        new_pair = each + second_element
        pair_counts[new_pair] = 0


no_of_elements = dict()


for i in range(0, len(start_string) - 1):
    curr_pair = start_string[i] + start_string[i + 1]

    pair_counts[curr_pair] += 1


def add_to_dict(str):
    for each in str:
        if no_of_elements.get(each) == None:
            no_of_elements[each] =  1
        else:
            no_of_elements[each] = no_of_elements.get(each) + 1

add_to_dict(start_string)

def transform_string():
    global pair_counts
    copy_dict = pair_counts.copy()
    
    for each_pair in pair_counts: #for each possible pair inside
        char_to_add = data.get(each_pair) #char to add in between the pair

        if char_to_add != None: 
            no_of_pairs = pair_counts.get(each_pair)

            if no_of_pairs != 0:
                new_pair1 = each_pair[0] + char_to_add
                new_pair2 = char_to_add +  each_pair[1]

                copy_dict[new_pair1] += no_of_pairs
                copy_dict[new_pair2] += no_of_pairs
                copy_dict[each_pair] -= no_of_pairs
 
                if no_of_elements.get(char_to_add) == None:
                    no_of_elements[char_to_add] =  no_of_pairs
                else:
                    no_of_elements[char_to_add]+= no_of_pairs
    pair_counts = copy_dict

for i in range(0, 40):
    transform_string()

arr = []
for each in no_of_elements:
    arr.append(no_of_elements.get(each))

arr.sort()
print(arr[9] - arr[0])