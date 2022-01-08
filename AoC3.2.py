with open('AoC3input.txt') as f:
    contents = f.readlines()

string_len = len(contents[0]) - 1
contents1 = list(map(lambda x: list(x), contents))
contents2 = list(map(lambda x: list(x), contents))

for j in range(0, string_len, 1):
    if len(contents1) == 1:
        break
    zeros = 0
    ones = 0
    for i in contents1:
        if i[j] == "0":
            zeros+=1
        else:
            ones+=1
 
    if zeros > ones:
        contents1 = list(filter(lambda x: x[j] == "0", contents1))
    else:
        contents1 = list(filter(lambda x: x[j] == "1", contents1))    

for j in range(0, string_len, 1):
    if len(contents2) == 1:
        break
    zeros = 0
    ones = 0
    for i in contents2:
        if i[j] == "0":
            zeros+=1
        else:
            ones+=1
 
    if zeros > ones:
        contents2 = list(filter(lambda x: x[j] == "1", contents2))
    else:
        contents2 = list(filter(lambda x: x[j] == "0", contents2))            

binary_generator = ""

for h in range(0, len(contents1[0]) - 1, 1):
    if contents1[0][h] == "0": 
        binary_generator+= "0"
    else:
        binary_generator+= "1"

binary_scrubber = ""

for h in range(0, len(contents2[0]) - 1, 1):
    if contents2[0][h] == "0": 
        binary_scrubber+= "0"
    else:
        binary_scrubber+= "1"

print(int(binary_scrubber, 2) * int(binary_generator, 2))
