with open('AoC13input.txt') as f:
    line = f.readline()

    list_of_coords = []
    while line != "\n":
        coords = [x for x in line.strip('\n').split(',')]
        list_of_coords.append(coords)

        line = f.readline()

max_x = 0
max_y = 0

for each in list_of_coords:
    max_x = max(max_x, int(each[0]))
    max_y = max(max_y, int(each[1]))

grid = []
for i in range(0, max_y + 1):
    grid.append([])

for i in range(0, max_y + 1):
    for j in range(0, max_x + 1):
        grid[i].append(0)


for each in list_of_coords:
    grid[int(each[1])][int(each[0])] = 1

def fold_along_x(x):
    first_half_grid = []
    for i in range(0, len(grid)):
        first_half_grid.append([])

    for i in range(0, len(grid)):
        for j in range(0, x):
            first_half_grid[i].append(grid[i][j])

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0]) - x - 1):  
            if first_half_grid[i][x - j - 1] != 1:
                 first_half_grid[i][x - j - 1] = grid[i][x + j + 1]

    
    return first_half_grid

def fold_along_y(y):
    first_half_grid = []
    for i in range(0, y):
        first_half_grid.append([])

    for i in range(0, y):
        for j in range(0, len(grid[0])):
            first_half_grid[i].append(grid[i][j])
    
    for i in range(0, len(grid) - y - 1):
        for j in range(0, len(grid[0])):  
            if first_half_grid[y - i - 1][j] != 1:
                 first_half_grid[y - i - 1][j] = grid[y + i + 1][j]
    
    return first_half_grid

def count_grid(grid):
    count = 0
    for i in grid:
        for j in i:
            if j == 1:
                count+=1

    return count


grid = fold_along_x(655)
grid = fold_along_y(447)
grid = fold_along_x(327)
grid = fold_along_y(223)
grid = fold_along_x(163)
grid = fold_along_y(111)
grid = fold_along_x(81)
grid = fold_along_y(55)
grid = fold_along_x(40)
grid = fold_along_y(27)
grid = fold_along_y(13)
grid = fold_along_y(6)

print(grid)


for line in grid:
    s = ""
    for char in line:
        if char == 1:
            s += "x"
        else:
            s +='-'
    print(s)