with open('AoC9input.txt') as f:
    contents = f.readlines()

    contents = list(map(lambda x: x.strip(), contents))

    contents = list(map(lambda x: list(map(lambda y: y, x)), contents))

basin_sizes = []
risk_level = 0

def has_up(row, column):
    return row > 0 

def has_down(row, column):
    return row < len(contents) - 1

def has_left(row, column):
    return column > 0

def has_right(row, column):
    return column < len(contents[0]) - 1 

class Grid:
    def __init__(self, value):
        self.travelled = False
        self.value = value

    def setTravelledTrue(self):
        self.travelled = True


for i in range(0, len(contents)):
    for j in range(0, len(contents[0])):
        contents[i][j] = Grid(int(contents[i][j]))


def recursive(i, j, basin_size_arr):
    curr = contents[i][j]
    curr.setTravelledTrue()
    basin_size_arr.append(1)

    if has_up(i, j) :
        if contents[i - 1][j].value != 9 and not contents[i - 1][j].travelled:
            recursive(i - 1, j, basin_size_arr)

    if has_down(i, j) :
        if contents[i + 1][j].value != 9 and not contents[i + 1][j].travelled:
            recursive(i + 1, j, basin_size_arr)

    if has_left(i, j) :
        if contents[i][j - 1].value != 9 and not contents[i][j - 1].travelled:
            recursive(i, j - 1, basin_size_arr)

    if has_right(i, j) :
        if contents[i][j + 1].value != 9 and not contents[i][j + 1].travelled:
            recursive(i, j + 1, basin_size_arr)

    return basin_size_arr


for i in range(0, len(contents)):
    for j in range(0, len(contents[0])):
        curr = contents[i][j]

        if curr.travelled == False and curr.value != 9:
            basin_size = len(recursive(i, j, []))
            basin_sizes.append(basin_size)

max1 = max(basin_sizes)
basin_sizes.remove(max1)
max2 = max(basin_sizes)
basin_sizes.remove(max2)
max3 = max(basin_sizes)

print(max1 * max2 * max3)
# for i in range(1, len(contents) - 1): #everything not in corners and 4 edges
#     for j in range(1, len(contents[0]) - 1):
#         curr = int(contents[i][j])

#         if curr < int(contents[i][j + 1]) and curr < int(contents[i][j - 1]) and curr < int(contents[i + 1][j]) and curr < int(contents[i - 1][j]):
#             risk_level+= 1 + curr

# for i in range(1, len(contents) - 1): #left and right most edges without corner
#     curr = int(contents[i][0])

#     if curr < int(contents[i][1]) and curr < int(contents[i + 1][0]) and curr < int(contents[i - 1][0]):
#         risk_level+= 1 + curr


#     curr = int(contents[i][len(contents[0]) - 1])

#     if curr < int(contents[i][len(contents[0]) - 2]) and curr < int(contents[i + 1][len(contents[0]) - 1]) and curr < int(contents[i - 1][len(contents[0]) - 1]):
#         risk_level+= 1 + curr


# for j in range(1, len(contents[0]) - 1): #up and down edges without corner
#     curr = int(contents[0][j])

#     if curr < int(contents[1][j]) and curr < int(contents[0][j - 1]) and curr < int(contents[0][j + 1]):
#         risk_level+= 1 + curr

#     curr = int(contents[len(contents) - 1][j])

#     if curr < int(contents[len(contents) - 2][j]) and curr < int(contents[len(contents) - 1][j - 1]) and curr < int(contents[len(contents) - 1][j + 1]):
#         risk_level+= 1 + curr

