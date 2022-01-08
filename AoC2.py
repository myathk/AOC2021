with open('AoC2input.txt') as f:
    contents = f.readlines()


split = list(map(lambda x: x.rsplit() , contents))
  

horizontal = 0
depth = 0
aim = 0
for i in split:
    if i[0] == "forward":
        horizontal = horizontal + int(i[1])
        depth = depth + int(i[1]) * aim
    elif i[0] == "up":
        aim = aim - int(i[1])
    else:
         aim = aim + int(i[1])

print(horizontal * depth)