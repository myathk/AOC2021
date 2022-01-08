from queue import PriorityQueue

with open('AoC15input.txt') as f:
    line = f.readline()

    graph = []
    while line:
        row = [int(x) for x in line.rstrip("\n")]
        graph.append(row)

        line = f.readline()



rows = len(graph)
columns = len(graph[0])
 
estimate_grid = []
for i in range(0, rows * 5):
    estimate_grid.append([])
    for j in range(0, columns * 5):
        estimate_grid[i].append(0)

def has_up(row, column):
    return row > 0 

def has_down(row, column):
    return row < rows - 1

def has_left(row, column):
    return column > 0

def has_right(row, column):
    return column < columns - 1 

class Node:
    def __init__(self, weight, r, c):
        self.weight = weight
        self.c = c
        self.r = r

    
    def adjacent_nodes(self):
        adj_nodes_list = []
        r = self.r
        c = self.c

        if has_up(r, c):
            adj_nodes_list.append(graph[r - 1][c])
    
        if has_down(r, c):
            adj_nodes_list.append(graph[r + 1][c])

        if has_left(r, c):
            adj_nodes_list.append(graph[r][c - 1])

        if has_right(r, c):
            adj_nodes_list.append(graph[r][c + 1])
        
        return adj_nodes_list

def expand_graph():
    new_graph = []

    for i in range(0, rows * 5):
        new_graph.append([])
        for j in range(0, columns * 5):
            new_graph[i].append(0)

    for i in range(0, rows):
        for j in range(0, columns):
            curr = graph[i][j] - 1

            for r in range(0, 5):

                curr+=1

                if curr == 10:
                    curr = 1

                curr_copy = curr - 1
                for c in range(0, 5):
                   
                    curr_copy+=1
                    if curr_copy == 10:
                        curr_copy = 1

                    new_graph[i + rows * r][j + columns * c] = curr_copy


    return new_graph


new_graph = expand_graph()
graph = new_graph


rows = len(graph)
columns = len(graph[0])

for i in range(0, rows):
    for j in range(0, columns):
        graph[i][j] = Node(graph[i][j], i, j)



vertices = (rows) * (columns)
estimate_dict = dict()

set = []

estimate_grid = dict()

for i in range(0, rows):
    for j in range(0, columns):
        estimate_dict[graph[i][j]] = float('inf')

estimate_dict[graph[0][0]] = 0

def relax(u, v):

    dist_u = estimate_grid.get(u)
    dist_v = estimate_dict.get(v)

    if dist_v > dist_u + v.weight:
        estimate_dict.update({v: dist_u + v.weight})


while len(set) != vertices:
    curr_min = min(estimate_dict, key=estimate_dict.get) #vertex with min estimate right now
    estimate_grid[curr_min] = estimate_dict.get(curr_min)
    del estimate_dict[curr_min]

    set.append(curr_min)

    adj_nodes = curr_min.adjacent_nodes()

    for each in adj_nodes:
        if each not in set:
            relax(curr_min, each)


print(estimate_grid.get(graph[rows - 1][columns - 1]))