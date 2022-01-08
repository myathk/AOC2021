with open('AoC4input.txt') as f:
    contents = f.readlines()

input_numbers_arr = list(map(lambda x: int(x), contents[0].rsplit(",")))


list_of_grids = []
individual_grid = []
for i in range(2, len(contents) + 1, 1):

    if len(individual_grid) == 5:
        list_of_grids.append(individual_grid)
        individual_grid = []
            

    if (i - 1)%6 != 0:
        list_with_invalid = contents[i].rsplit(" ")
        list_with_all_valid = filter(lambda x: x != "", list_with_invalid)
        individual_grid.append(list(map(lambda x: int(x), list_with_all_valid)))

def check_grid(truth_grid):
    row_solved = False
    column_solved = False


    for i in range (0, len(truth_grid), 1):

        if len(list(filter(lambda x: x != "x", truth_grid[i]))) == 0:
            row_solved = row_solved or True


    for j in range (0, len(truth_grid[0]), 1):
        one_column_solved = True
        for i in range (0, len(truth_grid), 1):
            if truth_grid[i][j] != "x":
                one_column_solved = one_column_solved and False

        column_solved = column_solved or one_column_solved

    return row_solved or column_solved

def mark_grid(grid, number):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == number:
                grid[i][j] = "x"

    return grid

grids_solved = 0
last_grid_index = 0
called_number = 0
for i in input_numbers_arr:

    all_found = False
    for j in range(0, len(list_of_grids)):

        grid_checked_true = check_grid(list_of_grids[j])

        if grid_checked_true == False:
            mark_grid(list_of_grids[j], i)

            if check_grid(list_of_grids[j]):
                grids_solved += 1
                last_grid_index = j
                called_number = i
            
            if grids_solved == len(list_of_grids):
                break
    
    if grids_solved == len(list_of_grids):
        break

print(list_of_grids[j], i)