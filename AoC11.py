with open('AoC11input.txt') as f:
    contents = f.readlines()

    contents = list(map(lambda x: x.strip(), contents))

    contents = list(map(lambda x: list(map(lambda y: y, x)), contents))

class Octopus:
    def __init__(self, energy):
        self.energy = energy

    def increase(self):
        self.energy+= 1

    def set_zero(self):
        self.energy = 0

def has_up(row, column):
    return row > 0 

def has_down(row, column):
    return row < len(contents) - 1

def has_left(row, column):
    return column > 0

def has_right(row, column):
    return column < len(contents[0]) - 1 

def has_up_left(row, column):
    return has_up(row, column) and has_left(row, column) 

def has_up_right(row, column):
    return has_up(row, column) and has_right(row, column)

def has_down_left(row, column):
    return has_down(row, column) and has_left(row, column)

def has_down_right(row, column):
    return has_down(row, column) and has_right(row, column) 


for i in range(0, len(contents)):
    for j in range(0, len(contents[0])):
        contents[i][j] = Octopus(int(contents[i][j]))

def increase_energy(i, j):
    curr = contents[i][j]
    if curr.energy != 0:
        curr.increase()

steps = 488
flashes = 0

def recursively_flash(i, j):
    curr = contents[i][j]

    if curr.energy < 10:
        return

    global flashes
    flashes+=1

    curr.set_zero()


    if has_up(i, j):
        increase_energy(i - 1, j)
        recursively_flash(i - 1, j)

    if has_down(i, j):
        increase_energy(i + 1, j)
        recursively_flash(i + 1, j)

    if has_left(i, j):
        increase_energy(i, j - 1)
        recursively_flash(i, j - 1)

    if has_right(i, j):
        increase_energy(i, j + 1)
        recursively_flash(i, j + 1)
    
    if has_up_left(i, j):
        increase_energy(i - 1, j - 1)
        recursively_flash(i - 1, j - 1)
    
    if has_up_right(i, j):
        increase_energy(i - 1, j + 1)
        recursively_flash(i - 1, j + 1)

    if has_down_left(i, j):
        increase_energy(i + 1, j - 1)
        recursively_flash(i + 1, j - 1)

    if has_down_right(i, j):
        increase_energy(i + 1, j + 1)
        recursively_flash(i + 1, j + 1)


for step in range(0, steps):
    
    for i in range(0, len(contents)):
        for j in range(0, len(contents[0])):    
            curr = contents[i][j]
            curr.increase()

    for i in range(0, len(contents)):
        for j in range(0, len(contents[0])):   
            recursively_flash(i, j)

values = list(map(lambda x: list(map(lambda y: y.energy, x)), contents))

print(values)