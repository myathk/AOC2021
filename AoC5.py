

rows, cols = (1000, 1000)
grid = [[0 for i in range(cols)] for j in range(rows)]


with open('AoC5input.txt') as f:
    contents = f.readlines()

for i in range(len(contents)):
    contents[i] = list(contents[i].rsplit(" -> "))


def mark_grid(pair):
    first_two = pair[0].rsplit(",")
    last_two = pair[1].rsplit(",")
    x1 = int(first_two[0])
    y1 = int(first_two[1])
    x2 = int(last_two[0])
    y2 = int(last_two[1])
    lower_x = min(x1, x2)
    lower_y = min(y1, y2)

    if (x1 == x2):
        for i in range(0, abs(y2 - y1) + 1):
            grid[lower_y + i][x1]+= 1
 
    elif (y1 == y2):

        for i in range(0, abs(x2 - x1) + 1, 1):

            grid[y1][lower_x + i]+= 1

    else:
        for i in range(0, abs(y2 - y1) + 1):
            if x2 > x1:
                if y2 > y1:
                    grid[y1 + i][x1 + i]+=1
                else:
                    grid[y1 - i][x1 + i]+= 1    
            else:
                if y2 > y1:
                    grid[y1 + i][x1 - i]+=1
                else:
                    grid[y1 - i][x1 - i]+=1

for i in contents:
    mark_grid(i)

count = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if grid[i][j] > 1:
            count+=1

print(count)