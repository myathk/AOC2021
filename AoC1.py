with open('AoC1input.txt') as f:
    contents = f.readlines()

count = 0
len = len(contents)

contents = list(map(lambda x: int(x), contents))

for i in range(3, len, 1):
    if contents[i]> contents[i - 3]:
        count+= 1


print(count)