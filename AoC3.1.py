with open('AoC3input.txt') as f:
    contents = f.readlines()


length = len(contents[0])
output = ""

for j in range(0, length - 1, 1):
    zeros = 0
    ones = 0
    for i in contents:
        if i[j] == "0":
            zeros+=1
        else:
            ones+=1

    if ones > zeros:
        output+="1"
    else: 
        output+="0"    

gamma_rate = int(output, 2)
output1 = ""


for h in range(0, len(output), 1):
    if output[h] == "0":
        output1+="1"
    else:
        output1+="0"
epsilon_rate = int(output1, 2)

print(gamma_rate*epsilon_rate)
